# Program to find the co-ordinates of contours in an image
import numpy as np
import cv2

# Load the image
font = cv2.FONT_HERSHEY_COMPLEX
image = cv2.imread('images/contour_shapes.jpg')

# Convert the image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Converting image to a binary image (black and white only image)
_, threshold = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)

# Find the contours in the image
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)

# Going through every contours found in the image
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.009*cv2.arcLength(cnt, True), True)

    # draw boundary of contours
    cv2.drawContours(image, [approx], 0, (0, 0, 255), 5)

    # find the co-ordinates of the vertices
    n = approx.ravel()
    i = 0

    for j in n:
        if (i % 2 == 0):
            x = n[i]
            y = n[i+1]

            # string containing the co-ordinates
            string = str(x) + " " + str(y)

            if (i == 0):
                # text on topmost co-ordinate
                cv2.putText(image, "Arrow tip", (x, y),
                            font, 0.5, (255, 0, 0))
            else:
                # text on remaining co-ordinates
                cv2.putText(image, string, (x, y),
                            font, 0.5, (0, 255, 0))

        i = i + 1

# Display the image
cv2.imshow('image', image)

# Wait for a key press and close the window
cv2.waitKey(2000)
cv2.destroyAllWindows()
