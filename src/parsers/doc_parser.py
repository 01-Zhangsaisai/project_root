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
        """从 DOC 文件中提取文本。

        返回:
            str: 提取的文本内容。

        异常:
            InvalidDOCException: 如果无法从 DOC 文件中提取文本。
        """
        doc = self.word_app.Documents.Open(self.file_path)
        text_content = doc.Content.Text.strip()
        doc.Close(False)
        return text_content   

    def extract_metadata(self) -> dict:
        """从 DOC 文件中提取元数据。

        返回:
            dict: 包含文档元数据的字典，包括标题、作者、创建时间和修改时间。

        异常:
            InvalidDOCException: 如果无法从 DOC 文件中提取元数据。
        """
        doc = self.word_app.Documents.Open(self.file_path)
        properties = {
            "title": doc.BuiltInDocumentProperties("Title").Value,
            "author": doc.BuiltInDocumentProperties("Author").Value,
            "created": doc.BuiltInDocumentProperties("Creation Date").Value,
            "modified": doc.BuiltInDocumentProperties("Last Author").Value,
        }
        doc.Close(False)
        return properties   

    def extract_images(self) -> list:
        """从 DOC 文件中提取图像。

        返回:
            list: 包含图像信息的列表。

        异常:
            InvalidDOCException: 如果无法从 DOC 文件中提取图像。
        """
        images = []
        doc = self.word_app.Documents.Open(self.file_path)
        
        for shape in doc.InlineShapes:
            # 这里可以添加代码来处理图像，例如将其保存到列表中
            print(shape)  # 仅为示例，实际处理逻辑需要实现
        
        doc.Close(False)
        return images