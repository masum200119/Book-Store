import cv2
import numpy as np

def boundary_element_sum(img):
    # Convert to grayscale if it's a colored image
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Get the dimensions of the image
    rows, cols = img.shape
    
    # Extract boundary elements
    top_row = img[0, :]          # First row
    bottom_row = img[-1, :]       # Last row
    left_column = img[:, 0]       # First column (excluding corners)
    right_column = img[:, -1]     # Last column (excluding corners)
    
    # Sum of all boundary elements
    boundary_sum = (
        np.sum(top_row) +             # Sum of top row
        np.sum(bottom_row) +          # Sum of bottom row
        np.sum(left_column[1:-1]) +   # Sum of left column excluding corners
        np.sum(right_column[1:-1])    # Sum of right column excluding corners
    )
    
    return boundary_sum

# Read the image
img = cv2.imread('image.jpg')

# Calculate the boundary element sum
sum_boundary = boundary_element_sum(img)

print("Boundary element sum:", sum_boundary)
