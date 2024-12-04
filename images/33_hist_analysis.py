# Program to represent an image with histogram

import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('images/scene_1.jpg', 0)

# Calculate the histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plot the histogram
plt.plot(hist, color='gray')
plt.show()

# another method
plt.hist(image.ravel(), 256, [0, 256])
plt.show()
