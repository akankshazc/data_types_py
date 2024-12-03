# Import opencv
import cv2

# Read the image
image = cv2.imread('images/van_gogh.jpg')

# Copying the image as its an inplace operation
output = image.copy()

# adding text to the image
text = cv2.putText(output, 'Van Gogh', (100, 100),
                   cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

# Display the image
cv2.imshow('Text', text)
cv2.waitKey(2000)
