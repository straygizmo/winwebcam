import cv2
import pytesseract
from PIL import Image
import numpy as np
import datetime
import os

# Set Tesseract path for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_and_ocr():
    # Try different camera indices
    camera_found = False
    cap = None
    working_camera_index = None
    
    for camera_index in range(5):  # Try camera indices 0-4
        print(f"Trying camera index {camera_index}...")
        
        # Try default backend first
        cap = cv2.VideoCapture(camera_index)
        
        if cap.isOpened():
            # Test if we can actually read a frame
            ret, frame = cap.read()
            if ret and frame is not None:
                print(f"Successfully opened camera at index {camera_index}")
                camera_found = True
                working_camera_index = camera_index
                break
            else:
                cap.release()
        
        # If default backend failed, try DirectShow backend (Windows specific)
        if not camera_found:
            cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
            if cap.isOpened():
                ret, frame = cap.read()
                if ret and frame is not None:
                    print(f"Successfully opened camera at index {camera_index} using DirectShow")
                    camera_found = True
                    working_camera_index = camera_index
                    break
                else:
                    cap.release()
    
    if not camera_found:
        print("Error: Could not open any webcam")
        print("Please check:")
        print("1. Is a webcam connected to your computer?")
        print("2. Is the webcam being used by another application?")
        print("3. Do you have permission to access the camera?")
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
    print("Starting webcam OCR application...")
    try:
        capture_and_ocr()
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()
