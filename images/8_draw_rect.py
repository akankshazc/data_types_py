# Import opencv
import cv2

# Read the image
image = cv2.imread('images/van_gogh.jpg')

# Copying the image as its an inplace operation
output = image.copy()

# Drawing a rectangle around the eyes in color green
rectangle = cv2.rectangle(output, (250, 250), (1000, 700), (0, 255, 0), 2)

# Display the image
cv2.imshow('Rectangle', rectangle)
cv2.waitKey(2000)
