import cv2
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 2)  # Kernel size (5, 5)

plt.imshow(cv2.cvtColor(gaussian_filtered, cv2.COLOR_BGR2RGB))
plt.title("Gaussian Filter")
plt.axis("off")
plt.show()
