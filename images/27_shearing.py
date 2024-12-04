# Program to demonstrate image shearing

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load an image
image = cv2.imread('images/scene_1.jpg')

# convert BGR image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

width, height = image.shape[:2]

# Shearing parameters
shearX = 0.25
shearY = 0.1

# Shearing matrix
shear_matrix = np.array([[1, shearX, 0], [shearY, 1, 0]], dtype=np.float32)

# warpAffine() to apply the shearing matrix
sheared_image = cv2.warpAffine(image_rgb, shear_matrix,
                               (height, width))

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Plot original image
ax[0].imshow(image_rgb)
ax[0].set_title('Original Image')

# Plot sheared image
ax[1].imshow(sheared_image)
ax[1].set_title('Sheared Image')

# Remove ticks from the subplots
for axis in ax:
    axis.set_xticks([])
    axis.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()
