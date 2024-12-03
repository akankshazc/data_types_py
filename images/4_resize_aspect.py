# Import opencv
import cv2

# Read the image
image = cv2.imread('images/van_gogh.jpg')

# Calculate the aspect ratio
ratio = 200.0 / image.shape[1]

# Creating a tuple with the new dimensions
dimensions = (200, int(image.shape[0] * ratio))

# Resize the image
resized_image = cv2.resize(image, dimensions)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(2000)
