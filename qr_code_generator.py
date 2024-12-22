import qrcode

def generate_qr_code(text, file_path="QRCode.png"):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # controls how many pixels each box in the QR code is
        border=4,  # controls the border (minimum is 4)
    )

    # Add data to the QR code
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill="black", back_color="white")
    img.save(file_path)
    print(f"QR code saved as {file_path}")

# Prompt user for input
text = input("Enter text to encode in QR Code: ")
generate_qr_code(text)
