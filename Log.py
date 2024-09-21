import cv2
import numpy as np
import matplotlib.pyplot as plt

def log_transform(image, c=1):
    # Normalize the image to the range [0,1]
    normalized_image = image / 255.0
    
    # Apply the log transformation
    log_transformed_image = c * np.log(1 + normalized_image)
    
    # Scale back to the range [0,255] and convert to uint8
    log_transformed_image = np.uint8(log_transformed_image / log_transformed_image.max() * 255)
    
    return log_transformed_image

# Read the image in grayscale
img = cv2.imread('masum.jpg', cv2.IMREAD_GRAYSCALE)

# Apply log transformation
log_transformed_img = log_transform(img, c=1)

# Display the original and log-transformed images using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(log_transformed_img, cmap='gray')
plt.title('Log Transformed Image')
plt.axis('off')

plt.show()
