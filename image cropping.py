import os
from PIL import Image

# crooping size
width = input('Enter Cropping width : ')
height = input('Enter Cropping height : ')


# open folder
os.chdir('images')


# putput folder
output_folder = input('Enter Folder Name : ')
os.makedirs(output_folder, exist_ok=True)


# loob over each image
for image in os.listdir('.'):
    if image.endswith(('.png','.jpg','.jpeg')):
        im = image.open(image)
        im1 = im.crop((0, 0, width, height))
        im1.save(f"{output_folder}/{image}")



