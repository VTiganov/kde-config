from PIL import Image
import numpy as np

# Load the image
image_path = 'raw.png'  # Replace with the path to your image
image = Image.open(image_path)
image = image.convert('RGBA')  # Convert to RGBA to handle transparency

# Convert the image to a NumPy array
image_array = np.array(image)

# Define the background color (e.g., yellow in RGBA format)
background_color = [255, 255, 0, 255]  # Replace with the color to remove (e.g., yellow)

# Create a mask where the background color matches
mask = np.all(image_array[:, :, :4] == background_color, axis=-1)

# Set the matching pixels to transparent
image_array[mask] = [0, 0, 0, 0]  # RGBA for fully transparent

# Convert the modified array back to an image
transparent_image = Image.fromarray(image_array, 'RGBA')

# Save or display the image
output_path = 'transparent_image.png'  # Specify the output path
transparent_image.save(output_path)
print(f"Image saved at: {output_path}")
