import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Laplacian filter to detect isolated points
# Apply Sobel filter in the x and y directions
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Detects vertical lines
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Detects horizontal lines

# Convert gradients to absolute scale and combine them
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
combined_sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Display the original and line-detected images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(sobel_x, cmap='gray')
plt.title("Vertical Lines (Sobel X)")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(sobel_y, cmap='gray')
plt.title("Horizontal Lines (Sobel Y)")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(combined_sobel, cmap='gray')
plt.title("Combined Line Detection (Sobel)")
plt.axis('off')

plt.show()
