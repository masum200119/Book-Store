import cv2
import numpy as np
import matplotlib.pyplot as plt

def divide_img_blocks(img, n_blocks=(2, 2)):
    
    horizontal_blocks = np.array_split(img, n_blocks[0], axis=0)
    
    splitted_img = [np.array_split(block, n_blocks[1], axis=1) for block in horizontal_blocks]
    
    return splitted_img  


img = cv2.imread('image.jpg')


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


blocks = divide_img_blocks(img, n_blocks=(2, 2))


# fig, axes = plt.subplots(1, 1, figsize=(10, 10))


# for i in range(2):
#     for j in range(2):
        
#         # axes[i, j].imshow(blocks[i][j])
#         axes[i, j].axis('off')  # Hide axis

img1 = blocks[0][1]
img0 = blocks[0][0]
plt.imshow(img1)
plt.show()
plt.imshow(img0)
plt.tight_layout()
plt.show()
