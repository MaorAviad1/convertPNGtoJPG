from PIL import Image
import os

# Set the folder containing the PNG images
png_folder = "C:/Users/Dana/PycharmProjects/convertPNGtoJPG"

# Set the folder where you want the JPG images to be saved
jpg_folder = "C:/Users/Dana/PycharmProjects/convertPNGtoJPG/newjpg"

# Loop through each file in the PNG folder
for file_name in os.listdir(png_folder):
    if file_name.endswith(".png"):
        # Set the file paths for the input PNG and output JPG files
        png_file_path = os.path.join(png_folder, file_name)
        jpg_file_path = os.path.join(jpg_folder, file_name.replace(".png", ".jpg"))

        # Open the PNG image using Pillow's Image class and save it as a JPG
        with Image.open(png_file_path) as im:
            im.convert("RGB").save(jpg_file_path)
