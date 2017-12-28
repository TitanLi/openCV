# -*- coding: UTF-8 -*-

# /usr/share/opencv/haarcascades/ 可找到很多xml可使用

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')

img = cv2.imread('a1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)
print "Found {0} faces!".format(len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w, y+h),(128,255,0),2)
cv2.imshow("found", img)
cv2.waitKey(5000)
