# -*- coding: UTF-8 -*-
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('./../xml/haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

#無限迴圈
while(True):
    #獲取視訊及返回狀態
    ret, img = video_capture.read()
    #將獲取的視訊轉化為灰色
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #檢測視訊中的人臉，並用vector儲存人臉的座標、大小（用矩形表示）
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #臉部檢測
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #顯示原影象
    cv2.imshow('img',img)
    #按q鍵退出while迴圈
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

#釋放攝像頭
video_capture.release()
#關閉所有視窗
cv2.destroyAllWindows()
