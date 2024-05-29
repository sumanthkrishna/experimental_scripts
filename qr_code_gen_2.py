pip install qrcode[pil] pillow


import qrcode
from PIL import Image

def generate_qr_code_with_logo(url, logo_path, output_path):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # You can adjust the version to control the size
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for better logo integration
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code instance
    qr_img = qr.make_image(fill='black', back_color='white')

    # Load the logo image
    logo = Image.open(logo_path)

    # Calculate the logo size and position
    qr_width, qr_height = qr_img.size
    logo_size = qr_width // 4  # Adjust the size of the logo relative to the QR code
    logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

    # Calculate the position to place the logo at the center of the QR code
    logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # Paste the logo onto the QR code
    qr_img.paste(logo, logo_pos, mask=logo)

    # Save the final image
    qr_img.save(output_path)
    print(f"QR code with logo saved as {output_path}")

# Example usage
url = "https://www.linkedin.com/in/sumanthkrishna/"
logo_path = "https://images.rawpixel.com/image_png_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvdjk4Mi1kMy0xMC5wbmc.png"
output_path = "qr_code_with_logo.png"
generate_qr_code_with_logo(url, logo_path, output_path)
