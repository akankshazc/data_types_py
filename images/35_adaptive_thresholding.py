# Adaptive thresholding

import cv2
import numpy as np

# load our input image
image = cv2.imread('images/scene_1.jpg')

# convert image to grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply adaptive thresholding
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 2)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 11, 2)

# display the images
cv2.imshow('Original Image', img)
cv2.waitKey(2000)

cv2.imshow('Adaptive Mean Threshold', thresh1)
cv2.waitKey(2000)

cv2.imshow('Adaptive Gaussian Threshold', thresh2)
cv2.waitKey(2000)

cv2.destroyAllWindows()
