import cv2
import numpy as np
import matplotlib.pyplot as plt

def power_law_transform(image, gamma=1.0, c=1):
    # Normalize the image to the range [0,1] for the transformation
    normalized_image = image / 255.0
    
    # Apply the power-law transformation (gamma correction)
    transformed_image = c * np.power(normalized_image, gamma)
    
    # Scale back to the range [0,255] and convert to uint8
    transformed_image = np.uint8(transformed_image * 255)
    
    return transformed_image

# Read the image in grayscale
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply power-law (gamma) transformation with gamma = 0.5 (brightens image)
gamma_corrected_img = power_law_transform(img, gamma=0.5)

# Apply power-law (gamma) transformation with gamma = 2.0 (darkens image)
gamma_dark_img = power_law_transform(img, gamma=2.0)

# Display the original and transformed images using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(gamma_corrected_img, cmap='gray')
plt.title('Gamma = 0.5 (Brightened)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(gamma_dark_img, cmap='gray')
plt.title('Gamma = 2.0 (Darkened)')
plt.axis('off')

plt.show()
