# Resizing an image

import cv2
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('images/landscape_1.jpg')

# Resize the image
half = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
smaller = cv2.resize(image, (150, 150))
stretch_near = cv2.resize(image, (780, 540), interpolation=cv2.INTER_NEAREST)

# Display the images
titles = ['Original', 'Half', 'Smaller', 'Stretch Near']
images = [image, half, smaller, stretch_near]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i])

plt.show()
