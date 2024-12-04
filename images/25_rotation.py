# Program to rotate an image

import cv2
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('images/scene_1.jpg')

# convert BGR image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Image rotation parameter
center = (image.shape[1] // 2, image.shape[0] // 2)
angle = 45
scale = 1

# getRotationMatrix2D() to get the rotation matrix for transformation
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# warpAffine() to apply the rotation matrix
rotated_image = cv2.warpAffine(image_rgb, rotation_matrix,
                               (image.shape[1], image.shape[0]))

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Plot original image
ax[0].imshow(image_rgb)
ax[0].set_title('Original Image')

# Plot rotated image
ax[1].imshow(rotated_image)
ax[1].set_title('Rotated Image')

# Remove ticks from the subplots
for axis in ax:
    axis.set_xticks([])
    axis.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()
