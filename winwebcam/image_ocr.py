import pytesseract
from PIL import Image
import os
import sys

def ocr_from_file(image_path):
    """Perform OCR on an image file."""
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found")
        return
    
    try:
        # Open and process the image
        image = Image.open(image_path)
        print(f"Processing image: {image_path}")
        print(f"Image size: {image.size}")
        print(f"Image mode: {image.mode}")
        
        # Perform OCR
        print("Performing OCR...")
        text = pytesseract.image_to_string(image, lang='eng+jpn')
        
        if text.strip():
            print("\n--- OCR Result ---")
            print(text)
            print("--- End of OCR ---\n")
            
            # Save OCR result to text file
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            text_filename = f"ocr_result_{base_name}.txt"
            with open(text_filename, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"OCR result saved to {text_filename}")
        else:
            print("No text detected in the image")
            
    except Exception as e:
        print(f"Error processing image: {e}")

def main():
    """Main entry point for image OCR."""
    if len(sys.argv) != 2:
        print("Usage: python image_ocr.py <image_path>")
        print("Example: python image_ocr.py screenshot.png")
        return
    
    image_path = sys.argv[1]
    ocr_from_file(image_path)

if __name__ == "__main__":
    main()
