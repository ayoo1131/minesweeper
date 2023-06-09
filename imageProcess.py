import cv2
import numpy as np
import sys
from PIL import Image

#read in the image file from the repo
inputFileName = 'Beginner.png'
image = cv2.imread(cv2.samples.findFile(inputFileName))
originalImage=image
if image is None:
    sys.exit("Could not read the image")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Apply gray scale to image

ret, thresh = cv2.threshold(image_gray, 200, 255, cv2.THRESH_BINARY)#
image_gray[thresh == 255] = 100

image_blur = cv2.GaussianBlur(image_gray, (5,5), 0) #Remove noise from image and blur the image
image_thresh = cv2.adaptiveThreshold(image_blur, 255, 1, 1, 11, 2) #From the tutorial

image_test = image_thresh 
contours, heirarchy = cv2.findContours(image_test, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_area = 0
c = 0
for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
                if area > max_area:
                    max_area = area
                    best_cnt = i
                    image = cv2.drawContours(image_test, contours, c, (0, 255, 0), 3)
        c+=1

mask = np.zeros((image_test.shape),np.uint8)
cv2.drawContours(mask,[best_cnt],0,255,-1)
th4 = cv2.drawContours(mask,[best_cnt],0,0,2)

out = np.zeros_like(image_gray)
out[mask ==255] = image_gray[mask==255]

image_blur = cv2.GaussianBlur(out, (5,5), 0) #Remove noise from image
image_thresh = cv2.adaptiveThreshold(image_blur, 255, 1, 1, 11, 2) #From the tutorial
cv2.imwrite("blur.jpg", image_blur)
cv2.imwrite("thresh.jpg", image_thresh)

contours,x = cv2.findContours(image_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print( x)

image_test = originalImage
c=0
for i in contours:
    area=cv2.contourArea(i)
    if area > 1000/2:
            cv2.drawContours(image_test,contours, c, (0, 255, 0), 3)

    c+=1

cv2.imwrite("finalImage.jpg", image_test)

