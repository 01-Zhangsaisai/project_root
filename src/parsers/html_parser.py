# src/parsers/html_parser.py

from bs4 import BeautifulSoup  # pip install beautifulsoup4 lxml html5lib  
from .base_parser import BaseParser  
from src.utils.exceptions import InvalidHTMLException  


class HTMLParser(BaseParser): 
    
    SUPPORTED_MIME_TYPES = ['text/html', 'application/xhtml+xml']  
    SUPPORTED_EXTENSIONS = ['.html', '.htm']  

    
    def extract_text(self) -> str:  
        try:  
            with open(self.file_path, 'r', encoding='utf-8') as file:  
                soup = BeautifulSoup(file, 'html.parser')  
                return soup.get_text().strip()  
        except Exception as e:  
            raise InvalidHTMLException(f"Failed to extract text from HTML file: {e}")  

    
    def extract_metadata(self) -> dict:  
        try:  
            with open(self.file_path, 'r', encoding='utf-8') as file:  
                soup = BeautifulSoup(file, 'html.parser')  
                title = soup.title.string if soup.title else None  
                return {"title": title}  
        except Exception as e:  
            raise InvalidHTMLException(f"Failed to extract metadata from HTML file: {e}")  

    
    def extract_images(self) -> list:
         images = []  
         try:
              with open(self.file_path, 'r', encoding='utf-8') as file:
                   soup = BeautifulSoup(file, 'html.parser')
                   img_tags = soup.find_all('img')
                   for img in img_tags:
                       img_url = img['src']
                       images.append(img_url)
              return images   
         except Exception as e:
              raise InvalidHTMLException(f"Failed to extract images from HTML file: {e}")