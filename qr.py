import qrcode

website_link = "https://campusfest.in"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(website_link)
qr.make(fit=True)

# Ippo black color patterns and white background kidaikum
img = qr.make_image(fill_color="black", back_color="white")

img.save("campusfest_standard_qr.png")

print("Black & White QR Code success-ah generate aayiruchu!")