import numpy as np
import matplotlib.pyplot as plt
import os

# Function to process an image: read 16-bit grayscale, map to 8-bit, and normalize
def process_image_with_dimensions(file_path, width, height):
    # Read the image data
    image_data = np.fromfile(file_path, dtype=np.uint16)

    # Reshape based on the provided dimensions
    image_data = image_data.reshape((height, width))

    # Normalize to 0-255 range
    min_val = np.min(image_data)
    max_val = np.max(image_data)
    image_8bit = ((image_data - min_val) / (max_val - min_val) * 255).astype(np.uint8)

    return image_8bit

# Function to save processed images with original file names
def save_processed_images(file_paths, width, height):
    for file_path in file_paths:
        # Process the image
        processed_image = process_image_with_dimensions(file_path, width, height)

        # Extract the base file name and construct the new file name
        base_file_name = os.path.basename(file_path)
        new_file_name = base_file_name.replace('.raw', '_processed.png')

        # Construct the full path for saving the file
        output_file_path = f'{new_file_name}'

        # Save the processed image
        plt.imsave(output_file_path, processed_image, cmap='gray')

# Provided dimensions for the images
width, height = 2592, 1944

# Paths to the image files
file_paths = [
    '纯净水690.raw',
    '纯净水宽.raw',
    '磷酸钠宽.raw',
    '磷酸钠690.raw',
    '注射690.raw',
    '注射宽波段.raw',
    '注射宽波段1.raw',
    '注射宽波段2.raw'
]

# Process and save the images
save_processed_images(file_paths, width, height)
