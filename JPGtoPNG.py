#JPG to PNG converter
#usage JPGtoPNG.py source_directory target_directory
#Version 1.0


import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f'Directory "{output_folder}" created.')

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'{output_folder}{clean_name[0]}.png', 'png')
    print(f'{filename} converted.')