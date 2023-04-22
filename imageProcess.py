import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

image = cv2.imread(cv2.samples.findFile("Beginner.png"))

if image is None:
    sys.exit("Could not read the image")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Apply gray scale to image
image_blur = cv2.GaussianBlur(image_gray, (5,5), 0) #Remove noise from image

image_thresh = cv2.adaptiveThreshold(image_blur, 255, 1, 1, 11, 2) #

ret,th1 = cv2.threshold(image_blur,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(image_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(image_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [image, th1, th2, th3]

#cv2.imshow("Original Image", image)




contours, heirarchy = cv2.findContours(image_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_area = 0
c = 0
for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
                if area > max_area:
                    max_area = area
                    best_cnt = i
                    image = cv2.drawContours(image_thresh, contours, c, (0, 255, 0), 3)
        c+=1

mask = np.zeros((image_gray.shape),np.uint8)
cv2.drawContours(mask,[best_cnt],0,255,-1)
cv2.drawContours(mask,[best_cnt],0,0,2)
#cv2.imshow("mask", mask)


cv2.startWindowThread()
#cv2.namedWindow("Image")

#cv2.imshow("Image", image_gray)
#cv2.imshow("Image", image_thresh)
cv2.imshow("Image", mask)
#cv2.imshow("Original Image", image)


cv2.waitKey(0)
cv2.destroyAllWindows()


