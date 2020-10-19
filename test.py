import os
import numpy
import cv2

path = 'C:\\Users\\cy\\Desktop\\original'

'''
def getTop(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] != 0:
                return i

def getBottom(img):
    for i in range(img.shape[0] - 1, -1, -1):
        for j in range(img.shape[1]):
            if img[i][j] != 0:
                return i


maxTop = 0
minBottom = 10000

for filename in os.listdir(path):
    img = cv2.imread(path + '/' + filename, 0)
    img = img[:, img.shape[1] // 2 : img.shape[1]]
    top = getTop(img)
    bottom = getBottom(img)
    if top > maxTop:
        maxTop = top
    if bottom < minBottom:
        minBottom = bottom

print("top", maxTop)
print("bottom", minBottom)
'''

'''
for filename in os.listdir(path):
    print(filename)
    idx = int(filename.split('_')[0])
    dire = int(filename.split('_')[1].split('.')[0])
    
    pn = ''
    if idx % 2 == 0:
        pn = str(idx) + '_' + str(idx - 1)
    else:
        pn = str(idx) + '_' + str(idx + 1)
    
    img = cv2.imread('D:/dataset0430/batch_5/' + pn + '/' + str(dire) + '.tiff')
    
    print('D:/dataset0430/batch_5/' + pn + '/' + str(dire) + '.tiff')
    
    img = img[562:1586, 1168:]
    
    cv2.imwrite(path + '/new2/' + filename, img)
'''

'''
for filename in os.listdir(path):
    print(filename)
    img = cv2.imread(path + '/' + filename)
    img = img[562:1586, 1168:]
    cv2.imwrite(path + '/new/' + filename, img)
'''

for filename in os.listdir(path):
    print(filename)
    img = cv2.imread(path + '/new/' + filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, contours, -1, (255, 255, 255), cv2.FILLED)
    
    mask = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    img2 = cv2.imread(path + '/new2/' + filename)
    
    img2[mask==0] = 0
    
    img2 = cv2.GaussianBlur(img2, (5, 5), 0)
    
    
    
    cv2.imshow('res', img2)
    cv2.waitKey()