# src/parsers/pdf_parser.py
import fitz
from pathlib import Path
from typing import Dict, List
from .base_parser import BaseParser
from src.utils.exceptions import InvalidFileError


class PDFParser(BaseParser):
    """
    Парсер PDF-документов
    Функционал: извлечение текста/метаданных/изображений
    Поддерживаемые форматы: .pdf, application/pdf
    """

    SUPPORTED_MIME_TYPES = ['application/pdf']
    SUPPORTED_EXTENSIONS = ['.pdf']

    def _validate_file(self):
        """Углубленная проверка PDF"""
        super()._validate_file()
        try:
            with fitz.open(self.file_path) as doc:
                if doc.is_encrypted:
                    raise InvalidFileError("pdf", Path(self.file_path), "файл зашифрован")
                if doc.page_count == 0:
                    raise InvalidFileError("pdf", Path(self.file_path), "пустой документ")
        except fitz.FileDataError:
            raise InvalidFileError("pdf", Path(self.file_path), "файл поврежден") from None

    def extract_text(self) -> str:
        """Извлечение текста из PDF"""
        try:
            with fitz.open(self.file_path) as doc:
                return "\n".join(page.get_text() for page in doc)
        except Exception as e:
            raise RuntimeError(f"Ошибка извлечения текста: {str(e)}")

    def extract_metadata(self) -> Dict[str, str]:
        """Безопасное извлечение метаданных"""
        with fitz.open(self.file_path) as doc:
            meta = doc.metadata or {}
            return {
                "title": meta.get("title", "Без названия"),
                "author": meta.get("author", "Неизвестный автор"),
                "creator": meta.get("creator", "Неизвестная программа"),
                "creation_date": meta.get("creationDate", "Неизвестная дата")
            }

    def extract_images(self) -> List[bytes]:
        """Извлечение изображений из PDF"""
        images = []
        try:
            with fitz.open(self.file_path) as doc:
                for page in doc:
                    for img in page.get_images():
                        xref = img[0]
                        images.append(doc.extract_image(xref)["image"])
        except Exception as e:
            raise RuntimeError(f"Ошибка извлечения изображений: {str(e)}")
        return images