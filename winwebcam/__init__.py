"""
Webcam capture with OCR functionality.

A Python package for capturing images from webcam and performing OCR (Optical Character Recognition)
on the captured images using Tesseract.
"""

__version__ = "0.1.0"
__author__ = "SuperFly"

from .webcam_ocr import capture_and_ocr

__all__ = ["capture_and_ocr"]
