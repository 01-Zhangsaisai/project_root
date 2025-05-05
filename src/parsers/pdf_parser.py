# src/parsers/pdf_parser.py
import fitz
from pathlib import Path
from typing import Dict, List
from .base_parser import BaseParser
from src.utils.exceptions import InvalidFileError


class PDFParser(BaseParser):
    """
    PDF文档解析器
    功能：提取文本/元数据/图片
    支持格式：.pdf, application/pdf
    """

    SUPPORTED_MIME_TYPES = ['application/pdf']
    SUPPORTED_EXTENSIONS = ['.pdf']

    def _validate_file(self):
        """PDF文件深度验证"""
        super()._validate_file()
        try:
            with fitz.open(self.file_path) as doc:
                if doc.is_encrypted:
                    raise InvalidFileError("pdf", Path(self.file_path), "文件已加密")
                if doc.page_count == 0:
                    raise InvalidFileError("pdf", Path(self.file_path), "空文档")
        except fitz.FileDataError:
            raise InvalidFileError("pdf", Path(self.file_path), "文件损坏") from None

    def extract_text(self) -> str:
        """提取PDF文本内容"""
        try:
            with fitz.open(self.file_path) as doc:
                return "\n".join(page.get_text() for page in doc)
        except Exception as e:
            raise RuntimeError(f"文本提取失败: {str(e)}")

    def extract_metadata(self) -> Dict[str, str]:
        """安全提取PDF元数据"""
        with fitz.open(self.file_path) as doc:
            meta = doc.metadata or {}
            return {
                "title": meta.get("title", "未知标题"),
                "author": meta.get("author", "未知作者"),
                "creator": meta.get("creator", "未知创建工具"),
                "creation_date": meta.get("creationDate", "未知日期")
            }

    def extract_images(self) -> List[bytes]:
        """提取PDF中的图片"""
        images = []
        try:
            with fitz.open(self.file_path) as doc:
                for page in doc:
                    for img in page.get_images():
                        xref = img[0]
                        images.append(doc.extract_image(xref)["image"])
        except Exception as e:
            raise RuntimeError(f"图片提取失败: {str(e)}")
        return images