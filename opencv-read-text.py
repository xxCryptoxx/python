from typing import Text
import cv2
import pytesseract

# input -> process -> output

# load image
img = cv2.imread('bitcoin.jpeg')

# extract text from image
text = pytesseract.image_to_string(img)

#display extracted text
print(text)