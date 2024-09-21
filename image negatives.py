import cv2
import numpy as np
import matplotlib.pyplot as plt

def negative_transform(image):
    # Get the maximum intensity value in the image (for 8-bit images, this is 255)
    L = 256
    
    # Apply the negative transformation
    negative_image = L - 1 - image
    
    return negative_image

# Read the image in grayscale
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply negative transformation
negative_img = negative_transform(img)

# Display the original and negative images using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(negative_img, cmap='gray')
plt.title('Negative Image')
plt.axis('off')

plt.show()
