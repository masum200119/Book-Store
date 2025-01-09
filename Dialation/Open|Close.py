import cv2
import numpy as np

# Load a binary image
image = cv2.imread('image.jpg', 0)  # Load in grayscale

# Define a structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)  # Adjust kernel size as needed

# Perform opening
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Perform closing
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.waitKey(0)  # Wait for a key press to close the windows
cv2.destroyAllWindows()
