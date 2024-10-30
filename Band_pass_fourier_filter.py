import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the image in grayscale
image = cv2.imread('masum.jpg', cv2.IMREAD_GRAYSCALE)

# Perform the Fourier transform and shift the zero frequency to the center
f_transform = np.fft.fftshift(np.fft.fft2(image))

# Get the center of the image
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2

# Create a band-pass mask
mask = np.ones((rows, cols), np.uint8)
r_out, r_in = 30, 10  # Define outer and inner radius for band-pass
cv2.circle(mask, (ccol, crow), r_out, 0, -1)  # Mask out low frequencies outside r_out
cv2.circle(mask, (ccol, crow), r_in, 1, -1)   # Retain frequencies within r_in

# Apply mask to the Fourier transform
filtered_transform = f_transform * mask

# Perform the inverse Fourier transform to obtain the filtered image
filtered_image = np.fft.ifft2(np.fft.ifftshift(filtered_transform))
filtered_image = np.abs(filtered_image)

# Display the filtered image
plt.imshow(filtered_image, cmap="gray")
plt.title("Band-Pass Filtered Image")
plt.axis("off")
plt.show()
