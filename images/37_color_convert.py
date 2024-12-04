# Convert image to different color spaces

import cv2

# load our input image
image = cv2.imread('images/scene_1.jpg')

# convert image to grayscale
grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# convert image to HSV
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# convert image to LAB
lab_img = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# display the images
cv2.imshow('Original Image', image)
cv2.waitKey(2000)

cv2.imshow('Grayscale Image', grayscale_img)
cv2.waitKey(2000)

cv2.imshow('HSV Image', hsv_img)
cv2.waitKey(2000)

cv2.imshow('LAB Image', lab_img)
cv2.waitKey(2000)

cv2.destroyAllWindows()
