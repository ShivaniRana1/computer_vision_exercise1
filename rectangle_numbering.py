
import numpy as np
import os
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('image.png',0)
ret,thresh = cv.threshold(img,150,255,cv.THRESH_BINARY)
contours,_ = cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
count =[contours[6],contours[7],contours[1],contours[0]]
height = []
for cnt in count:
    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    # cv.drawContours(img,[box],0,(0,255,0),20)   This is to visulaize which area is being contoured
    height.append(max(rect[1]))
    
height = sorted(height)

for cnt in count:
    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    individual_height = (max(rect[1]))
    if individual_height in height:
        individual_index = height.index(individual_height)
        individual_index = str(individual_index+1)
        image = cv.putText(img, individual_index,(box[0][0],box[0][1]+150),cv.FONT_HERSHEY_SIMPLEX,1,(0, 128, 0),4)
 
cv.imwrite('numbering_image.png',image)

