# import opencv library
import cv2

# Reading the image
image = cv2.imread('images/van_gogh.jpg')

# Extracting the RGB values of the pixel at location (160, 160)
b, g, r = image[160, 160]

print(f"Red: {r}, Green: {g}, Blue: {b}")
