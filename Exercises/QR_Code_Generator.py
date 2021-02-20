#QR Code Generator
import qrcode

qr =  qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=20,
                    border=2)

qr.add_data("https://www.google.com/")
qr.make(fit=True)

image = qr.make_image(fill_color="black",back_color="white")
image.save("qrimg.png")