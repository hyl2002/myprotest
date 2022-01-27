import cv2
import numpy as np
img1=cv2.imread('f.png')
img2=cv2.imread('j.png')
img3=img1.copy()
img_original=cv2.imread("f.png")
img6=img1.copy()
def nothing(x):
    pass
MyTrackBarName="Blending weight"
window_Name='image'
print(img1.shape)
print(img2.shape)
rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]#roi为图一的相同大大小的图片
img2_Grey=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)#将第二张图变为灰度图，并且进行膨化操作
ret,mask=cv2.threshold(img2_Grey,200,250,cv2.THRESH_BINARY)
mask_inv=cv2.bitwise_not(mask)#将其黑白颠倒
# cv2.imshow("windows",mask_inv)
img1_BG=cv2.bitwise_and(roi,roi,mask=mask)
# cv2.imshow("windows",img1_BG)
img2_FG=cv2.bitwise_and(img2,img2,mask=mask_inv)
# cv2.imshow("windows",img2_FG)
dst=cv2.add(img1_BG,img2_FG)
img3[0:rows,0:cols]=dst
# cv2.imshow("ji",dst)
img9=img3.copy()
football=img1[385:450,150:220]
img5=football.copy()
# cv2.imshow("windows",football)
img3[375:460,140:230]=(0,0,255)
# img4=img1.copy()
#构造一个有方框的没篮球的图片img6
img3[385:450,150:220]=img5
# cv2.imshow("windows",img3)
football=img6[385:450,150:220]
img11=football.copy()
img6[375:460,140:230]=(0,0,255)
img6[385:450,150:220]=img11
cv2.namedWindow(window_Name)
cv2.createTrackbar(MyTrackBarName,window_Name,0,100,nothing)
cv2.setTrackbarPos(MyTrackBarName,window_Name,0)
# cv2.imshow(MyTrackBarName,img3)
# cv2.imshow("windows",img3)
def img_blending(wd_Name,trackBarName, image1, image2):
    weight_x: float = (100 - cv2.getTrackbarPos(trackBarName, wd_Name)) / 100  # 动态获取滑动条的值并转换成小数
    weight_y: float = 1 - weight_x  # 另一个权值为 1 - weight_x
    return cv2.addWeighted(image1,weight_x,image2,weight_y,0)  # 返回对象

while 1:
     cv2.imshow(window_Name,img_blending(window_Name,MyTrackBarName,img6,img3))
     k = cv2.waitKey(1) & 0xFF  # 按 “ESC” 退出
     if k == 27:
         break
cv2.waitKey(0)
cv2.destroyAllWindows()