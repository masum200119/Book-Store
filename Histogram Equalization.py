import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a grayscale image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Step 1: Manually calculate the histogram
def manual_histogram(image):
    flattened_image = image.flatten()
    hist = np.zeros(256, dtype=int)
    for pixel_value in flattened_image:
        hist[pixel_value] += 1
    return hist

hist = manual_histogram(image)

# Step 2: Calculate the cumulative distribution function (CDF)
cdf = hist.cumsum()

# Step 3: Normalize the CDF
cdf_normalized = cdf * (255 / cdf[-1])  # Scale to [0, 255]

# Step 4: Map the pixel values to equalized values
equalized_image = np.interp(image.flatten(), np.arange(256), cdf_normalized).astype(np.uint8)

# Reshape the equalized image back to the original dimensions
equalized_image = equalized_image.reshape(image.shape)

# Plotting the original and equalized images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Equalized Image")
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.show()
