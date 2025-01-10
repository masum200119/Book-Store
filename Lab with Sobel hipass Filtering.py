import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
pixels = img.flatten()
frq = np.zeros(256, dtype=int)
for i in pixels:
    frq[i] += 1
total = pixels.size
freq = frq / total
plt.bar(range(256), freq, color='gray')
plt.show()

cdf = frq.cumsum()
cdf_norm = (255 / cdf[-1]) * cdf
equalized_image = np.interp(img.flatten(), np.arange(256), cdf_norm).astype(np.uint8)
equalized_image = equalized_image.reshape(img.shape)
plt.imshow(equalized_image, cmap='gray')
plt.axis("off")
plt.show()

sobel_x = cv2.Sobel(equalized_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(equalized_image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)
plt.imshow(sobel_combined, cmap="gray")
plt.axis("off")
plt.show()

img1 = sobel_combined
pixelss = cv2.normalize(sobel_combined, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8).flatten()
frequency = np.zeros(256, dtype=int)
for i in pixelss:
    frequency[i] += 1
total = pixelss.size
freeq = frequency / total
plt.bar(range(256), freeq, color='gray')
plt.show()
