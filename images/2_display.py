# Program to explain the cv2.imshow method

import cv2

path = 'van_gogh.jpeg'

# Reading the image in default mode
image = cv2.imread(path)

# naming the window in which the image will appear
window_name = 'Image'

# Displaying the image
cv2.imshow(window_name, image)

cv2.waitKey(2000)

# Closing all open windows
cv2.destroyAllWindows()
