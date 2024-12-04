# converting an image to grayscale

import cv2

# Load an image
image = cv2.imread('images/scene_1.jpg')

# Displaying the original image
cv2.imshow('Original Image', image)
cv2.waitKey(2000)

# Method 1: Using cvtColor
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Displaying the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(2000)

# Method 2: Using imread with flag value zero
gray_image_2 = cv2.imread('images/scene_1.jpg', 0)

# Displaying the grayscale image
cv2.imshow('Grayscale Image 2', gray_image_2)
cv2.waitKey(2000)

# Method 3: using pixel manipulation

# Obtain the dimensions of the image
height, width = image.shape[:2]

# Create a copy of the original image
gray_image_3 = image.copy()

# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
for i in range(height):
    for j in range(width):
        gray_image_3[i, j] = sum(image[i, j]) * 0.33

# Displaying the grayscale image
cv2.imshow('Grayscale Image 3', gray_image_3)
cv2.waitKey(2000)

cv2.destroyAllWindows()
