import qrcode

data = input("Enter text or URL: ")

qr = qrcode.make(data)

qr.save("my_qr.png")

print("QR Code generated successfully!")
print("Saved as: my_qr.png")