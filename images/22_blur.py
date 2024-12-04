# program to blur an image

import cv2
import numpy as np

# Load an image
image = cv2.imread('images/scene_1.jpg')

# Display the original image
cv2.imshow('Original', image)
cv2.waitKey(2000)

# Gaussian blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow('Blurred', blurred)
cv2.waitKey(2000)

# Median blur
median = cv2.medianBlur(image, 5)
cv2.imshow('Median', median)
cv2.waitKey(2000)

# Bilateral blur
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral', bilateral)
cv2.waitKey(2000)

cv2.destroyAllWindows()
