import cv2
import numpy as np
import imutils

# Read image
image = cv2.imread("image.png")

# Select ROI
r = cv2.selectROI("select the area", image)
cropped_image = image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rect)
box = np.int0(box)
# contour_image = cv2.drawContours(cropped_image,[box],-1,(0,255,0),10) 
center = (rect[0][0],rect[0][1])
width= round(rect[1][0])
height = round(rect[1][1])
theta=round(rect[2])
shape = ( cropped_image.shape[1], cropped_image.shape[0] )
matrix = cv2.getRotationMatrix2D( center=center, angle=theta, scale=1 )
cropped_image = cv2.warpAffine( src=cropped_image, M=matrix, dsize=shape )
# cv2.imwrite("final_picture.png",cropped_image)    --- If you want to save aligned cropped image
cv2.imshow("image", cropped_image)
cv2.waitKey(0)
    

