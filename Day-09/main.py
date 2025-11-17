# Day-09/main.py
# pip install qrcode[pil]   ← Pehle terminal mein ye daal

import qrcode

print("QR CODE GENERATOR")
text = input("Kya likhna hai QR mein? (YouTube link, WiFi, text): ")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(text)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr.png")

print("QR Code ban gaya → my_qr.png file check kar!") 