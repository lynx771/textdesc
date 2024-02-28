from django.shortcuts import render
from django.http import HttpResponse
import cv2
import pytesseract
import tempfile
import os


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):

    img = cv2.imread(image_path)
    if img is None:
        return "Error: Unable to open image."

    
    img = cv2.resize(img, None, fx=0.5, fy=0.5)
   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    adpt_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)

    text = pytesseract.image_to_string(adpt_threshold)

    return text

def home(request):
    extracted_text = None
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(image.read())
            temp_file_path = temp_file.name

        extracted_text = extract_text_from_image(temp_file_path)
        os.unlink(temp_file_path)  
    return render(request, 'home.html', {'extracted_text': extracted_text})