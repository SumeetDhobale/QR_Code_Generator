import qrcode
from PIL import Image #pip install qrcode[pil]

qr=qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10, border=10,) #customize qr code
qr.add_data("https://github.com/SumeetDhobale")
qr.make(fit=True) #make qr code

img=qr.make_image(fill_color="red", back_color="yellow")
img.save("GitHub.png")