# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\lip-detection\lipstick-GUI\mainUI.ui'
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

label_text = ['孔洞', '无缺陷（一阶段误检）', '刮擦', '余料']

def messageDialog(text):
    # app = QApplication(sys.argv)
    msg_box = QMessageBox(QMessageBox.Warning, '警告', text)
    msg_box.exec_()

class Ui_Form(object):
    def setupUi(self, Form):
        
        self.curr_path = ""
        self.flag = 0
        
        
        Form.setObjectName("Form")
        Form.resize(1093, 896)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(960, 140, 101, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(760, 140, 75, 21))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(440, 240, 301, 641))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 140, 61, 21))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 180, 431, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 131, 16))
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(250, 140, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 510, 131, 16))
        self.label_3.setObjectName("label_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(760, 240, 301, 641))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 140, 91, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 140, 91, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(840, 140, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 180, 61, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(850, 140, 101, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 180, 75, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 570, 131, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(320, 140, 431, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 30, 431, 61))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 420, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 450, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(230, 450, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(40, 480, 121, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(40, 290, 331, 16))
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(230, 420, 121, 16))
        self.label_16.setObjectName("label_16")

        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(40, 320, 331, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(140, 420, 54, 12))
        self.label_19.setObjectName("label_19")



        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(40, 370, 311, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(40, 540, 311, 16))
        self.label_15.setObjectName("label_15")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 600, 321, 281))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(40, 260, 331, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(40, 350, 311, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(540, 220, 91, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(880, 220, 91, 16))
        self.label_29.setObjectName("label_29")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(40, 390, 131, 16))
        self.label_10.setObjectName("label_10")

        self.pushButton.clicked.connect(self.click_choose_inputfile)
        self.pushButton_2.clicked.connect(self.click_choose_outputfile)
        self.pushButton_4.clicked.connect(self.singleTest)
        self.pushButton_3.clicked.connect(self.batchTest)
        self.pushButton_3.grabKeyboard()
        
        self.pushButton_5.clicked.connect(self.showNewWindow2)
        self.pushButton_6.clicked.connect(self.showNewWindow)
        # self.graphicsView_2.clicked.connect(self.changeRes)
        self.pushButton_6.clicked.connect(self.updateParas)
        
        self.retranslateUi(Form)
  
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        
        
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        
        
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "口红外观缺陷自动检测系统"))
        self.pushButton_3.setText(_translate("Form", "批量检测"))
        self.pushButton.setText(_translate("Form", "选择文件夹"))
        self.label.setText(_translate("Form", "输入路径"))
        self.lineEdit_2.setText(_translate("Form", self.curr_path))
        self.label_4.setText(_translate("Form", "核心检测参数设置："))
        self.label_3.setText(_translate("Form", "当前检测文件："))
        self.pushButton_6.setText(_translate("Form", "参数修改"))
        self.pushButton_5.setText(_translate("Form", "中间结果设置"))
        self.label_2.setText(_translate("Form", "输出路径"))
        self.pushButton_4.setText(_translate("Form", "单张检测"))
        self.pushButton_2.setText(_translate("Form", "选择文件夹"))
        self.label_5.setText(_translate("Form", "当前图片检测结果："))
        self.lineEdit.setText(_translate("Form", main.resOutPath))
        self.label_7.setText(_translate("Form", "口红外观缺陷自动检测系统 v0.2"))
        self.label_7.setFont(font)
        self.label_6.setText(_translate("Form", "ROI最小面积："))
        self.label_8.setText(_translate("Form", "外轮廓掩码宽度："))
        self.label_9.setText(_translate("Form", "脸部掩码宽度："))
        self.label_13.setText(_translate("Form", "头部区域高度："))
        self.label_14.setText(_translate("Form", "Canny低阈值：脸部 67 | 头部 55 | 膏身 40"))
        self.label_16.setText(_translate("Form", "定位框合并距离："))

        self.label_18.setText(_translate("Form", "Canny高阈值：脸部 157 | 头部 100 | 膏身 93"))
        self.label_19.setText(_translate("Form", "12500"))



        self.label_15.setText(_translate("Form", ""))
        
        self.label_26.setText(_translate("Form", "Harris响应常数k：0.005"))
        self.label_27.setText(_translate("Form", "双边滤波：灰度参数20，空间参数20"))
        self.label_28.setText(_translate("Form", "缺陷定位结果"))
        self.label_29.setText(_translate("Form", "缺陷特征分布"))
        self.label_10.setText(_translate("Form", "其他附加参数设置："))

        
        
    
    def click_choose_inputfile(self):
        dir_path=QFileDialog.getExistingDirectory(None, r"choose directory", r"C:\Users\Administrator\Desktop")
        self.curr_path = dir_path
        self.lineEdit.setText(self.curr_path)
    
    def click_choose_outputfile(self):
        dir_path=QFileDialog.getExistingDirectory(None, r"choose directory", r"C:\Users\Administrator\Desktop")
        main.resOutPath = dir_path
        self.lineEdit_2.setText(dir_path)

    
    
    def showImgs(self, res1, res2):
        res1 = cv2.resize(res1, (300, 640))
        res2 = cv2.resize(res2, (300, 640))
        
    
        res1 = cv2.cvtColor(res1, cv2.COLOR_BGR2RGB)
        res2 = cv2.resize(res2, (300, 640))
        
        totalBytes = res1.nbytes
        x = res1.shape[1]                                        #获取图像大小
        y = res1.shape[0]
        bytesPerLine = int(totalBytes/y)
        
        frame = QImage(res1, x, y, bytesPerLine, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        item=QGraphicsPixmapItem(pix)                      #创建像素图元
        
        scene=QGraphicsScene()                             #创建场景
        scene.addItem(item)
        self.graphicsView.setScene(scene)                  #将场景添加至视图
        
        frame2 = QImage(res2, x, y, bytesPerLine, QImage.Format_RGB888)
        pix2 = QPixmap.fromImage(frame2)
        item2=QGraphicsPixmapItem(pix2)                      #创建像素图元
        
        scene2=QGraphicsScene()                             #创建场景
        scene2.addItem(item2)
        self.graphicsView_2.setScene(scene2)                  #将场景添加至视图
        
    def singleTest(self):
        
        img_path = QFileDialog.getOpenFileName(None, "选择文件", "C:/Users/cy/Desktop/final_ori", "All Files (*);;Text Files (*.txt)")
        print(img_path[0])
        self.label_15.setText(img_path[0])
        img = cv2.imread(img_path[0])
        try:
            img.shape
        except:
            messageDialog('无法读取的文件格式。')
            return
        
        if img.shape[0] != 1024 or img.shape[1] != 1280:
            messageDialog('非标准检测格式的图像。')
            return
        
        
        self.textEdit.clear()
        filename = img_path[0].split('/')[-1]
        
        face = ''
        
        if os.path.exists('D:/dataset0511/output/face/' + filename):  
            face = 'D:/dataset0511/output/face/' + filename

        res1, res2, recs, labels = main.single_test('D:/dataset0511/output/body/' + filename, face, 'D:/dataset0511/output/bottom/' + filename)
        self.showImgs(res1, res2)
        
        count = 0
        
        if len(recs) == 0:
            self.textEdit.append('OK')
        else:
            self.textEdit.append(f'检测{len(recs)}处：刮擦{labels.count(2)}处，孔洞{labels.count(0)}处，余料{labels.count(3)}处，无缺陷{labels.count(1)}处，')
            for rec in recs:
                count += 1
                self.textEdit.append(str(count) + '['+ str(label_text[labels[count-1]]) +'] :' + str(rec.x1) + ',' + str(rec.x2) + ',' + str(rec.y1) + ',' + str(rec.y2))


        
        
    
    def showNewWindow(self):
        self.widget2 = QtWidgets.QWidget()
        self.ui2 = Ui_paras.Ui_Form()
        self.ui2.setupUi(self.widget2)
        
        self.widget2.show()
        self.updateParas()
        
        
        
    
    def showNewWindow2(self):
        self.widget3 = QtWidgets.QWidget()
        self.ui3 = Ui_record.Ui_Form()
        self.ui3.setupUi(self.widget3)
        
        self.widget3.show()
        
    
    def batchTest(self):
        if self.curr_path == '':
            messageDialog('输入路径为空。')
            return 

        if self.flag == 1:
            self.flag = 0
            return

        self.flag = 1
        
        delay, okPressed = QInputDialog.getInt(None, "设置图片延迟时间：","毫秒:", 1000, 0, 10000, 100)
                
        for filename in os.listdir(self.curr_path):
            
            if self.flag == 0:
                return
            
            print(filename)
            
            self.label_15.setText(self.curr_path + '/' + filename)
            
            face = ''
            if os.path.exists('D:/dataset0511/output/face/' + filename):  
                face = 'D:/dataset0511/output/face/' + filename
            
            if not os.path.exists('D:/dataset0511/output/body/' + filename):
                messageDialog('存在无法正常处理的图片。')
                self.flag = 0
                return 
            
            res1, res2, recs, labels = main.single_test('D:/dataset0511/output/body/' + filename, face, 'D:/dataset0511/output/bottom/' + filename)
            self.showImgs(res1, res2)
            self.textEdit.clear()
            
            count = 0
            
            for rec in recs:
                count += 1
                self.textEdit.append(str(count) + '['+ str(label_text[labels[count-1]]) +'] :' + str(rec.x1) + ',' + str(rec.x2) + ',' + str(rec.y1) + ',' + str(rec.y2))
            
            cv2.waitKey(delay)

               
            # time.sleep(delay / 1000)
        self.flag = 0
    
    
    def updateParas(self):
        self.label_26.setText('Harris响应常数k：'+str(main.harris_params[0]))
        self.label_14.setText('Canny低阈值：脸部 '+str(main.canny_params[4])+' | 头部 '+str(main.canny_params[0])+' | 膏身 '+str(main.canny_params[2]))
        self.label_18.setText('Canny高阈值：脸部 '+str(main.canny_params[5])+' | 头部 '+str(main.canny_params[1])+' | 膏身 '+str(main.canny_params[3]))
        self.label_27.setText('双边滤波：灰度参数'+str(canny.color_para)+'，空间参数'+str(canny.space_para))
        self.label_16.setText('定位框合并距离：'+str(main.merge_dist))
        self.label_8.setText('外轮廓掩码宽度：'+str(getROI.border_thickness))
        self.label_9.setText('脸部掩码宽度：'+str(getROI.face_thickness))
        self.label_13.setText('头部区域高度：'+str(canny.top_height))
            