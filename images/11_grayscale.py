# Import the required library
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image
image = cv2.imread('van_gogh.jpg', cv2.IMREAD_GRAYSCALE)

# Display the image
cv2.imshow('Grayscale Image', image)
cv2.waitKey(2000)
