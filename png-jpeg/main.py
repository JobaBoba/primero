from PIL import Image
import os

input_folder = "/path/to/png/folder/"
output_folder = "/path/to/jpg/folder/"

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        png_file_path = os.path.join(input_folder, filename)
        image = Image.open(png_file_path)
        jpg_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        image.convert('RGB').save(jpg_file_path)
