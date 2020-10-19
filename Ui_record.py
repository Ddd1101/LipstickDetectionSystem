# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\lip-detection\lipstick-GUI\record.ui'
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
import os

save_param = [False,False,False,False,False,False,False,False,False]


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 425)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(30, 80, 101, 16))
        self.checkBox.setObjectName("checkBox")
        
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 110, 101, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 170, 111, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 140, 101, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 200, 111, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 320, 121, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setGeometry(QtCore.QRect(30, 290, 101, 16))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Form)
        self.checkBox_8.setGeometry(QtCore.QRect(30, 260, 101, 16))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_10 = QtWidgets.QCheckBox(Form)
        self.checkBox_10.setGeometry(QtCore.QRect(30, 230, 101, 16))
        self.checkBox_10.setObjectName("checkBox_10")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 161, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 30, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(440, 30, 37, 21))
        self.toolButton.setObjectName("toolButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 110, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(190, 140, 161, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(190, 170, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(190, 200, 161, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(190, 230, 161, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(190, 260, 161, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(190, 290, 161, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(190, 320, 161, 16))
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 360, 441, 41))
        self.pushButton.setObjectName("pushButton")
        
        self.checkBox.setChecked(save_param[0])
        self.checkBox_2.setChecked(save_param[1])
        self.checkBox_4.setChecked(save_param[2])
        self.checkBox_3.setChecked(save_param[3])
        self.checkBox_5.setChecked(save_param[4])
        self.checkBox_10.setChecked(save_param[5])
        self.checkBox_8.setChecked(save_param[6])
        self.checkBox_7.setChecked(save_param[7])
        self.checkBox_6.setChecked(save_param[8])
        
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.toolButton.clicked.connect(self.click_choose_outputfile)
        self.pushButton.clicked.connect(self.updateChecked)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "中间结果设置"))
        self.checkBox.setText(_translate("Form", "膏体ROI区域"))
        self.checkBox_2.setText(_translate("Form", "底座区域"))
        self.checkBox_3.setText(_translate("Form", "外轮廓掩码"))
        self.checkBox_4.setText(_translate("Form", "脸部区域"))
        self.checkBox_5.setText(_translate("Form", "脸部轮廓掩码"))
        self.checkBox_6.setText(_translate("Form", "缺陷定位结果子图"))
        self.checkBox_7.setText(_translate("Form", "融合特征"))
        self.checkBox_8.setText(_translate("Form", "Canny二值特征"))
        self.checkBox_10.setText(_translate("Form", "Harris二值特征"))
        self.label.setText(_translate("Form", "中间结果输出根目录root："))
        self.lineEdit.setText(_translate("Form", main.outPath))
        self.lineEdit.setReadOnly(True)
        self.toolButton.setText(_translate("Form", "..."))
        self.label_2.setText(_translate("Form", "root/roi"))
        self.label_3.setText(_translate("Form", "root/foundation "))
        self.label_4.setText(_translate("Form", "root/face"))
        self.label_5.setText(_translate("Form", "root/faceMask"))
        self.label_6.setText(_translate("Form", "root/borderMask"))
        self.label_7.setText(_translate("Form", "root/harris"))
        self.label_8.setText(_translate("Form", "root/canny"))
        self.label_9.setText(_translate("Form", "root/res"))
        self.label_10.setText(_translate("Form", "root/blocks"))
        self.pushButton.setText(_translate("Form", "应用更改"))

        
    
    def click_choose_outputfile(self):
        dir_path=QFileDialog.getExistingDirectory(None, r"choose directory", r"C:\Users\Administrator\Desktop")
        self.lineEdit.setText(dir_path)
    
    def updateChecked(self):
        save_param[0] = self.checkBox.isChecked()
        save_param[1] = self.checkBox_2.isChecked()
        save_param[2] = self.checkBox_4.isChecked()
        save_param[3] = self.checkBox_3.isChecked()
        save_param[4] = self.checkBox_5.isChecked()
        save_param[5] = self.checkBox_10.isChecked()
        save_param[6] = self.checkBox_8.isChecked()
        save_param[7] = self.checkBox_7.isChecked()
        save_param[8] = self.checkBox_6.isChecked()
        main.outPath = self.lineEdit.text()
        if not os.path.exists(main.outPath + '/roi'):
            os.mkdir(main.outPath + '/roi')
        if not os.path.exists(main.outPath + '/foundation'):
            os.mkdir(main.outPath + '/foundation')
        if not os.path.exists(main.outPath + '/face'):
            os.mkdir(main.outPath + '/face')
        if not os.path.exists(main.outPath + '/faceMask'):
            os.mkdir(main.outPath + '/faceMask')
        if not os.path.exists(main.outPath + '/borderMask'):
            os.mkdir(main.outPath + '/borderMask')
        if not os.path.exists(main.outPath + '/harris'):
            os.mkdir(main.outPath + '/harris')
        if not os.path.exists(main.outPath + '/canny'):
            os.mkdir(main.outPath + '/canny')
        if not os.path.exists(main.outPath + '/res'):
            os.mkdir(main.outPath + '/res')
        if not os.path.exists(main.outPath + '/blocks'):
            os.mkdir(main.outPath + '/blocks')

