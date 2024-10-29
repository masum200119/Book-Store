import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a grayscale image
image = cv2.imread('masum.jpg', cv2.IMREAD_GRAYSCALE)

# Flatten the image array to get a list of pixel values
pixels = image.flatten()

# Initialize an array to store the frequency of each pixel value (0-255)
frequency = np.zeros(256)

# Count occurrences of each pixel value
for pixel in pixels:
    frequency[pixel] += 1

# Calculate the probability of each pixel value
total_pixels = pixels.size
probability = frequency / total_pixels

# Plotting the probability histogram
plt.figure(figsize=(10, 5))
plt.bar(range(256), probability, color='gray')
plt.xlabel('Pixel Value')
plt.ylabel('Probability')
plt.title('Probability of Pixel Values')
plt.show()
