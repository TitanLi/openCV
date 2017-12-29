# -*- coding: UTF-8 -*-
# /usr/share/opencv/haarcascades/ 可找到很多xml可使用

import numpy as np
import cv2

# 獲取人臉識別訓練數據
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')

# 讀取圖片
img = cv2.imread('a1.jpg')
# 將圖片變成灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 檢測視訊中的人臉，並用vector儲存人臉的座標、大小（用矩形表示）
# detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]])
# image:檢測對象CV_8U輸入矩陣的圖像
# scaleFactor:指定每個圖像比例縮小圖像大小的參數
# minNeighbors:指定每個候選矩形應該保留多少個鄰居的參數。 此參數將影響檢測到的人臉質量：較高的值會導致較少的檢測，但質量較高。
# flags:與舊版級聯分類器模型函數cvHaarDetectObjects的flags相同.此參數不被用於新版模型。(可省略)
# minSize:最小可能的對象的大小，小於的對象將被忽略
# maxSize:最大可能的對象的大小，大於的對象將被忽略
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)
print "Found {0} faces!".format(len(faces))
print faces
for (x,y,w,h) in faces:
    # opencv 的強大之處的一個體現就是其可以對圖片進行任意編輯，處理
    # 下面的這個函數最後一個參數指定的就是畫筆的大小
    # rectangle
    cv2.rectangle(img,(x,y),(x+w, y+h),(128,255,0),2)
    # circle
    cv2.circle(img,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

# 顯示原影像
cv2.imshow("found", img)
# 等待5秒後關閉
cv2.waitKey(5000)
