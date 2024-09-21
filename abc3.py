import cv2
import numpy as np
import matplotlib.pyplot as plt

def divide_img_blocks(img, n_blocks=(2, 2)):
    # Split the image horizontally into n_blocks[0] rows
    horizontal_blocks = np.array_split(img, n_blocks[0], axis=0)
    # Further split each horizontal block vertically into n_blocks[1] columns
    splitted_img = [np.array_split(block, n_blocks[1], axis=1) for block in horizontal_blocks]
    
    return splitted_img  # Return a list of lists containing the image blocks

# Read the image
img = cv2.imread('image.jpg')

# Convert BGR (OpenCV default) to RGB for displaying with matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Divide the image into blocks
blocks = divide_img_blocks(img, n_blocks=(2, 2))

# Create a plot to show the blocks
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Display each block
for i in range(2):
    for j in range(2):
        axes[i, j].imshow(blocks[i][j])
        axes[i, j].axis('off')  # Hide axis

plt.tight_layout()
plt.show()
