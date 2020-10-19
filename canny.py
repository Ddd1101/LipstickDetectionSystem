import numpy as np
import os
import cv2

top_height = 350
face_bias = 5
color_para = 10
space_para = 10


def getFaceLine(img):
    
    for i in range(img.shape[0] // 2, 0, -1):
        if np.any(img[i] != 0):
            return i

    return 0


def canny_withoutFace(input, face_height, face_t1, face_t2, bottom_t1, bottom_t2):
    
    face = input[:face_height, :input.shape[1]]
    bottom = input[face_height:, :input.shape[1]]
    cv2.bilateralFilter(face, 5, 5, 5)
    cv2.bilateralFilter(bottom, 5, 5, 5)
    canny_face = cv2.Canny(face, face_t1, face_t2, L2gradient=True)
    canny_bottom = cv2.Canny(bottom, bottom_t1, bottom_t2, L2gradient=True)
    canny_res = np.vstack((canny_face, canny_bottom))
    return canny_res

def canny_face_(face, t1, t2):
    cv2.bilateralFilter(face, 5, color_para, space_para)
    res = cv2.Canny(face, t1, t2, L2gradient=True)
    return res

def canny_(img, face, top_t1, top_t2, bottom_t1, bottom_t2, face_t1, face_t2):
    if np.any(face != 0):
        face_res = canny_face_(face, face_t1, face_t2)
        face_height = getFaceLine(face) + face_bias
        non_face = img - face
        non_face_res = canny_withoutFace(non_face, face_height, top_t1, top_t2, bottom_t1, bottom_t2)
        res = cv2.addWeighted(face_res, 1, non_face_res, 1, 0)
    else:
        res = canny_withoutFace(img, top_height, top_t1, top_t2, bottom_t1, bottom_t2)
    return res

def HarrisDetect(img, mask, borderMask, k, th):
    cornerStrength = cv2.cornerHarris(img, 3, 3, k)
    harrisCorners = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    
    harrisCorners[cornerStrength > th * cornerStrength.max()] = 255       # th = 0.01
    
    mask = mask.reshape((mask.shape[0], -1))
    borderMask = borderMask.reshape((borderMask.shape[0], -1))
   
    harrisCorners[mask == 0] = 0
    harrisCorners[borderMask == 255] = 0
    
    return harrisCorners
            