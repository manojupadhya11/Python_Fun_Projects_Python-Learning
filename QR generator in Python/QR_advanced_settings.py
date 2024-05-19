#Advanced settings width, border color background color change etc.
import qrcode 
from PIL import Image
import qrcode.constants

qr  = qrcode.QRCode(version=1,
                             error_correction = qrcode.constants.ERROR_CORRECT_H,
                             box_size = 10,border = 4,)



qr.add_data("https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ")

qr.make(fit=True)
img2 = qr.make_image(fill_color ="black", back_color = "blue")

img2.save("Designed_QR.png")