from PIL import Image # Для загрузки и открытия изображений
import numpy as np


image_path = 'raw.png' # Загрузка изображения  
image = Image.open(image_path)
image = image.convert('RGBA')  # В РГБА для более удобной работы с прозрачностью.

image_array = np.array(image) # Переводим картинку в нумпай список.

# Определяю цвета фона, которые будем убирать. Пришлось взять несколько образцов вокруг каждой кошки, чтобы точно все удалилось (цвета не однородные)
background_colors = [
    np.array([242, 209, 97, 255]), # First cat
    np.array([235, 197, 68, 255]),
    np.array([229, 185, 50, 255]),
    np.array([225, 174, 21, 255]), # Third cat
    np.array([214, 164, 6.9, 255]),
    np.array([216, 160, 36.975, 255]), # Second cat
    np.array([185, 138, 4.08, 255]),
    np.array([169, 124, 0, 255]),
    np.array([214, 113.985, 0, 255]), # Fourth cat
    np.array([199.92, 104.04, 2.04, 255]),
    np.array([183.09, 85.935, 0, 255])
]

tolerance = 15  # Допустимое отклонение по цвету, т.к. он не идеально одинаковый на всем фоне

cat_masks = [  # Дополнительно пришлось создать маску для мордочки каждой кошки, потому что похожие цвета все время пытаюстся удалиться.
    (127,135,373,504),   # Создается по координатам: (x1, y1, x2, y2)
    (111,676,364,864),  # От верхнего левого угла до правого нижнего угла.
    (671,654,874,814)
    
]
# Для каждого из цветов фона создаем маску.
mask = np.zeros(image_array.shape[:2], dtype=bool)  
for bg_color in background_colors:
    diff = np.abs(image_array - bg_color)
    mask |= np.all(diff <= tolerance, axis=-1)  

for x1, y1, x2, y2 in cat_masks:
    mask[y1:y2, x1:x2] = False

image_array[mask] = [255, 255, 255, 255]  # Сделал фон белым. С помощью маски из всех нулей можно сделать полностью прозрачный.

# Convert the modified array back to an image
transparent_image = Image.fromarray(image_array, 'RGBA')

# Сохранил картинку
output_path = 'enhanced.png' 
transparent_image.save(output_path)