# pip install pillow qrcode
import qrcode

# Link for website
# input_data = "http://192.168.0.19:8000/live/searchmatch/人民路3188号1幢/"
# input_data = '王**\n地铁1号线东段\nG0010202181'
input_data = '轨道交通1号线东段'

pk = 1
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save(f'{pk}.png')

