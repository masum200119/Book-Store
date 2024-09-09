from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "butterfly.jpg"  # Replace with the path to your image
image = Image.open(image_path)

# Convert the image to a numpy array
image_array = np.array(image)

# Split the image into R, G, B channels
r, g, b = image_array[:, :, 0], image_array[:, :, 1], image_array[:, :, 2]

# Manually calculate the histogram for each channel
def calculate_histogram(channel):
    histogram = np.zeros(256)  # There are 256 possible intensity values
    for value in channel.ravel():
        histogram[value] += 1
    return histogram

r_hist = calculate_histogram(r)
g_hist = calculate_histogram(g)
b_hist = calculate_histogram(b)

# Plot the histograms using the plot function
plt.figure(figsize=(12, 6))

# Red channel
plt.subplot(1, 3, 1)
plt.plot(r_hist, color='red')
plt.title('Red Channel Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Green channel
plt.subplot(1, 3, 2)
plt.plot(g_hist, color='green')
plt.title('Green Channel Histogram')
plt.xlabel('Pixel Intensity')

# Blue channel
plt.subplot(1, 3, 3)
plt.plot(b_hist, color='blue')
plt.title('Blue Channel Histogram')
plt.xlabel('Pixel Intensity')

plt.tight_layout()
plt.show()
