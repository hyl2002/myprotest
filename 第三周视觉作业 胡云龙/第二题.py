import cv2
import numpy as np
img1=cv2.imread("../red.jpg")
hsv=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
lower_red=np.array([156,43,46])
upper_red=np.array([180,255,255])
mask=cv2.inRange(hsv,lower_red,upper_red)
res=cv2.bitwise_and(img1,img1,mask=mask)

ret,threshold=cv2.threshold(res,175,255,cv2.THRESH_BINARY)
rows,cols=threshold.shape[:2]
M=cv2.getRotationMatrix2D((cols/2,rows/2),-20,0.6)
dst=cv2.warpAffine(threshold,M,(cols,rows))
cv2.imshow("windows",dst)
cv2.waitKey(0)
cv2.destroyWindow()
