pip install qrcode[pil]

import qrcode

def generate_qr_code(url, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Version of the QR code, 1 to 40 (controls size)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border size (minimum is 4)
    )

    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage
url = "https://www.linkedin.com/in/sumanthkrishna/"
filename = "FollowSumanthOnLinkedIn.png"
generate_qr_code(url, filename)
