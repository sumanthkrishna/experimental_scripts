# To scrape text from image files in a folder and write them into a text file, you can use the Tesseract OCR (Optical Character Recognition) library in Python. 

# First, ensure you have Tesseract installed on your system. You can install it using the following commands:

# Linux - 
# sudo apt-get update 
# sudo apt-get install tesseract-ocr

# MacOS - 
# brew install tesseract

# Windows - 
# For Windows, download and install from: https://github.com/UB-Mannheim/tesseract/wiki

import os
import pytesseract
from PIL import Image

# Path to the folder containing image files
folder_path = 'puzzles'

# Output text file path
output_file = 'output.txt'

# Initialize pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # Update this path if necessary OR UPDATE THE PATH VARIABLE

# Open or create a text file for writing
with open(output_file, 'w') as f:
    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Read the image file
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            
            # Perform OCR to extract text from the image
            text = pytesseract.image_to_string(image)
            
            # Write the extracted text to the text file
            f.write(f"File: {filename}\n")
            f.write(text + '\n\n')

print("Text extracted from image files and written to output.txt")
