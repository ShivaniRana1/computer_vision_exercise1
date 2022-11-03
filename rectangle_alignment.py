from copy import copy
from turtle import width
import cv2
import numpy as np

img1 = cv2.imread("image.png")
image_copy = img1.copy() 
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(blurred, 10, 100)

# define a (3, 3) structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# apply the dilation operation to the edged image
dilate = cv2.dilate(edged, kernel, iterations=1)
contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
i=0
print(len(contours))
for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    center = (rect[0][0],rect[0][1])
    width= round(rect[1][0])
    height = round(rect[1][1])
    theta=round(rect[2])
    shape = ( image_copy.shape[1], image_copy.shape[0] )
    matrix = cv2.getRotationMatrix2D( center=center, angle=theta, scale=1 )
    image1 = cv2.warpAffine( src=image_copy, M=matrix, dsize=shape )
    x = int( center[0] - width/2  )
    y = int( center[1] - height/2 )

    image1 = image1[ y:y+height, x:x+width ]
    i=i+1
    cv2.imwrite("straight_image{}.png".format(i),image1)
    

    
















