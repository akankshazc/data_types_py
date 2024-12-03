# Program to subtract images

import cv2

# Load the images
image1 = cv2.imread('landscape_1.jpg')
image2 = cv2.imread('landscape_2.jpg')

# Subtract the images
subtracted_image = cv2.subtract(image1, image2)

# Display the subtracted image
cv2.imshow('Subtracted Image', subtracted_image)

# Wait for the user to press any key
cv2.waitKey(10000)
