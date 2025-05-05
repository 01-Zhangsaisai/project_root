# src/parsers/docx_parser.py
from docx import Document
from docx.opc.exceptions import PackageNotFoundError
from pathlib import Path
from .base_parser import BaseParser
from src.utils.exceptions import InvalidFileError


class DOCXParser(BaseParser):
    """
    Microsoft Word文档解析器（新版）
    支持格式：application/vnd.openxmlformats-officedocument.wordprocessingml.document, .docx
    """

    SUPPORTED_MIME_TYPES = ['application/vnd.openxmlformats-officedocument.wordprocessingml.document']
    SUPPORTED_EXTENSIONS = ['.docx']

    def _validate_file(self):
        """执行DOCX特定验证"""
        super()._validate_file()
        path = Path(self.file_path)
        try:
            Document(path)
        except PackageNotFoundError:
            raise InvalidFileError("docx", path, "文件损坏") from None

    def extract_text(self) -> str:
        """提取文档文本内容"""
        doc = Document(self.file_path)
        return "\n".join(para.text for para in doc.paragraphs)

    def extract_metadata(self) -> dict:
        """提取文档属性信息"""
        doc = Document(self.file_path)
        return {
            "title": doc.core_properties.title,
            "author": doc.core_properties.author,
            "created": doc.core_properties.created
        }

    def extract_images(self) -> list:
        """提取嵌入式图片"""
        doc = Document(self.file_path)
        return [rel.target_part.blob for rel in doc.part.rels.values() if "image" in rel.reltype]