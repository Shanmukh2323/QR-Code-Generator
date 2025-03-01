import qrcode  

# UPI Payment URL
upi_url = 'upi://pay?pa=imshanmukh@ybl&pn=SAHUKARI%20JYOTHI&tn=tq'

# Generating QR code
img = qrcode.make(upi_url)
img.save("payment_qr.png")
img.show()

print("QR code generated successfully!")
