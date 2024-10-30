import cv2
import matplotlib.pyplot as plt

image = cv2.imread('masum.jpg')
laplacian_filtered = cv2.Laplacian(image, cv2.CV_64F)

plt.imshow(cv2.convertScaleAbs(laplacian_filtered), cmap="gray")
plt.title("Laplacian Filter")
plt.axis("off")
plt.show()
