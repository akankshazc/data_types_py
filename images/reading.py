# Import the required library
import cv2

# Reading the image

image = cv2.imread('van_gogh.jpg')

h, w, c = image.shape

print(f"Height: {h}, Width: {w}, Channels: {c}")
