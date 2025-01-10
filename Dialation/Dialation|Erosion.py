import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Define a kernel
kernel = np.ones((5, 5), np.uint8)  # You can adjust the kernel size (5x5 here)

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=5)

# Plot the images side by side
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Eroded image
plt.subplot(1, 2, 2)
plt.imshow(eroded_image, cmap='gray')
plt.title('Eroded Image')
plt.axis('off')

# Show the plot
plt.tight_layout()
plt.show()
