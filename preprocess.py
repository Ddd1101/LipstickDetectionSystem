import numpy as np
import os
import cv2
import getROI




def getROI(img):
    # img = img[:, img.shape[1] // 2 :]
    ori = img.copy()
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for ct in contours:
        x, y, w, h = cv2.boundingRect(ct)
        if w * h > 125000:
            # cv2.rectangle(m_ori, (x, y), (x+w, y+h), (0, 255, 0), 5)
            ROI = ori[y:y+h, x:x+w]
    return ROI


def grabCut(img, height):
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    rows = img.shape[0]
    cols = img.shape[1]

    
    rect = (0, rows - height, cols, height)  #划定区域
    
    
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,1,cv2.GC_INIT_WITH_RECT)#函数返回值为mask,bgdModel,fgdModel
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')#0和2做背景

    img = img * mask2[:,:, np.newaxis]  #使用蒙板来获取前景区域
    return img

def fill_color_demo(image, upPara, downPara):
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    copyIma = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv2.floodFill(copyIma, mask, (w//2, 130), (0, 255, 255), (downPara, downPara, downPara), (upPara, upPara, upPara), cv2.FLOODFILL_FIXED_RANGE)
    # print(copyIma)
    
    resmask = np.zeros([h, w], np.uint8)
    
    for i in range(resmask.shape[0]):
        for j in range(resmask.shape[1]):
            if copyIma[i][j][0] == 0 and copyIma[i][j][1] == 255:
                resmask[i][j] = 255
    
    kernel = np.ones((3, 3),np.uint8)
    resmask = cv2.morphologyEx(resmask, cv2.MORPH_CLOSE, kernel)
    contours, hierarchy = cv2.findContours(resmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(resmask, contours, -1, (255, 255, 255), cv2.FILLED)
    
    
    return resmask
################################################################################


path = 'C:/Users/cy/Desktop/final_ori'

bottom_height = 180
upPara = 25
downPara = 25


for filename in os.listdir(path):
    img = cv2.imread(path + '/' + filename)
    
    direc = filename.split('_')[1].split('.')[0]
    
    ROI = getROI(img)
    bottom = grabCut(ROI, bottom_height)
    cv2.imshow("bottom", bottom)
    
    
    if direc == '1':
        face = fill_color_demo(ROI, upPara, downPara)
        cv2.imshow('face', face)
    cv2.waitKey()

