# src/parsers/docx_parser.py

from docx import Document  # pip install python-docx   
from .base_parser import BaseParser   
from src.utils.exceptions import InvalidDOCXException  


class DOCXParser(BaseParser): 
    
    SUPPORTED_MIME_TYPES = ['application/vnd.openxmlformats-officedocument.wordprocessingml.document']   
    SUPPORTED_EXTENSIONS = ['.docx']  

    
    def extract_text(self) -> str:
         try:
              doc = Document(self.file_path)
              text_chunks = [para.text for para in doc.paragraphs]
              return "\n".join(text_chunks).strip()
         except Exception as e:
              raise InvalidDOCXException(f"Failed to extract text from DOCX file: {e}")

    
     def extract_metadata(self) -> dict:
         try:
              doc = Document(self.file_path)
              core_properties = doc.core_properties
        return {
                  "title": core_properties.title,
                  "author": core_properties.author,
                  "created": core_properties.created,
                  "modified": core_properties.modified,
              }
         except Exception as e:
              raise InvalidDOCXException(f"Failed to extract metadata from DOCX file: {e}")

    
     def extract_images(self) -> list:
         images = []
         try:
             doc = Document(self.file_path)
             for rel in doc.part.rels.values():
                 if "image" in rel.reltype:
                     image_data = rel.target_part.blob  # 获取图片二进制数据。
                     images.append(image_data)
             return images   
         except Exception as e:
             raise InvalidDOCXException(f"Failed to extract images from DOCX file: {e}")