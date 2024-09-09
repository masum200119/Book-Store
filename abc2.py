import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv.imread("masum.JPG", cv.IMREAD_GRAYSCALE)

# Get the dimensions of the image
row, col = img.shape

# Initialize the histogram array
y = np.zeros((256), np.uint64)

# Calculate the histogram
for i in range(row):
    for j in range(col):
        y[img[i, j]] += 1

# Create an array for the x-axis (intensity values)
x = np.arange(0, 256)

# Plot the histogram as a bar chart
plt.bar(x, y, color="gray", align="center")
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Grayscale Histogram')
plt.show()
