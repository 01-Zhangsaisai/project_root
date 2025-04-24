# src/parsers/djvu_parser.py

from pydjvu import DjVuDocument  # pip install pydjvu
from .base_parser import BaseParser
from src.utils.exceptions import InvalidDJVUException

class DJVUParser(BaseParser):
    
    SUPPORTED_MIME_TYPES = ['image/vnd.djvu']
    SUPPORTED_EXTENSIONS = ['.djvu']

    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self) -> str:
        try:
            document = DjVuDocument(self.file_path)
            text = ""
            for page in document.pages:
                text += page.text + "\n"
            return text.strip()
        except Exception as e:
            raise InvalidDJVUException(f"Failed to extract text from DJVU file: {e}")

    def extract_metadata(self) -> dict:
        try:
            document = DjVuDocument(self.file_path)
            metadata = {
                "title": document.title,
                "author": document.author,
                "num_pages": len(document.pages)
            }
            return metadata
        except Exception as e:
            raise InvalidDJVUException(f"Failed to extract metadata from DJVU file: {e}")

    def extract_images(self) -> list:
        images = []
        try:
            document = DjVuDocument(self.file_path)
            for i, page in enumerate(document.pages):
                image_path = f"page_{i + 1}.png"  # Save each page as an image
                page.save_image(image_path)  # Save the image (you may need to adjust this based on your needs)
                images.append(image_path)
            return images
        except Exception as e:
            raise InvalidDJVUException(f"Failed to extract images from DJVU file: {e}")