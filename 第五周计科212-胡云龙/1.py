import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('house.png',0)
img1=cv2.imread('house.png')
equ=cv2.equalizeHist(img)
cv2.imshow("windows",equ)
hsv=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
hist=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
plt.imshow(hist,interpolation ='nearest')
plt.show()
cv2.waitKey(0)
cv2.destroyWindow()
