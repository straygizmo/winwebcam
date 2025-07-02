# Webcam OCR

A Python application that captures webcam images and performs OCR (Optical Character Recognition) on them. Press Enter to capture an image from your webcam and extract text using Tesseract OCR.

## Environment Setup

### Prerequisites

1. **Install uv** (if not already installed):
```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. **Install Python dependencies**:
```bash
uv pip install -e .
```

3. **Install Tesseract OCR**:

   **Windows (Recommended method):**
   ```bash
   winget install UB-Mannheim.TesseractOCR
   ```
   
   **Alternative Windows method:**
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Install manually and add to PATH
   
   **Note:** The application automatically configures the Tesseract path for Windows installations.

4. **For Japanese OCR support**:
   - Japanese language data is included with the standard Tesseract installation
   - The application supports both English and Japanese text recognition (`lang='eng+jpn'`)

## Usage

### Webcam OCR

```bash
uv run python .\winwebcam\webcam_ocr.py
```

**Controls:**
- **Enter**: Capture image and perform OCR
- **q**: Quit application

The application will:
- Open your webcam and display a live video feed
- Save captured images with timestamps (e.g., `capture_20250702_152608.png`)
- Save OCR results to text files (e.g., `ocr_result_20250702_152608.txt`)
- Display extracted text in the console

### Image File OCR

For processing existing image files or when webcam is not available:

```bash
uv run python .\winwebcam\image_ocr.py <image_file_path>
```

Example:
```bash
uv run python .\winwebcam\image_ocr.py screenshot.png
```

## Troubleshooting

### "Could not open any webcam" Error

This error can occur due to several reasons:

1. **No webcam connected**
   - Ensure USB camera is properly connected
   - Check if built-in camera is enabled in Device Manager

2. **Camera in use by another application**
   - Close video calling apps (Zoom, Teams, Skype, etc.)
   - Stop camera access in web browsers
   - Check Windows Camera app

3. **Camera access permissions**
   - Go to Windows Settings > Privacy & Security > Camera
   - Enable "Camera access" and "Let apps access your camera"
   - Ensure desktop apps can access camera

4. **Camera driver issues**
   - Update camera drivers through Device Manager
   - Restart computer if camera was recently connected

### Camera Diagnostic Tool

If you're experiencing camera issues, run the diagnostic tool:

```bash
uv run python camera_diagnostic.py
```

This tool will:
- Test different camera backends (default and DirectShow)
- List available camera devices
- Provide detailed troubleshooting information

### Tesseract OCR Issues

If OCR fails with "tesseract is not installed" error:

1. **Verify Tesseract installation**:
   ```bash
   tesseract --version
   ```

2. **Manual path configuration** (if needed):
   Edit `winwebcam/webcam_ocr.py` and update the Tesseract path:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

### Alternative: Use Image File OCR

If webcam issues persist, you can still use OCR functionality:
1. Take a screenshot using Windows Snipping Tool
2. Save the image file
3. Process it using `image_ocr.py`

## Package Installation

To install as a package and use from command line:

```bash
# Install package
uv pip install -e .

# Run from command line
winwebcam
```

## Features

- **Multi-language OCR**: Supports English and Japanese text recognition
- **Real-time webcam preview**: Live video feed before capture
- **Automatic file saving**: Timestamped image and text file output
- **Cross-platform compatibility**: Optimized for Windows with DirectShow backend support
- **Robust camera detection**: Tests multiple camera indices and backends
- **Error handling**: Comprehensive error messages and troubleshooting guidance

## Technical Details

- **OpenCV**: Used for webcam capture and image processing
- **Tesseract OCR**: Text recognition engine
- **PIL/Pillow**: Image format conversion
- **DirectShow backend**: Windows-specific camera backend for better compatibility
- **Multiple camera index testing**: Automatically finds working camera

## Requirements

- Python 3.8+
- OpenCV (cv2)
- pytesseract
- Pillow (PIL)
- numpy
- Tesseract OCR engine

All Python dependencies are automatically installed via `uv pip install -e .`
