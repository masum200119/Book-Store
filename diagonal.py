import cv2
import numpy as np

def diagonal_element_sum(img, include_secondary=False):
    # Convert to grayscale if it's a colored image
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Get the dimensions of the image
    rows, cols = img.shape
    
    # Primary diagonal sum (only along the minimum dimension for non-square images)
    min_dim = min(rows, cols)
    primary_diagonal_sum = np.sum([img[i, i] for i in range(min_dim)])
    
    # Secondary diagonal sum (if included, only along the minimum dimension)
    secondary_diagonal_sum = 0
    if include_secondary:
        secondary_diagonal_sum = np.sum([img[i, cols - 1 - i] for i in range(min_dim)])

    # Return the sum of primary (and secondary if included)
    return primary_diagonal_sum, secondary_diagonal_sum if include_secondary else primary_diagonal_sum

# Read the image
img = cv2.imread('image.jpg')

# Calculate the sum of diagonal elements
primary_sum, secondary_sum = diagonal_element_sum(img, include_secondary=True)

print("Primary diagonal sum:", primary_sum)
print("Secondary diagonal sum:", secondary_sum)
