# Program to create a border around an image

import cv2

# Load an image
image = cv2.imread('images/scene_1.jpg')

# Create a border around the image of blue color
border = cv2.copyMakeBorder(image, 10, 10, 10, 10,
                            cv2.BORDER_CONSTANT, value=[255, 0, 0])

# Display the image
cv2.imshow('Border', border)
cv2.waitKey(2000)


# Creating a border with reflection
border_reflect = cv2.copyMakeBorder(image, 100, 100, 50, 50,
                                    cv2.BORDER_REFLECT)

# Display the image
cv2.imshow('Border Reflect', border_reflect)
cv2.waitKey(2000)

cv2.destroyAllWindows()
