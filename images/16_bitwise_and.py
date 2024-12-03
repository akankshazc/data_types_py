# bitwise conjunction of two images

import cv2

# Load two images
image1 = cv2.imread('images/image_1.png')
image2 = cv2.imread('images/image_2.png')

# Perform bitwise AND operation
output = cv2.bitwise_and(image1, image2)

# Display the output
cv2.imshow('Bitwise AND', output)

cv2.waitKey(2000)
