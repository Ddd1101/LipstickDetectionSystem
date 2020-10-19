import numpy as np
import os
import cv2

minArea = 125000
border_thickness = 10
face_thickness = 15

def removeWhiteBorder(img, height, th):
    ROI = img[img.shape[0]-height:]
    _, res = cv2.threshold(ROI, th, 255, cv2.THRESH_TOZERO_INV)
    img[img.shape[0]-height:] = res
    return img


def getROI_(inputPath, facePath, th, bottomPath):
    
    RES = []
    
    img = cv2.imread(inputPath)
    bottom = cv2.imread(bottomPath)
    
    img = img[:, img.shape[1] // 2 :]
    bottom = bottom[:, bottom.shape[1] // 2 :]
    
    ori_bottom = bottom.copy()
    ori = img.copy()
    m_ori = img.copy()
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bottom = cv2.cvtColor(bottom, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, th, 255, cv2.THRESH_BINARY)
    _, bottom = cv2.threshold(bottom, th, 255, cv2.THRESH_BINARY)
    
    # tmp_binary = img.copy()
    
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    contours_bottom , _ = cv2.findContours(bottom, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for ct in contours_bottom:
        x, y, w, h = cv2.boundingRect(ct)
        if w * h > 1000: 
            bottomROI = ori_bottom[y:y+h, x:x+w]
            RES.append(bottomROI)
    
    for ct in contours:
        x, y, w, h = cv2.boundingRect(ct)
        if w * h > minArea:
            cv2.rectangle(m_ori, (x, y), (x+w, y+h), (0, 255, 0), 5)
            ROI = ori[y:y+h, x:x+w]
            if ROI.shape[2] == 3:
                ROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
            
            original_ROI = ROI.copy()
            ROI = removeWhiteBorder(ROI, 90, 120)
            RES.append(ROI)
            
            _, ROI = cv2.threshold(ROI, th, 255, cv2.THRESH_TOZERO)
            new_contours, _ = cv2.findContours(ROI, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            result = 255 - np.zeros((ROI.shape[0], ROI.shape[1], 1), dtype=np.uint8)
            
            cv2.drawContours(result, new_contours, -1, 0, border_thickness)
            RES.append(result)
            
            if facePath == "":
                face = np.zeros((h, w, 3), dtype=np.uint8)
                RES.append(face)
                faceBorderMask = 255 - np.zeros((ROI.shape[0], ROI.shape[1], 1), dtype=np.uint8)

                RES.append(faceBorderMask)
            else:
                face = cv2.imread(facePath, 0)
                face = face[:, face.shape[1] // 2 :]
                faceROI = face[y:y+h, x:x+w]
                RES.append(faceROI)
                
                _, faceBorder = cv2.threshold(faceROI, 1, 255, cv2.THRESH_BINARY)
                face_contours, _ = cv2.findContours(faceBorder, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                faceBorderMask = 255 - np.zeros((ROI.shape[0], ROI.shape[1], 1), dtype=np.uint8)
                cv2.drawContours(faceBorderMask, face_contours, -1, 0, face_thickness)
                
                RES.append(faceBorderMask)
            
            RES.append(original_ROI)
            return RES
    
    raise Exception(inputPath + 'ERROR: 无法得到ROI区域，阈值过高或图像过暗。')

    
                
            
            
            
    