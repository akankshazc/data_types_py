import cv2

# Reading the image
image = cv2.imread('images/van_gogh.jpg')

# Splitting the image into its color channels
blue, green, red = cv2.split(image)

# Display the image
cv2.imshow('Blue Channel', blue)
cv2.waitKey(2000)

cv2.imshow('Green Channel', green)
cv2.waitKey(2000)

cv2.imshow('Red Channel', red)
cv2.waitKey(2000)

# Destroy all windows
cv2.destroyAllWindows()
