# Denoising of colored images

import numpy as np
import cv2

# Load the image
image = cv2.imread('images/scene_1.jpg')

# denoise the image
dst = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(2000)
cv2.imshow('Denoised Image', dst)
cv2.waitKey(2000)

cv2.waitKey(0)
cv2.destroyAllWindows()
