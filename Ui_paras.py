# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\lip-detection\lipstick-GUI\paras.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import cv2
import sys
import main
import os
import Ui_paras
import Ui_record
import time
import getROI
import canny
import locate
import main
import Ui_mainUI


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(383, 490)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 20, 51, 21))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(130, 40, 121, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 70, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(200, 70, 121, 16))
        self.label_9.setObjectName("label_9")
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setGeometry(QtCore.QRect(120, 70, 61, 22))
        self.spinBox_2.setProperty("value", getROI.border_thickness) # 外轮廓掩码宽度
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(Form)
        self.spinBox_3.setGeometry(QtCore.QRect(300, 70, 61, 22))
        self.spinBox_3.setProperty("value", getROI.face_thickness) # 脸部轮廓掩码宽度
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 150, 51, 21))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(130, 170, 131, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 230, 61, 16))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(20, 260, 61, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(20, 290, 61, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(110, 230, 61, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(110, 260, 61, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(110, 290, 61, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(240, 230, 61, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(240, 260, 61, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(240, 290, 61, 16))
        self.label_20.setObjectName("label_20")
        self.spinBox_7 = QtWidgets.QSpinBox(Form)
        self.spinBox_7.setGeometry(QtCore.QRect(160, 230, 61, 22))
        self.spinBox_7.setProperty("value", main.canny_params[4]) # 脸部低阈值
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QtWidgets.QSpinBox(Form)
        self.spinBox_8.setGeometry(QtCore.QRect(160, 260, 61, 22))
        self.spinBox_8.setProperty("value", main.canny_params[0]) # 头部低阈值
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_9 = QtWidgets.QSpinBox(Form)
        self.spinBox_9.setGeometry(QtCore.QRect(160, 290, 61, 22))
        self.spinBox_9.setProperty("value", main.canny_params[2]) # 膏身低阈值
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_10 = QtWidgets.QSpinBox(Form)
        self.spinBox_10.setGeometry(QtCore.QRect(300, 260, 61, 22))
        self.spinBox_10.setMaximum(1000)
        self.spinBox_10.setProperty("value", main.canny_params[1]) # 头部高阈值
        self.spinBox_10.setObjectName("spinBox_10")
        self.spinBox_11 = QtWidgets.QSpinBox(Form)
        self.spinBox_11.setGeometry(QtCore.QRect(300, 290, 61, 22))
        self.spinBox_11.setProperty("value", main.canny_params[3]) # 膏身高阈值
        self.spinBox_11.setObjectName("spinBox_11")
        self.spinBox_12 = QtWidgets.QSpinBox(Form)
        self.spinBox_12.setGeometry(QtCore.QRect(300, 230, 61, 22))
        self.spinBox_12.setMaximum(1000)
        self.spinBox_12.setProperty("value", main.canny_params[5])   # 脸部高阈值
        self.spinBox_12.setObjectName("spinBox_12")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(20, 200, 121, 16))
        self.label_21.setObjectName("label_21")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(160, 200, 61, 22))
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setProperty("value", main.harris_params[0]) # 响应常数k
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.spinBox_13 = QtWidgets.QSpinBox(Form)
        self.spinBox_13.setGeometry(QtCore.QRect(300, 200, 61, 22))
        self.spinBox_13.setMaximum(150000)
        self.spinBox_13.setProperty("value", canny.top_height)   # 头部高度
        self.spinBox_13.setObjectName("spinBox_13")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(240, 200, 51, 16))
        self.label_22.setObjectName("label_22")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 340, 51, 21))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(130, 360, 131, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(70, 380, 121, 16))
        self.label_23.setObjectName("label_23")
        self.spinBox_14 = QtWidgets.QSpinBox(Form)
        self.spinBox_14.setGeometry(QtCore.QRect(230, 380, 61, 22))
        self.spinBox_14.setMaximum(100)
        self.spinBox_14.setProperty("value", main.merge_dist) # 合并距离
        self.spinBox_14.setObjectName("spinBox_14")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 410, 361, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(20, 100, 121, 16))
        self.label_24.setObjectName("label_24")
        self.spinBox_15 = QtWidgets.QSpinBox(Form)
        self.spinBox_15.setGeometry(QtCore.QRect(120, 100, 61, 22))
        self.spinBox_15.setProperty("value", canny.color_para)    # 双边滤波灰度参数
        self.spinBox_15.setObjectName("spinBox_15")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(200, 100, 121, 16))
        self.label_25.setObjectName("label_25")
        self.spinBox_16 = QtWidgets.QSpinBox(Form)
        self.spinBox_16.setGeometry(QtCore.QRect(300, 100, 61, 22))
        self.spinBox_16.setProperty("value", canny.space_para)    # 双边滤波空间参数
        self.spinBox_16.setObjectName("spinBox_16")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 450, 361, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        self.params = []
        self.updateParams()
        
        
        
        self.pushButton.clicked.connect(self.showItems)
        
        self.pushButton_2.clicked.connect(self.undo)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "参数修改"))
        self.label.setText(_translate("Form", "预处理"))
        self.label_8.setText(_translate("Form", "外轮廓掩码宽度"))
        self.label_9.setText(_translate("Form", "脸部掩码宽度"))
        self.label_2.setText(_translate("Form", "特征提取"))
        self.label_7.setText(_translate("Form", "Canny脸部："))
        self.label_13.setText(_translate("Form", "Canny头部："))
        self.label_14.setText(_translate("Form", "Canny膏身："))
        self.label_15.setText(_translate("Form", "低阈值"))
        self.label_16.setText(_translate("Form", "低阈值"))
        self.label_17.setText(_translate("Form", "低阈值"))
        self.label_18.setText(_translate("Form", "高阈值"))
        self.label_19.setText(_translate("Form", "高阈值"))
        self.label_20.setText(_translate("Form", "高阈值"))
        self.label_21.setText(_translate("Form", "Harris 响应常数k："))
        self.label_22.setText(_translate("Form", "头部高度"))
        self.label_3.setText(_translate("Form", "缺陷定位"))
        self.label_23.setText(_translate("Form", "定位框合并距离"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.label_24.setText(_translate("Form", "双边滤波灰度参数"))
        self.label_25.setText(_translate("Form", "双边滤波空间参数"))
        self.pushButton_2.setText(_translate("Form", "取消修改"))
    
    
    def updateParams(self):
        self.params.append(self.spinBox_2.text())
        self.params.append(self.spinBox_3.text())
        self.params.append(self.spinBox_15.text())
        self.params.append(self.spinBox_16.text())
        self.params.append(self.doubleSpinBox.text())
        self.params.append(self.spinBox_13.text())
        self.params.append(self.spinBox_7.text())
        self.params.append(self.spinBox_12.text())
        self.params.append(self.spinBox_8.text())
        self.params.append(self.spinBox_10.text())
        self.params.append(self.spinBox_9.text())
        self.params.append(self.spinBox_11.text())
        self.params.append(self.spinBox_14.text())
        
        print('外轮廓掩码宽度：', self.spinBox_2.text())
        print('脸部轮廓掩码宽度：', self.spinBox_3.text())
        print('双边滤波灰度参数：', self.spinBox_15.text())
        print('双边滤波空间参数：', self.spinBox_16.text())
        
        print('响应常数k：', self.doubleSpinBox.text())
        print('头部区域高度：', self.spinBox_13.text())
        print('Canny脸部低：', self.spinBox_7.text())
        print('Canny脸部高：', self.spinBox_12.text())
        print('Canny头部低：', self.spinBox_8.text())
        print('Canny头部高：', self.spinBox_10.text())
        print('Canny膏身低：', self.spinBox_9.text())
        print('Canny膏身高：', self.spinBox_11.text())
        
        print('定位框合并距离：', self.spinBox_14.text())
    
    def showItems(self):
        self.updateParams()
        getROI.border_thickness = int(self.spinBox_2.text())
        getROI.face_thickness = int(self.spinBox_3.text())
        canny.color_para = int(self.spinBox_15.text())
        canny.space_para = int(self.spinBox_16.text())
        main.harris_params[0] = float(self.doubleSpinBox.text())
        canny.top_height = int(self.spinBox_13.text())
        main.canny_params[0] = int(self.spinBox_8.text())
        main.canny_params[1] = int(self.spinBox_10.text())
        main.canny_params[2] = int(self.spinBox_9.text())
        main.canny_params[3] = int(self.spinBox_11.text())
        main.canny_params[4] = int(self.spinBox_7.text())
        main.canny_params[5] = int(self.spinBox_12.text())
        main.merge_dist = int(self.spinBox_14.text())
             
        # paras = [main.canny_params[4], main.canny_params[0], main.canny_params[2], main.canny_params[5], main.canny_params[1], main.canny_params[3],main.harris_params[0],canny.color_para,canny.space_para,main.merge_dist,getROI.border_thickness,getROI.face_thickness,canny.top_height]
        
        
        
        
    
    def undo(self):
        self.spinBox_2.setProperty("value", self.params[0])    # 双边滤波灰度参数
        self.spinBox_3.setProperty("value", self.params[1])    # 双边滤波灰度参数
        self.spinBox_15.setProperty("value", self.params[2])    # 双边滤波灰度参数
        self.spinBox_16.setProperty("value", self.params[3])    # 双边滤波灰度参数
        self.doubleSpinBox.setProperty("value", self.params[4])    # 双边滤波灰度参数
        self.spinBox_13.setProperty("value", self.params[5])    # 双边滤波灰度参数
        self.spinBox_7.setProperty("value", self.params[6])    # 双边滤波灰度参数
        self.spinBox_12.setProperty("value", self.params[7])    # 双边滤波灰度参数
        self.spinBox_8.setProperty("value", self.params[8])    # 双边滤波灰度参数
        self.spinBox_10.setProperty("value", self.params[9])    # 双边滤波灰度参数
        self.spinBox_9.setProperty("value", self.params[10])    # 双边滤波灰度参数
        self.spinBox_11.setProperty("value", self.params[11])    # 双边滤波灰度参数
        self.spinBox_14.setProperty("value", self.params[12])    # 双边滤波灰度参数

