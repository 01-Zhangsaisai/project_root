# src/parsers/html_parser.py
from bs4 import BeautifulSoup
from pathlib import Path
from .base_parser import BaseParser
from src.utils.exceptions import InvalidFileError


class HTMLParser(BaseParser):
    """
    HTML文档解析器
    支持格式：text/html, application/xhtml+xml, .html, .htm
    """

    SUPPORTED_MIME_TYPES = ['text/html', 'application/xhtml+xml']
    SUPPORTED_EXTENSIONS = ['.html', '.htm']

    def _validate_file(self):
        """执行HTML结构验证"""
        super()._validate_file()
        path = Path(self.file_path)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                BeautifulSoup(f.read(), 'html.parser')
        except Exception as e:
            raise InvalidFileError("html", path, "无效的HTML结构") from e

    def extract_text(self) -> str:
        """提取纯文本内容"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return BeautifulSoup(f, 'html.parser').get_text().strip()

    def extract_metadata(self) -> dict:
        """提取网页元信息"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            return {
                "title": soup.title.string if soup.title else None,
                "charset": soup.original_encoding
            }

    def extract_images(self) -> list:
        """提取图片链接"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            return [img['src'] for img in soup.find_all('img') if img.get('src')]