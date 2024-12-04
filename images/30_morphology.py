# Program to demonstrate morphological image processing

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('images/van_gogh.jpg')

# Convert BGR to gray
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Creating a structuring element
kernel = np.ones((5, 5), np.uint8)

# perform dilation
dilated = cv2.dilate(image_rgb, kernel, iterations=3)

# perform erosion
eroded = cv2.erode(image_rgb, kernel, iterations=3)

# perform opening (erosion followed by dilation)
opening = cv2.morphologyEx(image_rgb, cv2.MORPH_OPEN, kernel)

# perform closing (dilation followed by erosion)
closing = cv2.morphologyEx(image_rgb, cv2.MORPH_CLOSE, kernel)

# create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Plot the dilated image
axs[0, 0].imshow(dilated, cmap='Greys')
axs[0, 0].set_title('Dilated Image')
axs[0, 0].set_xticks([])
axs[0, 0].set_yticks([])

# Plot the eroded image
axs[0, 1].imshow(eroded, cmap='Greys')
axs[0, 1].set_title('Eroded Image')
axs[0, 1].set_xticks([])
axs[0, 1].set_yticks([])

# Plot the opened image (erosion followed by dilation)
axs[1, 0].imshow(opening, cmap='Greys')
axs[1, 0].set_title('Opened Image')
axs[1, 0].set_xticks([])
axs[1, 0].set_yticks([])

# Plot the closed image (dilation followed by erosion)
axs[1, 1].imshow(closing, cmap='Greys')
axs[1, 1].set_title('Closed Image')
axs[1, 1].set_xticks([])
axs[1, 1].set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()
