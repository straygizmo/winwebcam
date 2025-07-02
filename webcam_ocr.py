import cv2
import pytesseract
from PIL import Image
import numpy as np
import datetime
import os

def capture_and_ocr():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    
    print("Press Enter to capture image and perform OCR")
    print("Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to capture frame")
            break
        
        cv2.imshow('Webcam - Press Enter to capture', frame)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == 13:  # Enter key
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"capture_{timestamp}.png"
            
            cv2.imwrite(filename, frame)
            print(f"\nImage saved as {filename}")
            
            # Convert BGR to RGB for OCR
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(rgb_frame)
            
            # Perform OCR
            print("Performing OCR...")
            try:
                text = pytesseract.image_to_string(pil_image, lang='eng+jpn')
                
                if text.strip():
                    print("\n--- OCR Result ---")
                    print(text)
                    print("--- End of OCR ---\n")
                    
                    # Save OCR result to text file
                    text_filename = f"ocr_result_{timestamp}.txt"
                    with open(text_filename, 'w', encoding='utf-8') as f:
                        f.write(text)
                    print(f"OCR result saved to {text_filename}")
                else:
                    print("No text detected in the image")
                    
            except Exception as e:
                print(f"OCR Error: {e}")
            
            print("\nPress Enter to capture another image or 'q' to quit")
            
        elif key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Check if Tesseract is installed and configured
    try:
        # For Windows, you might need to specify the path to tesseract.exe
        # Uncomment and modify the following line if needed:
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        capture_and_ocr()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have installed:")
        print("1. Tesseract-OCR (https://github.com/UB-Mannheim/tesseract/wiki)")
        print("2. Required Python packages: pip install -r requirements.txt")