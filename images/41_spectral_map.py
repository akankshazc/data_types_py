# spectral map of an image

import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('images/scene_1.jpg', 0)

# plot heat map image
plt.imshow(image, cmap='nipy_spectral')
plt.show()
