# -*- coding: UTF-8 -*-

import numpy as np
import cv2

img = cv2.imread('apple.jpg')

# 顯示圖片
cv2.imshow('My Image', img)

# 按下任意鍵則關閉所有視窗
# 函數是用來等待與讀取使用者按下的按鍵，而其參數是等待時間（單位為毫秒），若設定為 0 就表示持續等待至使用者按下按鍵為止
cv2.waitKey(0)
# 關閉所有 OpenCV 的視窗
cv2.destroyAllWindows()
# 關閉 'My Image' 視窗
cv2.destroyWindow('My Image')

# 讓視窗可以自由縮放大小
cv2.namedWindow('My Image1', cv2.WINDOW_NORMAL)
cv2.imshow('My Image1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
