import cv2
import numpy as np
import math
# from matplotlib import pyplot as plt
img_rgb = cv2.imread('qizi.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('qizi_w2.png',0)
h,w = template.shape[:2]
template2=cv2.imread("qizi_b2.png",0)
h1,w1=template2.shape[:2]
res2=cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
threshold2=0.89
loc = np.where(res >= threshold)
loc2=np.where(res2>=threshold2)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0] + w+6, pt[1] + h), (0, 255,0),1)
for pt1 in zip(*loc2[::-1]):
    cv2.rectangle(img_rgb,pt1,(pt1[0] + w1+7, pt1[1] + h1), (0, 0,255),1)
mas=-1
mas1=-1
mas2=-1
for pt1 in zip(*loc2[::-1]):
    for pt in zip(*loc[::-1]):
        pre=((pt1[0]-pt[0])**2+(pt1[1]-pt[1])**2)
        if(mas<pre):
            mas=pre

for pt1 in zip(*loc2[::-1]):
    for pt in zip(*loc[::-1]):
        pre2=(pt[0]-pt1[0])**2+(pt[1]-pt1[1])**2
        if(pre2==mas):
            cv2.line(img_rgb,(pt[0]+12,pt[1]+12),(pt1[0]+12,pt1[1]+12),(0,0,255),4)
 #求黑子之间的最大距离
for pt1 in zip(*loc2[::-1]):
    for pt2 in zip(*loc2[::-1]):
        ptt=(pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2
        if(mas1<ptt):
            mas1=ptt
#求白子之间的最大距离
for pt in zip(*loc[::-1]):
    for pt3 in zip(*loc[::-1]):
        ptt=(pt[0]-pt3[0])**2+(pt[1]-pt3[1])**2
        if(mas2<ptt):
            mas2=ptt
print("黑子之间的最大距离为：")
print(math.sqrt(mas1))
print("白子之间的最大距离：")
print(math.sqrt(mas2))
edges=cv2.Canny(img_gray,47,69,apertureSize=3)
minlengeth=100
maxlineGap=20
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minlengeth,maxlineGap)
# colors=((0,0,255),(255,0,0),(0,255,0))*30
# def shecolor(each):
#     if(each<=2):
#         return each
#     else:
#         return

for each in range(len(lines)):
    for x1,y1,x2,y2 in lines[each]:
        cv2.line(img_rgb,(x1,y1),(x2,y2),(255,0,0),4)
cv2.imshow("img_rgb",img_rgb)
cv2.waitKey(0)