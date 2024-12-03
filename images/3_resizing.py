# Import opencv
import cv2

# Read the image
image = cv2.imread('images/van_gogh.jpg')

# Resize the image
resized_image = cv2.resize(image, (200, 200))

# Display the resized image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(2000)
