# Import the required library
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image
image = cv2.imread('van_gogh.jpg')

plt.imshow(image)

plt.waitforbuttonpress(2000)
plt.close('all')
