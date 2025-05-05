# src/parsers/djvu_parser.py
import subprocess
import os
import fitz
from pathlib import Path
from .base_parser import BaseParser
from src.utils.exceptions import InvalidFileError, FileAccessError


class DJVUParser(BaseParser):
    """
    DjVu图像文档解析器
    支持格式：image/vnd.djvu, .djvu
    """

    SUPPORTED_MIME_TYPES = ['image/vnd.djvu']
    SUPPORTED_EXTENSIONS = ['.djvu']

    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.pdf_path = self._convert_to_pdf()

    def _validate_file(self):
        """执行DjVu特定验证"""
        super()._validate_file()
        path = Path(self.file_path)
        with open(path, 'rb') as f:
            if f.read(4) != b'AT&T':
                raise InvalidFileError("djvu", path, "无效文件头")

    def _convert_to_pdf(self) -> str:
        """将DjVu转换为临时PDF文件"""
        pdf_path = Path(self.file_path).with_suffix('.pdf')
        try:
            subprocess.run(
                ["ddjvu", "-format=pdf", self.file_path, str(pdf_path)],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise InvalidFileError("djvu", Path(self.file_path), "格式转换失败") from None
        return str(pdf_path)

    def extract_text(self) -> str:
        """从转换后的PDF提取文本"""
        with fitz.open(self.pdf_path) as doc:
            return "\n".join(page.get_text() for page in doc)

    def extract_metadata(self) -> dict:
        """提取元数据"""
        with fitz.open(self.pdf_path) as doc:
            return dict(doc.metadata)

    def extract_images(self) -> list:
        """提取图像数据"""
        images = []
        with fitz.open(self.pdf_path) as doc:
            for page in doc:
                images.extend(doc.extract_image(img[0])["image"] for img in page.get_images())
        return images

    def __del__(self):
        """清理临时PDF文件"""
        if os.path.exists(self.pdf_path):
            os.remove(self.pdf_path)