from PIL import Image
import numpy as np

# Load the image
image_path = 'raw.png'  # Replace with your image path
image = Image.open(image_path)
image = image.convert('RGBA')  # Convert to RGBA to handle transparency

# Convert the image to a NumPy array
image_array = np.array(image)

# Define the background color and tolerance
background_color = np.array([255, 255, 0, 255])  # Replace with your background color
tolerance = 60  # Adjust this value as needed

# Create a mask where the pixel color is within the tolerance of the background color
diff = np.abs(image_array - background_color)
mask = np.all(diff <= tolerance, axis=-1)

# Set the matching pixels to transparent
image_array[mask] = [0, 0, 0, 0]  # RGBA for fully transparent

# Convert the modified array back to an image
transparent_image = Image.fromarray(image_array, 'RGBA')

# Save the output
output_path = 'transparent_image.png'  # Specify the output path
transparent_image.save(output_path)
print(f"Transparent image saved at: {output_path}")
