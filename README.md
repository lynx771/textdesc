Text Extraction Web App
This is a web application built with Django that allows users to upload an image and extract text from it using Optical Character Recognition (OCR) technology.

Features
Upload Image: Users can upload an image file from their device.
Extract Text: The uploaded image is processed to extract text using the Tesseract OCR library.
Display Result: The extracted text is displayed to the user.

Installation
1.Clone the repository:
  git clone <repository-url>

2.Install dependencies:
  pip install -r requirements.txt

3.Set up Tesseract OCR:
  Install Tesseract OCR
  Set the Tesseract executable path in settings.py:
  pytesseract.pytesseract.tesseract_cmd = '/path/to/tesseract'

4.Run migrations:
  python manage.py migrate

5.Run the development server:
  python manage.py runserver

Access the application at http://localhost:8000.

Usage
Navigate to the homepage.
Click on the "Upload Image" button and select an image file from your device.
Click on the "Extract Text" button to process the uploaded image and display the extracted text.
The extracted text will be displayed on the same page.

Technologies Used
Django
Tesseract OCR
HTML
CSS
