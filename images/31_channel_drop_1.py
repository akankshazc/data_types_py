# Program to demonstrate channel drop using Pillow

from PIL import Image
import numpy as np

# Creating an image object, of the sample image
img = Image.open(r"images/van_gogh.jpg")

# Method 1: Using a transform matrix as an argument to the convert() method
# transform matrix (12 value tuple) for dropping the green channel
matrix = (1, 0, 0, 0,
          0, 0, 0, 0,
          0, 0, 1, 0)

# Applying the transform to the image
new_img_1 = img.convert("RGB", matrix)

# Displaying the image
new_img_1.show()
