import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the main image and template
main_image = cv2.imread('main_image.jpg', cv2.IMREAD_GRAYSCALE)
template = cv2.imread('template.jpg', cv2.IMREAD_GRAYSCALE)

# Check if images are loaded
if main_image is None or template is None:
    print("Error: Unable to load images.")
    exit()

# Perform template matching
result = cv2.matchTemplate(main_image, template, cv2.TM_CCOEFF_NORMED)

# Find the best match location
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc  # Top-left corner of the best match
h, w = template.shape

# Draw a rectangle around the matched area
matched_image = main_image.copy()
cv2.rectangle(matched_image, top_left, (top_left[0] + w, top_left[1] + h), 255, 2)

# Plot the images
plt.figure(figsize=(12, 6))

# Main image
plt.subplot(1, 3, 1)
plt.imshow(main_image, cmap='gray')
plt.title('Main Image')
plt.axis('off')

# Template image
plt.subplot(1, 3, 2)
plt.imshow(template, cmap='gray')
plt.title('Template')
plt.axis('off')

# Result with matched rectangle
plt.subplot(1, 3, 3)
plt.imshow(matched_image, cmap='gray')
plt.title('Matched Image')
plt.axis('off')

plt.tight_layout()
plt.show()
