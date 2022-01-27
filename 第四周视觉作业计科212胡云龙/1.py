import cv2
import numpy as np
from matplotlib import pyplot as plt
img1=cv2.imread('si.png',0)
# cv2.imshow("windows",img1)
img =cv2.medianBlur(img1,5)
ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)#以灰度图读入，然后采用阈值操作
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,7)#cv2.ADAPTIVE_THRESH_MEAN_C的含义是（x,y）减去C的邻域平均值
#THRESH_BINARY，正向二值化
cv2.imshow("windows",th2)
cv2.waitKey(0)
cv2.destroyWindow()
