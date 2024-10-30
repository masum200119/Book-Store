import cv2
import matplotlib.pyplot as plt

image = cv2.imread('masum.jpg')
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
mean_filtered = cv2.blur(image, (3, 5))  # Kernel size (5, 5)



plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(mean_filtered, cv2.COLOR_BGR2RGB))

plt.title("Mean Filter")
plt.axis("off")
plt.show()
