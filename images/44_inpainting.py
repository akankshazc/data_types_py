# Program to demonstrate image inpainting

import cv2
import numpy as np

# Load the image
damaged_img = cv2.imread('images/cat_damaged.png')

# get the shape of the image
height, width, _ = damaged_img.shape

# converting all pixels greater than zero to black while black becomes white
for i in range(height):
    for j in range(width):
        if damaged_img[i, j].sum() > 0:
            damaged_img[i, j] = 0
        else:
            damaged_img[i, j] = 255

# saving the mask
mask = damaged_img.copy()

# display the mask
cv2.imshow("/images/damaged_image_mask.png", mask)
cv2.waitKey(2000)
