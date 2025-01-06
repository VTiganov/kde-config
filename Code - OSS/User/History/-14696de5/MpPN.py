import numpy as np
from PIL import Image

# Load the image
image_path = 'raw.png'
image = Image.open(image_path)
image = image.convert('RGBA')  # Convert to RGBA to handle transparency
image_array = np.array(image)

# Define the background color (e.g., white background)
background_color = np.array([255, 255, 255, 255])  # RGBA for white

# Create a mask where the background color is present
# Ensure the mask has the correct shape
mask = np.all(image_array == background_color, axis=-1)

# Check the shapes to ensure they match
print(f"Image array shape: {image_array.shape}")
print(f"Mask shape: {mask.shape}")

# Set the background pixels to transparent
image_array[mask] = [0, 0, 0, 0]  # RGBA for transparent

# Convert the array back to an image
transparent_image = Image.fromarray(image_array, 'RGBA')

# Save or display the image
transparent_image.save('path_to_save_transparent_image.png')
transparent_image.show()
