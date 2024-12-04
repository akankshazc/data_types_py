# filter color in an image

import cv2
import numpy as np

# load our input image
image = cv2.imread('images/img_1.png')

# convert image to HSV
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define the range of blue color in HSV
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# create a mask for the blue color
mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

# apply the mask to the image
blue_img = cv2.bitwise_and(image, image, mask=mask)

# display the images
cv2.imshow('Original Image', image)
cv2.waitKey(2000)

cv2.imshow('Mask Image', mask)
cv2.waitKey(2000)

cv2.imshow('Blue Image', blue_img)
cv2.waitKey(2000)

cv2.destroyAllWindows()
