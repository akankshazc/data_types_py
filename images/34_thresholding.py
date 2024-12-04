# Simple thresholding or Binary thresholding

import cv2
import numpy as np

# load our input image
image = cv2.imread('images/scene_1.jpg')

# convert image to grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply different thresholding methods
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# display the images
cv2.imshow('Original Image', img)
cv2.waitKey(2000)

cv2.imshow('Binary Threshold', thresh1)
cv2.waitKey(2000)

cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.waitKey(2000)

cv2.imshow('Truncated Threshold', thresh3)
cv2.waitKey(2000)

cv2.imshow('Set to 0', thresh4)
cv2.waitKey(2000)

cv2.imshow('Set to 0 Inverted', thresh5)
cv2.waitKey(2000)

cv2.destroyAllWindows()
