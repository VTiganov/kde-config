from PIL import Image
import numpy as np

# Load the image
image_path = 'raw.png'  # Replace with your image path
image = Image.open(image_path)
image = image.convert('RGBA')  # Convert to RGBA to handle transparency

# Convert the image to a NumPy array
image_array = np.array(image)

# Define the background colors (add more colors as needed)
background_colors = [
    np.array([242, 209, 97, 255]),
    np.array([235, 197, 68, 255]),
    np.array([229, 185, 50, 255]),
    np.array([225, 174, 21, 255]),
    np.array([214, 164, 6.9, 255]),
    np.array([216, 160, 36.975, 255])
]

tolerance = 15  # Adjust this value as needed

# Create a mask for all specified colors
mask = np.zeros(image_array.shape[:2], dtype=bool)  # Initialize mask
for bg_color in background_colors:
    diff = np.abs(image_array - bg_color)
    mask |= np.all(diff <= tolerance, axis=-1)  # Update mask for each color

# Set the matching pixels to transparent
image_array[mask] = [0, 0, 0, 0]  # RGBA for fully transparent

# Convert the modified array back to an image
transparent_image = Image.fromarray(image_array, 'RGBA')

# Save the output
output_path = 'transparent_image.png'  # Specify the output path
transparent_image.save(output_path)
print(f"Transparent image saved at: {output_path}")
