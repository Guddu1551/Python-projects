import qrcode
import datetime

def qr_generator(text):
        qr = qrcode.QRCode(
              version =1,
              error_correction = qrcode.constants.ERROR_CORRECT_L,
              box_size = 10,
              border = 4,
        )
        
        now = datetime.datetime.now()
        date_time = now.strftime("%d-%m-%Y_%H-%M")
        
        qr.add_data(text)
        qr.make(fit = True)
        img = qr.make_image(fill_color = "black", back_color = "white")
        img.save(f"qr_code_{date_time}.png")
        
print("Please enter the link to generate QR code for: ")
link = input()
qr_generator(link)
