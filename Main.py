# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 22:31:29 2021

@author: Mahfuz_Shazol
"""

import cv2

path='1.jpg'
wigthImg=700
heightImg=700

img=cv2.imread(path)
img=cv2.resize(img,(wigthImg,heightImg))
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny=cv2.Canny(imgBlur,10,50)

cv2.imshow("Original",img)
#cv2.imshow("Gray",imgGray)
#cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.waitKey(0)

