# experimental_scripts
 List of scripts to experiment
 
One challenge a day! 
The idea is to take up a random challenge and provide the solution in the favorite lanugage. Feel free to create the script(s) as required per your favorite language (Ruby, Python, R...) and submit for reviews

BE RESPECTFUL WITH SOLUTIONS AND LEVERAGE THE LEARNING PROCESS 
 
01/05/2023 
Grab a stock price - Script to show price of any stock. This challenge explains ability to connect remote api and display the price. 

11/9/2023
Automation script to download a report! 
https://github.com/sumanthkrishna/experimental_scripts/blob/main/automate-report-download-script-java.java

# Contract testing steps

# Git Cleanup bash/python scripts

# QR Code Generator 5/29/2024
### Explanation
1. Import the necessary library: qrcode for generating the QR code.
2. Create a QR code instance: Configure the QR code with specific parameters like version, error correction level, box size, and border.
3. Add data to the QR code: Use the add_data method to add the URL.
4. Generate the QR code: Call make with fit=True to generate the QR code with the provided data.
5. Create an image: Use make_image to create an image of the QR code.
6. Save the image: Save the generated QR code image to a file with the specified filename.

### Running the Snippet
1. Copy the above code into a Python script file, for example, generate_qr_code.py.
2. Run the script using Python python generate_qr_code.py



# QR Code Generator with logo in the middle 5/29/2024

### Explanation
Create a QR Code Instance:

1. qrcode.QRCode is used to create a QR code instance with specified parameters.
2. version=1: Controls the size of the QR code. You can increase the version for larger QR codes.
3. error_correction=qrcode.constants.ERROR_CORRECT_H: High error correction allows for better logo integration by allowing more parts of the QR code to be covered.
4. box_size=10: Size of each box in the QR code.
5. border=4: Border size.

### Add Data:

qr.add_data(url): Adds the URL data to the QR code.
qr.make(fit=True): Generates the QR code.
Generate QR Code Image:

qr.make_image(fill='black', back_color='white'): Creates an image of the QR code with black fill and white background.
Load and Resize Logo:

Image.open(logo_path): Opens the logo image.
logo.resize((logo_size, logo_size), Image.ANTIALIAS): Resizes the logo to fit within the QR code.
Center Logo on QR Code:

Calculates the position to center the logo on the QR code.
qr_img.paste(logo, logo_pos, mask=logo): Pastes the logo onto the QR code image. The mask=logo parameter ensures that the logo is correctly overlaid with transparency preserved.
Save the Final Image:

qr_img.save(output_path): Saves the final QR code image with the logo.
