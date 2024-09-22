import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import Counter

# Step 1: Load the image and convert it to grayscale
def load_image(image_path):
    image = Image.open(image_path).convert('L')  # Convert to grayscale ('L' mode)
    return np.array(image)

# Step 2: Create a function to calculate probabilities and plot the histogram
def plot_histogram(image_array):
    # Flatten the 2D array
    flattened_image = image_array.flatten()
    
    # Count pixel intensities
    pixel_counts = Counter(flattened_image)
    
    # Total number of pixels
    total_pixels = flattened_image.size
    
    # Calculate probabilities
    pixel_probabilities = {intensity: count / total_pixels for intensity, count in pixel_counts.items()}
    
    # Prepare data for plotting
    intensities = list(pixel_probabilities.keys())
    probabilities = list(pixel_probabilities.values())
    
    # Plot the histogram
    plt.bar(intensities, probabilities, width=1, align='center', color='gray')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Probability')
    plt.title('Histogram of Pixel Intensity Probabilities')
    plt.show()

# Step 3: Main function to load an image, convert it, and plot the histogram
def main(image_path):
    # Load image and convert to 2D array
    image_array = load_image(image_path)
    
    # Plot histogram
    plot_histogram(image_array)

# Example usage:
image_path = 'Abdulla.jpg'  # Replace with the path to your image
main(image_path)
