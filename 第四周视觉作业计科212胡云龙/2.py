 import cv2
import numpy as np
img=cv2.imread("aol.png")
img1=img.copy()#复制原图象
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# hsv = cv2.medianBlur(hsv, 5)
down_c = np.array([0,100,0])
upper_C = np.array([10,255,255])
mask = cv2.inRange(hsv, down_c, upper_C)
res=cv2.bitwise_and(img,img,mask=mask)#对图像进行掩码处理
# cv2.imshow("windows",mask)
gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)#用灰度图读入
cv2.imshow("windows",gray)
ret,thresh=cv2.threshold(mask,127,255,cv2.THRESH_BINARY)#将图像进行二值化处理
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#获取边界的信息
# cv2.imshow("windows",hierarchy)
# 找出最大轮廓
area = []  # 定义一个空列表
for k in range(len(contours)):
    area.append(cv2.contourArea(contours[k]))  # 向列表里添加每一个轮廓的面积
max = np.argmax(np.array(area))  # 找到列表中面积最大的元素
cnt = contours[max]#此处的cnt表示的是最大的轮廓
# # 用矩形识别
x, y, w, h = cv2.boundingRect(cnt)#找出该轮廓的最大外界矩形
center=(int(x+w/2),int(y+h/2))#计算中心点
print('长', w, '宽', h,'中心点',center)
img = cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 5)

# 用圆识别
(x, y), radius = cv2.minEnclosingCircle(cnt)#返回的值为矩形的最大外接圆的中心，radius为圆的半径
center = (int(x), int(y))
radius = int(radius)
print('中心点', center, '半径', radius)
img = cv2.circle(img1, center, radius, (0, 255, 0), 5) #用函数画出圆
#输出四大极点
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])#使用的为元组
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
print('左极点', leftmost, '右极点', rightmost, '上极点', topmost, '下极点', bottommost)
cv2.imshow("windows",img1)
cv2.waitKey(0)
cv2.destroyWindow()