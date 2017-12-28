# -*- coding: UTF-8 -*-

import numpy as np
import cv2

img = cv2.imread('apple.jpg')

# 寫入圖檔
# 可透過圖片的副檔名來指定輸出的圖檔格式
cv2.imwrite('output.jpg', img)

# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
cv2.imwrite('output1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])

# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
cv2.imwrite('output2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])
