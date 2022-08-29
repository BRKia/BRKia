import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5
)
qr.add_data('https://jwc.hqu.edu.cn/')
qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
img.show()
img.save('qr_figure.png')
