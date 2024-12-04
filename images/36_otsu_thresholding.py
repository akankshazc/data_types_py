# Otsu thresholding

import cv2
import numpy as np

# load our input image
image = cv2.imread('images/scene_1.jpg')

# convert image to grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply Otsu thresholding
ret, thresh1 = cv2.threshold(
    img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# display the images
cv2.imshow('Original Image', img)
cv2.waitKey(2000)

cv2.imshow('Otsu Threshold', thresh1)
cv2.waitKey(2000)

cv2.destroyAllWindows()
