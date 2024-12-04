# Program to erode an image

import cv2
import numpy as np

# Load an image
image = cv2.imread('images/gfg.png')

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Erode the image
eroded = cv2.erode(image, kernel, cv2.BORDER_REFLECT)

# Display the image
cv2.imshow('Eroded', eroded)

cv2.waitKey(3000)
