# Import the required library
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image
image = cv2.imread('van_gogh.jpg')

# Converting BGR to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(rgb_image)

plt.waitforbuttonpress(2000)
plt.close('all')
