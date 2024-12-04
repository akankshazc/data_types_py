# Program to demonstrate channel drop

from PIL import Image
import numpy as np

# Creating an image object, of the sample image
img = Image.open(r"images/van_gogh.jpg")

# Method 2: using pixel manipulation to drop the blue channel
img_arr = np.array(img, np.uint8)

# Setting the value of every pixel in the third column to 0
img_arr[::, ::, 2] = 0

# Creating an image object from the array
new_img_2 = Image.fromarray(img_arr)

# Displaying the image
new_img_2.show()
