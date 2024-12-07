# Program for applying bilateral filtering to a noisy image

import cv2

# Load the image
image = cv2.imread('images/noisy_image_taj.jpg')

# Apply bilateral filter with d = 15, sigmaColor = 80, sigmaSpace = 80
bilateral = cv2.bilateralFilter(image, 15, 80, 80)

# Display the image
cv2.imshow('image', bilateral)
cv2.waitKey(2000)

# compare with other kinds of filters
# Apply median filter
median = cv2.medianBlur(image, 5)

# Display the image
cv2.imshow('image', median)
cv2.waitKey(2000)

# Apply Gaussian filter
gaussian = cv2.GaussianBlur(image, (5, 5), 0)

# Display the image
cv2.imshow('image', gaussian)
cv2.waitKey(2000)

# Apply average filter
average = cv2.blur(image, (5, 5))

# Display the image
cv2.imshow('image', average)
cv2.waitKey(2000)

# Close all the windows
cv2.destroyAllWindows()
