from PIL import Image, ImageOps
import os
from pathlib import Path

# base_dir = os.getcwd()  # for running in the console
base_dir = os.path.dirname(os.getcwd()) # for running executable file
input_path = base_dir + '\inputs'
out_path = base_dir + '\outputs'
logo = base_dir + '\logo.png'


logo = Image.open(logo)
# logo = Image.open("C:\\Users\\pengliangyu\\Desktop\\utils\\watermark\\logo.png")

# resize the logo
lwidth, lheight = logo.size
logo = logo.resize((int(lwidth*2), int(lheight*2)))
width_of_watermark , height_of_watermark = logo.size

for filename in os.listdir(input_path):
    f = os.path.join(input_path, filename)
    if os.path.isfile(f):
        im = Image.open(f)
        if im.width > 1000 or im.height > 1000:
            im = ImageOps.contain(im, (1000, 1000))
        width, height = im.size

        position = (int((width/2-width_of_watermark/2)),int((height/2-height_of_watermark/2)))

        copied_image = im.copy()
        copied_image.paste(logo.copy(), position, logo)
        copied_image.save(os.path.join(out_path, filename))

print('everything is ok') 

