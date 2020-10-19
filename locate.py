import numpy as np
import os
import cv2
import predict


recs = []

th = 45
minSize = 15

def setT(t):
    th = t


class Rect:
    def __init__(self, x, y, w, h):
        self.x1, self.y1, self.w, self.h = x, y, w, h
        self.x2 = self.x1 + self.w
        self.y2 = self.y1 + self.h
    
    def area(self):
        return self.w*self.h


def calDist(rect1, rect2):

    cx1 = rect1.x1 + rect1.w // 2
    cy1 = rect1.y1 + rect1.h // 2
    cx2 = rect2.x1 + rect2.w// 2
    cy2 = rect2.y1 + rect2.h // 2

    dist = ((cx1 - cx2)** 2 + (cy1 - cy2)** 2)** 0.5
    
    return dist


def recs_or(rect1, rect2):  # 并集
    x1 = min(rect1.x1, rect2.x1)
    x2 = max(rect1.x2, rect2.x2)
    y1 = min(rect1.y1, rect2.y1)
    y2 = max(rect1.y2, rect2.y2)
    return Rect(x1, y1, x2 - x1, y2 - y1)


def recs_and(rect1, rect2): # 交集
    x1 = max(rect1.x1, rect2.x1)
    y1 = max(rect1.y1, rect2.y1)
    x2 = min(rect1.x2, rect2.x2)
    y2 = min(rect1.y2, rect2.y2)

    if x1 > x2 or y1 > y2:
        return 0
    else:
        return Rect(x1, y1, x2 - x1, y2 - y1)


def isInside(rect1, rect2):
    # 若两矩形相交的比例超过任意一个矩形的50%，则认为inside
    res = recs_and(rect1, rect2)
    if res == 0:
        return False
    else:
        if res.area() > 0.5 * rect1.area() or res.area() > 0.5 * rect2.area():
            return True
    return False


def update(rect):
    if len(recs) == 0:
        recs.append(rect)
        return
    
    for i in range(len(recs)):
        if calDist(recs[i], rect) < th:
            newRect = recs_or(recs[i], rect)
            del recs[i]
            recs.append(newRect)
            return
    
    recs.append(rect)
    return


def merge():
    for i in range(len(recs)):
        for j in range(i + 1, len(recs), 1):
            if isInside(recs[i], recs[j]):
                recs[i] = recs_or(recs[i], recs[j])
                del recs[j]
                return False
    return True


def getSobel(ROI):
    if len(ROI.shape) == 3:
        ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
    xgrad = cv2.Sobel(ROI, cv2.CV_8UC1, 1, 0, 3)
    ygrad = cv2.Sobel(ROI, cv2.CV_8UC1, 0, 1, 3)
    res = cv2.addWeighted(xgrad, 0.5, ygrad, 0.5, 0)
    return res

def getLapliacian(ROI):
    if len(ROI.shape) == 3:
        ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
    res = cv2.Laplacian(ROI, cv2.CV_8UC1, ksize = 3)
    return res

def calG_C(ROI, sobel, feature):
    if len(ROI.shape) == 3:
        ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
    sobel[feature==0] = 0
    
    totalG = 0
    totalN = 0
    totalColor = 0
    colorN = 0
    
    for i in range(ROI.shape[1]):
        for j in range(ROI.shape[0]):
            if sobel[j][i] != 0:
                totalG += sobel[j][i]
            if ROI[j][i] != 255:
                totalColor += ROI[j][i]
                colorN += 1
    
    if colorN == 0:
        return 0
    aveColor = totalColor / colorN
    return totalG / aveColor
                


def locate(img, ori, border, faceBorder, harris, t, sobel):
    
    final_recs = []
    
    recs.clear()
    setT(t)
    
    ori = cv2.cvtColor(ori, cv2.COLOR_GRAY2BGR)
    
    clone = ori.copy()
    
    border = border.reshape((border.shape[0], -1))
    faceBorder = faceBorder.reshape((faceBorder.shape[0], -1))
    
    img[border == 0] = 0
    img[faceBorder == 0] = 0
    
 
    img = cv2.addWeighted(img, 1, harris, 1, 0)
    
    feature = img.copy()
    
    
    
    contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    ori2 = ori.copy()
    cv2.drawContours(ori2, contours, -1, (0, 0, 255), 3)

    for ct in contours:
        x, y, w, h = cv2.boundingRect(ct)
        update(Rect(x, y, w, h))
    
    c = merge()

    while c == False:
        c = merge()

    
    count = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(len(recs)):
        if recs[i].area() > minSize:
            
            block_feature = img[recs[i].y1:recs[i].y2+1, recs[i].x1:recs[i].x2+1]
            block_sobel = sobel[recs[i].y1:recs[i].y2+1, recs[i].x1:recs[i].x2+1]
            
            block = clone[recs[i].y1:recs[i].y2+1, recs[i].x1:recs[i].x2+1]
            
            aveT = calG_C(block, block_sobel, block_feature)
            
            #if aveT > 10:
            count += 1
            cv2.rectangle(ori, (recs[i].x1, recs[i].y1), (recs[i].x2, recs[i].y2), (0, 255, 0), 1)
            cv2.putText(ori, str(count), (recs[i].x1, recs[i].y1), font, 0.8, (0, 0, 255), 1)
            final_recs.append(recs[i])
        
        
    return ori, ori2, final_recs, feature