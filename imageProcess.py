import cv2
import numpy as np
import sys

image = cv2.imread(cv2.samples.findFile("Beginner.png"))

if image is None:
    sys.exit("Could not read the image")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.startWindowThread()
cv2.namedWindow("Image")

#cv2.imshow("Image", image)
cv2.imshow("Image", image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


