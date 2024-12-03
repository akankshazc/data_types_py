# bitwise OR operation of two images

import cv2

# Load two images
image1 = cv2.imread('images/image_1.png')
image2 = cv2.imread('images/image_2.png')

# Perform bitwise OR operation
output = cv2.bitwise_or(image1, image2)

# Display the images
cv2.imshow('Image 1', output)

cv2.waitKey(2000)
