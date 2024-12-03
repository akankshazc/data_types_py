# Program to add two images

import cv2

# reading the images
image1 = cv2.imread('images/scene_1.jpg')
image2 = cv2.imread('images/scene_2.jpg')

# adding the images
weighted_sum = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

# displaying the images
cv2.imshow('Weighted Image', weighted_sum)

cv2.waitKey(2000)
