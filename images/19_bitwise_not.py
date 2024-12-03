# bitwise NOT operation of an image

import cv2

# Load an image
image = cv2.imread('images/image_1.png')

# Perform bitwise NOT operation
output = cv2.bitwise_not(image)

# Display the image
cv2.imshow('Image', output)

cv2.waitKey(2000)

# Close all the windows
cv2.destroyAllWindows()
