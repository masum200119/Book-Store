import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Laplacian filter to detect isolated points
laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=3)  # Kernel size can be adjusted
laplacian = cv2.convertScaleAbs(laplacian)  # Convert to 8-bit

# Display the original and point-detected images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(laplacian, cmap='gray')
plt.title("Point Detection (Laplacian)")
plt.axis('off')
plt.show()
