import cv2
import pytesseract
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('sample_image.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Extract text using Pytesseract
extracted_text = pytesseract.image_to_string(gray)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)


