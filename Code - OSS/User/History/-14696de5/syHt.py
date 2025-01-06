import numpy as np
from PIL import Image

image_path = 'raw.png'
image = Image.open(image_path)
image = image.convert('RGBA')
image_array = np.array(image)

background_color = np.array([255, 255, 255, 255])

mask = np.all(image_array == background_color, axis=1)

image_array[mask] = [0,0,0,0]

transparent_image = Image.fromarray(image_array, 'RGBA')

transparent_image.save('after.png')