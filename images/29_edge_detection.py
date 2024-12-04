# Program to demonstrate edge detection

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('images/van_gogh.jpg')

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# apply Cannny edge detection
edges = cv2.Canny(image, threshold1=100, threshold2=500)

# create subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Display the original image
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')

# Display the edge detected image
axs[1].imshow(edges, cmap='gray')
axs[1].set_title('Edge Detected Image')

# remove the ticks
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# display the subplots
plt.tight_layout()
plt.show()
