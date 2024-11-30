# Program to explain the cv2.imwrite() method

# Import the required library
import cv2
import os

# Image path
path = 'van_gogh.jpg'

# Directory you want to save image in
# we are saving the image in the working directory for simplicity
directory = '../images'

# Reading the image
image = cv2.imread(path)

# Change the current directory
os.chdir(directory)

# List files and directories
print("Before saving image:")
print(os.listdir(directory))

# Filename
filename = 'saved_image.jpg'

# Saving the image
cv2.imwrite(filename, image)

# List files and directories
print("After saving image:")
print(os.listdir(directory))

print("Image saved successfully")
