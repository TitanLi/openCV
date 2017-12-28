# -*- coding: UTF-8 -*-

import numpy as np
import cv2

img = cv2.imread('apple.jpg')

# 圖片讀取
# 會儲存成一個 NumPy 的陣列
print type(img)

# NumPy 陣列的大小
#（RGB 彩色圖片的 channel 是 3，灰階圖片則為 1）
print img.shape

# 此為預設值，這種格式會讀取 RGB 三個 channels 的彩色圖片，而忽略透明度的 channel
imgColor = cv2.imread('apple.jpg',cv2.IMREAD_COLOR);
print imgColor.shape

# 以灰階的格式來讀取圖片
imgGraycale = cv2.imread('apple.jpg',cv2.IMREAD_GRAYSCALE);
print imgGraycale.shape

# 讀取圖片中所有的 channels，包含透明度的 channel
imgUnchanged = cv2.imread('apple.jpg',cv2.IMREAD_UNCHANGED);
print imgUnchanged.shape
