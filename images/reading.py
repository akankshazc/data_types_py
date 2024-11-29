# Import the required library
import cv2

# Reading the image

image = cv2.imread('van_gogh.jpg')

h, w = image.shape[:2]

print(f"Height: {h}, Width: {w}")
