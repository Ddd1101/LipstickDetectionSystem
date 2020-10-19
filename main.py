import numpy as np
import os
import cv2
import getROI
import canny
import locate
import Ui_mainUI
import Ui_paras
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import os
import predict
import Ui_record

root = "D:/dataset0511/output"

canny_params = [ 60, 90, 30, 60, 60, 100 ]
harris_params = [ 0.001, 0.01 ]
merge_dist = 45

outPath = ''
resOutPath = ''


def single_test(filepath, facePath, bottomPath):
    
    filename = filepath.split('/')[-1]
    curname = filename
    
    RES = getROI.getROI_(filepath, facePath, 1, bottomPath)
    bottom = RES[0] # 底座
    ROI = RES[1]    # ROI
    border = RES[2] # 外轮廓掩码
    faceROI = RES[3]    # 脸部
    faceBorderMask = RES[4] # 脸部轮廓掩码
    
    if outPath != '' and Ui_record.save_param[0] == True:
        cv2.imwrite(outPath + '/roi/' + filename, ROI)
    if outPath != '' and Ui_record.save_param[1] == True:
        cv2.imwrite(outPath + '/foundation/' + filename, bottom)
    if outPath != '' and Ui_record.save_param[2] == True:
        cv2.imwrite(outPath + '/face/' + filename, faceROI)
    if outPath != '' and Ui_record.save_param[3] == True:
        cv2.imwrite(outPath + '/faceMask/' + filename, faceBorderMask)
    if outPath != '' and Ui_record.save_param[4] == True:
        cv2.imwrite(outPath + '/borderMask/' + filename, border)
    
    sobel = locate.getLapliacian(ROI)

    canny_res = canny.canny_(ROI, faceROI, canny_params[0], canny_params[1], canny_params[2], canny_params[3], canny_params[4], canny_params[5]) # Canny二值
    harris_res = canny.HarrisDetect(ROI, border, faceBorderMask, harris_params[0], harris_params[1])    # Harris二值
    
    if outPath != '' and Ui_record.save_param[5] == True:
        cv2.imwrite(outPath + '/harris/' + filename, harris_res)
    if outPath != '' and Ui_record.save_param[6] == True:
        cv2.imwrite(outPath + '/canny/' + filename, canny_res)
    
    locate.th = merge_dist
    
    res1, res2, recs, feature = locate.locate(canny_res, ROI, border, faceBorderMask, harris_res, merge_dist, sobel) # 融合特征

    if outPath != '' and Ui_record.save_param[7] == True:
        cv2.imwrite(outPath + '/res/' + filename, feature)
        
    if resOutPath != '':
        cv2.imwrite(resOutPath + '/res1_' + filename, res1)
        cv2.imwrite(resOutPath + '/res2_' + filename, res2)
    
    count = 10
    for filename in os.listdir('D:/dataset0511/output/cache/scratched/'):
        os.remove('D:/dataset0511/output/cache/scratched/' + filename)
        
    for rec in recs:
        block = ROI[rec.y1:rec.y2+1, rec.x1:rec.x2+1]
        cv2.imwrite('D:/dataset0511/output/cache/scratched/' + str(count) + '.bmp', block)
        count += 1
        if outPath != '' and Ui_record.save_param[8] == True:
            print("filename = ", curname)
            cv2.imwrite(outPath + '/blocks/' + curname.split('.')[0] + '_' + str(count-10) + '.bmp', block)
        # 结果子图
     

    if len(recs) == 0:
        labels = []
    else:
        labels = predict.predict_()
    # cv2.imshow('res1', res1)
    # cv2.imshow('res2', res2)
    # cv2.waitKey()
    
    return res1, res2, recs, labels

'''
for filename in os.listdir(root + '/body'):
    print(filename)
    if os.path.exists(root + '/face/' + filename):
        single_test(root + '/body/' + filename, root + '/face/' + filename, root + '/bottom/' + filename)
    else:
        single_test(root + '/body/' + filename, "", root + '/bottom/' + filename)
'''

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()

    # ui = Ui_mainUI.Ui_Form()
    
    myUI = Ui_mainUI.Ui_Form()
    
    print(myUI)
    
    myUI.setupUi(widget)
    myUI.updateParas()
    widget.show()
    sys.exit(app.exec_())
    



    
    