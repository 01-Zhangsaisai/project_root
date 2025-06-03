# src/parsers/doc_parser.py
from pathlib import Path
from typing import List
from .base_parser import BaseParser
from src.utils.exceptions import InvalidFileError, FileAccessError
from docx import Document

class DOCParser(BaseParser):
    """
    Парсер документов Microsoft Word (.docx)
    Поддерживаемые форматы: application/vnd.openxmlformats-officedocument.wordprocessingml.document, .docx
    """

    SUPPORTED_MIME_TYPES = ['application/vnd.openxmlformats-officedocument.wordprocessingml.document']
    SUPPORTED_EXTENSIONS = ['.docx']

    def __init__(self, file_path: str):
        super().__init__(file_path)

    def _validate_file(self):
        """Проверка DOCX-файла"""
        super()._validate_file()
        try:
            doc = Document(self.file_path)
        except Exception as e:
            raise InvalidFileError("docx", Path(self.file_path), "файл поврежден") from e

    def extract_text(self) -> str:
        """Извлечение текста"""
        try:
            doc = Document(self.file_path)
            text = '\n'.join([para.text for para in doc.paragraphs]).strip()
            return text
        except Exception as e:
            raise FileAccessError(Path(self.file_path), "чтение текста") from e

    def extract_metadata(self) -> dict:
        """Извлечение метаданных"""
        return {}

    def extract_images(self) -> List[bytes]:
        """Извлечение изображений (заглушка)"""
        return []

    def __del__(self):
        pass  
