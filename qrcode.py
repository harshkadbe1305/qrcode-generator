import qrcode 
import image                        
qr =qrcode.QRCode(
    version=15,#complication of qrcode
    box_size=10,#size of the box of the qrcode
    border=5,#white part of the image
)
data="https://www.youtube.com/watch?v=o-uWRhi2ngE"
qr.add_data(data)
qr.make(fit = True)
img=qr.make_image(fill="black",back_colour="white")
img.save("test.png")