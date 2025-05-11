# src/parsers/html_parser.py
from bs4 import BeautifulSoup
from pathlib import Path
from .base_parser import BaseParser
from src.utils.exceptions import InvalidFileError


class HTMLParser(BaseParser):
    """
    Парсер HTML-документов
    Поддерживаемые форматы: text/html, application/xhtml+xml, .html, .htm
    """

    SUPPORTED_MIME_TYPES = ['text/html', 'application/xhtml+xml']
    SUPPORTED_EXTENSIONS = ['.html', '.htm']

    def _validate_file(self):
        """Проверка структуры HTML"""
        super()._validate_file()
        path = Path(self.file_path)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                BeautifulSoup(f.read(), 'html.parser')
        except Exception as e:
            raise InvalidFileError("html", path, "некорректная структура HTML") from e

    def extract_text(self) -> str:
        """Извлечение чистого текста"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return BeautifulSoup(f, 'html.parser').get_text().strip()

    def extract_metadata(self) -> dict:
        """Извлечение метаинформации"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            return {
                "title": soup.title.string if soup.title else None,
                "charset": soup.original_encoding
            }

    def extract_images(self) -> list:
        """Извлечение ссылок на изображения"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            return [img['src'] for img in soup.find_all('img') if img.get('src')]