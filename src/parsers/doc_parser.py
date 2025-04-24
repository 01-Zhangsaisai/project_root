# src/parsers/doc_parser.py

import win32com.client  # pip install pywin32   
from .base_parser import BaseParser   
from src.utils.exceptions import InvalidDOCException  


class DOCParser(BaseParser): 
    
     SUPPORTED_MIME_TYPES = ['application/msword']   
     SUPPORTED_EXTENSIONS = ['.doc']  

     
     def __init__(self, file_path):   
         super().__init__(file_path)   
         self.word_app = win32com.client.Dispatch('Word.Application')   

     
     def extract_text(self) -> str:
          try:
               doc = self.word_app.Documents.Open(self.file_path)
               text_content = doc.Content.Text.strip()
               doc.Close(False)
               return text_content   
          except Exception as e:
               raise InvalidDOCException(f"Failed to extract text from DOC file: {e}")
          finally:
               self.word_app.Quit()

     
     def extract_metadata(self) -> dict:
          try:
               doc = self.word_app.Documents.Open(self.file_path)
               properties = {
                   "title": doc.BuiltInDocumentProperties("Title").Value,
                   "author": doc.BuiltInDocumentProperties("Author").Value,
                   "created": doc.BuiltInDocumentProperties("Creation Date").Value,
                   "modified": doc.BuiltInDocumentProperties("Last Author").Value,
               }
               doc.Close(False)
               return properties   
          except Exception as e:
               raise InvalidDOCException(f"Failed to extract metadata from DOC file: {e}")
          finally:
               self.word_app.Quit()

     
     def extract_images(self) -> list:
          images = []
          try:
               doc = self.word_app.Documents.Open(self.file_path)
               for shape in doc.InlineShapes:
                    print(shape)
                    