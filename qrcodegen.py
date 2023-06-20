import qrcode

def generate_qrcode(url, output_file):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

# Example usage:
website_url = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
output_file_path = "qrcode.png"

generate_qrcode(website_url, output_file_path)
print("QR code generated and saved as:", output_file_path)
