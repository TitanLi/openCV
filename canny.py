# -*- coding: UTF-8 -*-
# 將圖片線條化

import numpy as np
import cv2

img = cv2.imread('apple.jpg')

canny_img = cv2.Canny(img,100,100);

cv2.imshow('My Image', canny_img)

cv2.waitKey(0)
# 關閉所有 OpenCV 的視窗
cv2.destroyAllWindows()
