# Program for image translation

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load an image
image = cv2.imread('images/scene_1.jpg')

# convert BGR image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

width, height = image.shape[:2]

tx, ty = 100, 70

# Translation matrix
translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)

# warpAffine() to apply the translation matrix
translated_image = cv2.warpAffine(image_rgb, translation_matrix,
                                  (height, width))

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Plot original image
ax[0].imshow(image_rgb)
ax[0].set_title('Original Image')

# Plot translated image
ax[1].imshow(translated_image)
ax[1].set_title('Translated Image')

# Remove ticks from the subplots
for axis in ax:
    axis.set_xticks([])
    axis.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()
