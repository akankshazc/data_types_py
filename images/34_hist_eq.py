# Histogram equalization

import cv2
import numpy as np

# Load the image
image = cv2.imread('images/scene_1.jpg', 0)

# creating a histogram equalization
equ = cv2.equalizeHist(image)

# stacking images side-by-side
res = np.hstack((image, equ))

# show image input vs output
cv2.imshow('Input vs Output', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
