import os
import io
from PIL import Image
import cairosvg
from PIL import UnidentifiedImageError  # Import the specific exception


def find_max_size(root_directory):
    max_width, max_height = 0, 0
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            try:
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    with Image.open(os.path.join(dirpath, filename)) as img:
                        width, height = img.size
                        max_width, max_height = max(max_width, width), max(max_height, height)
                elif filename.lower().endswith('.svg'):
                    svg_path = os.path.join(dirpath, filename)
                    png_data = cairosvg.svg2png(url=svg_path)
                    with Image.open(io.BytesIO(png_data)) as img:
                        width, height = img.size
                        max_width, max_height = max(max_width, width), max(max_height, height)
            except UnidentifiedImageError:
                print(f"Cannot identify image file: {os.path.join(dirpath, filename)}")
                continue
    return max_width, max_height

def make_canvas_size(max_width, max_height):
    canvas_width = ((max_width - 1) // 32 + 1) * 32
    canvas_height = ((max_height - 1) // 32 + 1) * 32
    return canvas_width, canvas_height

def center_image_on_canvas(image, canvas_size):
    canvas = Image.new('RGB', canvas_size, 'hotpink')
    x = (canvas_size[0] - image.size[0]) // 2
    y = (canvas_size[1] - image.size[1]) // 2
    canvas.paste(image, (x, y))
    return canvas

root_directory = '/Users/m041946/Documents/2024-1-Winter/AIHC-5010/final_project/data/ACL-fig/training_data/train'
save_directory = '/Users/m041946/Documents/2024-1-Winter/AIHC-5010/final_project/data/ACL-fig/training_data/train_resized'

max_width, max_height = find_max_size(root_directory)
canvas_size = make_canvas_size(max_width, max_height)

for dirpath, dirnames, filenames in os.walk(root_directory):
    for dirname in dirnames:
        new_dir_path = os.path.join(save_directory, os.path.relpath(os.path.join(dirpath, dirname), root_directory))
        os.makedirs(new_dir_path, exist_ok=True)
    
    for filename in filenames:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.svg')):
            filepath = os.path.join(dirpath, filename)
            if filename.lower().endswith('.svg'):
                png_data = cairosvg.svg2png(url=filepath)
                image = Image.open(io.BytesIO(png_data))
            else:
                image = Image.open(filepath)
            canvas = center_image_on_canvas(image, canvas_size)
            save_path = os.path.join(save_directory, os.path.relpath(dirpath, root_directory), filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            canvas.save(save_path)
