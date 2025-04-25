# src/parsers/docx_parser.py

from docx import Document  # pip install python-docx   
from .base_parser import BaseParser   
from src.utils.exceptions import InvalidDOCXException  

class DOCXParser(BaseParser): 
    
    SUPPORTED_MIME_TYPES = ['application/vnd.openxmlformats-officedocument.wordprocessingml.document']   
    SUPPORTED_EXTENSIONS = ['.docx']  

    def extract_text(self) -> str:
        """从 DOCX 文件中提取文本。

        返回:
            str: 提取的文本内容。

        异常:
            InvalidDOCXException: 如果无法从 DOCX 文件中提取文本。
        """
        doc = Document(self.file_path)
        text_chunks = [para.text for para in doc.paragraphs]
        return "\n".join(text_chunks).strip()

    def extract_metadata(self) -> dict:
        """从 DOCX 文件中提取元数据。

        返回:
            dict: 包含文档元数据的字典，包括标题、作者、创建时间和修改时间。

        异常:
            InvalidDOCXException: 如果无法从 DOCX 文件中提取元数据。
        """
        doc = Document(self.file_path)
        core_properties = doc.core_properties
        return {
            "title": core_properties.title,
            "author": core_properties.author,
            "created": core_properties.created,
            "modified": core_properties.modified,
        }

    def extract_images(self) -> list:
        """从 DOCX 文件中提取图像。

        返回:
            list: 包含图像二进制数据的列表。

        异常:
            InvalidDOCXException: 如果无法从 DOCX 文件中提取图像。
        """
        images = []
        doc = Document(self.file_path)
        for rel in doc.part.rels.values():
            if "image" in rel.reltype:
                image_data = rel.target_part.blob  # 获取图片二进制数据
                images.append(image_data)
        return images