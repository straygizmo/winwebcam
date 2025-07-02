"""
Command-line interface for winwebcam package.
"""

import pytesseract
from .webcam_ocr import capture_and_ocr


def main():
    """Main entry point for the command-line interface."""
    try:
        # For Windows, you might need to specify the path to tesseract.exe
        # Uncomment and modify the following line if needed:
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        capture_and_ocr()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have installed:")
        print("1. Tesseract-OCR (https://github.com/UB-Mannheim/tesseract/wiki)")
        print("2. Required Python packages: pip install opencv-python pytesseract Pillow numpy")


if __name__ == "__main__":
    main()
