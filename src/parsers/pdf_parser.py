# src/parsers/pdf_parser.py

import fitz  # PyMuPDF库，pip install pymupdf 
from .base_parser import BaseParser 
from src.utils.exceptions import InvalidPDFException 

class PDFParser(BaseParser): 
    """
    PDFParser 用于解析 PDF 文件并提取文本、元数据和图像。

    Attributes:
        SUPPORTED_MIME_TYPES (list): 支持的 MIME 类型。
        SUPPORTED_EXTENSIONS (list): 支持的文件扩展名。
    """

    SUPPORTED_MIME_TYPES = ['application/pdf'] 
    SUPPORTED_EXTENSIONS = ['.pdf'] 

    def extract_text(self) -> str: 
        """提取 PDF 文件中的文本内容。

        Returns:
            str: 提取的文本内容。

        Raises:
            InvalidPDFException: 如果提取文本失败。
        """
        text_chunks = [] 
        with fitz.open(self.file_path) as doc: 
            for page in doc: 
                text_chunks.append(page.get_text()) 
        return "\n".join(text_chunks).strip() 

    def extract_metadata(self) -> dict: 
        """提取 PDF 文件的元数据。

        Returns:
            dict: 包含文档元数据的字典，包括标题、作者和创建日期。

        Raises:
            InvalidPDFException: 如果提取元数据失败。
        """
        with fitz.open(self.file_path) as doc: 
            meta = doc.metadata or {} 
        return { 
            "title": meta.get("title"), 
            "author": meta.get("author"), 
            "creation_date": meta.get("creationDate") 
        } 

    def extract_images(self) -> list: 
        """提取 PDF 文件中的所有图像。

        Returns:
            list: 包含提取到的图像的列表。

        Raises:
            InvalidPDFException: 如果提取图像失败。
        """
        images = [] 
        with fitz.open(self.file_path) as doc: 
            for page in doc: 
                for img_info in page.get_images(full=True): 
                    xref = img_info[0] 
                    base_image = doc.extract_image(xref) 
                    images.append(base_image["image"]) 
        return images 
