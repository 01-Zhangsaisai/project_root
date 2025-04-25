# src/parsers/html_parser.py

from bs4 import BeautifulSoup  # pip install beautifulsoup4 lxml html5lib  
from .base_parser import BaseParser  
from src.utils.exceptions import InvalidHTMLException  

class HTMLParser(BaseParser): 
    
    SUPPORTED_MIME_TYPES = ['text/html', 'application/xhtml+xml']  
    SUPPORTED_EXTENSIONS = ['.html', '.htm']  

    def extract_text(self) -> str:  
        """从 HTML 文件中提取文本。

        返回:
            str: 提取的文本内容。

        异常:
            InvalidHTMLException: 如果无法从 HTML 文件中提取文本。
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:  
            soup = BeautifulSoup(file, 'html.parser')  
            return soup.get_text().strip()  

    def extract_metadata(self) -> dict:  
        """从 HTML 文件中提取元数据。

        返回:
            dict: 包含文档元数据的字典，包括标题。

        异常:
            InvalidHTMLException: 如果无法从 HTML 文件中提取元数据。
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:  
            soup = BeautifulSoup(file, 'html.parser')  
            title = soup.title.string if soup.title else None  
            return {"title": title}  

    def extract_images(self) -> list:
        """从 HTML 文件中提取图像 URL。

        返回:
            list: 包含图像 URL 的列表。

        异常:
            InvalidHTMLException: 如果无法从 HTML 文件中提取图像。
        """
        images = []  
        with open(self.file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            img_tags = soup.find_all('img')
            for img in img_tags:
                img_url = img['src']
                images.append(img_url)
        
        return images   