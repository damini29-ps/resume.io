import qrcode

def generate_qr_code(url, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="white")

    # Save the image to a file
    img.save(file_name)

if __name__ == "__main__":
    link = "https://www.behance.net/daminisharma2905"  # Replace this with your desired link
    qr_file_name = "qr_code.png"  # The filename for the generated QR code image

    generate_qr_code(link, qr_file_name)
    print(f"QR code for {link} generated and saved to {qr_file_name}")
