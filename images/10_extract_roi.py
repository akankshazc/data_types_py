# Import opencv library
import cv2

# read the image
image = cv2.imread('images/van_gogh.jpg')

# define the region of interest
roi = image[160:320, 160:320]

# display the region of interest
cv2.imshow('Region of Interest', roi)
cv2.waitKey(2000)
