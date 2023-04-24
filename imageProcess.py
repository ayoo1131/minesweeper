import cv2
import numpy as np
import sys
from PIL import Image

image = cv2.imread(cv2.samples.findFile("Beginner.png"))

if image is None:
    sys.exit("Could not read the image")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Apply gray scale to image

ret, thresh = cv2.threshold(image_gray, 200, 255, cv2.THRESH_BINARY)
image_gray[thresh == 255] = 100

image_blur = cv2.GaussianBlur(image_gray, (5,5), 0) #Remove noise from image
image_thresh = cv2.adaptiveThreshold(image_blur, 255, 1, 1, 11, 2) #From the tutorial
cv2.imwrite("blur.jpg", image_blur)
cv2.imwrite("thresh.jpg", image_thresh)

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
cv2.imwrite("crop.jpg", out)


#cv2.imwrite("grayImageOriginal.jpg", image_gray)
#cv2.imwrite("grayImageDarkEdge.jpg", gray)
#cv2.imwrite("blurImage.jpg", image_blur)
#cv2.imwrite("thresh1.jpg", image_thresh)
#cv2.imwrite("output2.jpg", th2)
#cv2.imwrite("output3.jpg", th3)
cv2.imwrite("output4.jpg", th4)
