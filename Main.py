# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 22:31:29 2021

@author: Mahfuz_Shazol
"""

import cv2
import helper as hp
import numpy as np


path='1.jpg'
wigthImg=700
heightImg=700

img=cv2.imread(path)
img=cv2.resize(img,(wigthImg,heightImg))

imgCounters=img.copy()

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny=cv2.Canny(imgBlur,10,50)

counters,hierarchy=cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgCounters,counters,-1,(0,0,255),10)

imageBlank=np.zeros_like(img)

imageArray=([img,imgGray,imgBlur,imgCanny],
            [imgCounters,imageBlank,imageBlank,imageBlank])
imgStacked=hp.stackImages(imageArray,0.5)


#cv2.imshow("Original",img)
#cv2.imshow("Gray",imgGray)
#cv2.imshow("Blur",imgBlur)
#cv2.imshow("Canny",imgCanny)
cv2.imshow("Stacked Images",imgStacked)
cv2.waitKey(0)

