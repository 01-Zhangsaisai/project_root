# src/parsers/pdf_parser.py

import fitz  # PyMuPDF库，pip install pymupdf 
from .base_parser import BaseParser 
from src.utils.exceptions import InvalidPDFException 


class PDFParser(BaseParser): 
    
    SUPPORTED_MIME_TYPES = ['application/pdf'] 
    SUPPORTED_EXTENSIONS = ['.pdf'] 

    
    def extract_text(self) -> str: 
        try: 
            text_chunks = [] 
            with fitz.open(self.file_path) as doc: 
                for page in doc: 
                    text_chunks.append(page.get_text()) 
            return "\n".join(text_chunks).strip() 
        except Exception as e: 
            raise InvalidPDFException(f"Failed to extract text: {e}") 

    
    def extract_metadata(self) -> dict: 
        try: 
            with fitz.open(self.file_path) as doc: 
                meta = doc.metadata or {} 
            return { 
                "title": meta.get("title"), 
                "author": meta.get("author"), 
                "creation_date": meta.get("creationDate") 
            } 
        except Exception as e: 
            raise InvalidPDFException(f"Failed to extract metadata: {e}") 

    
    def extract_images(self) -> list: 
        images = [] 
        try: 
            with fitz.open(self.file_path) as doc: 
                for page in doc: 
                    for img_info in page.get_images(full=True): 
                        xref = img_info[0] 
                        base_image = doc.extract_image(xref) 
                        images.append(base_image["image"]) 
            return images 
        except Exception as e: 
            raise InvalidPDFException(f"Failed to extract images: {e}") 
