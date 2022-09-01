import datetime
import os
from os.path import splitext
from pathlib import Path
import shutil

from PIL import Image, ImageOps, ImageFile
import filetype

ImageFile.LOAD_TRUNCATED_IMAGES = True

# base_dir = Path(__file__).parent # for test running in the console
base_dir = Path(__file__).parent.parent  # for running executable file
print(base_dir)
input_path = base_dir / '处理前'  
out_path = base_dir / '处理后'
print('复制文件中，请耐心等待...\n')
try:
    shutil.copytree(input_path, out_path)
except:
    pass
print('复制文件结束！\n')
logo_path = base_dir / 'logo.png'

def rename(input_path):
    for root, _, files in os.walk(input_path):
        counter = 1
        for filename in files:
            _, extension = splitext(filename)
            f = os.path.join(root, filename)
            if os.path.isfile(f) and filetype.is_image(f):
                new_name = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S-%f') + '-' + str(counter) + extension
                os.replace(f, os.path.join(root, new_name))
                counter += 1

def resize(input_path):
    for root, _, files in os.walk(input_path):
        for filename in files:
            f = os.path.join(root, filename)
            if os.path.isfile(f) and filetype.is_image(f):
                im = Image.open(f)
                im = ImageOps.contain(im, (1000, 1000))

                copied_image = im.copy()
                copied_image.save(os.path.join(root, filename))

def resize_watermark(input_path):
    logo = Image.open(logo_path)
    # resize the logo
    lwidth, lheight = logo.size
    logo = logo.resize((int(lwidth*2), int(lheight*2)))
    width_of_watermark , height_of_watermark = logo.size

    for root, _, files in os.walk(input_path):
        for filename in files:
            f = os.path.join(root, filename)
            if os.path.isfile(f) and filetype.is_image(f):
                im = Image.open(f)
                im = ImageOps.contain(im, (1000, 1000))
                width, height = im.size

                position = (int((width/2-width_of_watermark/2)),int((height/2-height_of_watermark/2)))

                copied_image = im.copy()
                copied_image.paste(logo.copy(), position, logo)
                copied_image.save(os.path.join(root, filename))


choice = input('请选择操作：1.重命名 2.压缩 3.压缩+水印 4.退出 5.清除"处理后"文件夹(重置)\n\n')

if choice == '1':
    print('照片批量重命名中，请耐心等待...\n')
    rename(out_path)
    print('重命名结束！请打开"处理后"文件夹查看结果！\n')
elif choice == '2':
    print('照片批量压缩中，请耐心等待...')
    resize(out_path)
    print('压缩结束！请打开"处理后"文件夹查看结果！\n')
elif choice == '3':
    print('照片批量压缩+水印中，请耐心等待...\n')
    resize_watermark(out_path)
    print('压缩+水印结束！请打开"处理后"文件夹查看结果！\n')
elif choice == '4':
    print('已退出\n')
elif choice == '5':
    try:
        shutil.rmtree(out_path)
    except FileNotFoundError:
        pass
    print('已清除"处理后"文件夹\n')


input('确定退出？点击Enter退出...')





