# src/parsers/doc_parser.py
import win32com.client
from pathlib import Path
from typing import List
from .base_parser import BaseParser
from src.utils.exceptions import InvalidFileError, FileAccessError


class DOCParser(BaseParser):
    """
    Парсер документов Microsoft Word (.doc)
    Поддерживаемые форматы: application/msword, .doc
    """

    SUPPORTED_MIME_TYPES = ['application/msword']
    SUPPORTED_EXTENSIONS = ['.doc']

    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.word_app = None
        self._init_word_app()

    def _init_word_app(self):
        """Инициализация приложения Word"""
        try:
            self.word_app = win32com.client.Dispatch("Word.Application")
            self.word_app.Visible = False  # Фоновый режим
        except Exception as e:
            raise FileAccessError(Path(self.file_path), "запуск Word") from e

    def _validate_file(self):
        """Проверка DOC-файла"""
        super()._validate_file()
        try:
            doc = self.word_app.Documents.Open(self.file_path)
            doc.Close(SaveChanges=False)
        except Exception as e:
            raise InvalidFileError("doc", Path(self.file_path), "файл поврежден") from e

    def extract_text(self) -> str:
        """Извлечение текста"""
        try:
            doc = self.word_app.Documents.Open(self.file_path)
            text = doc.Content.Text.strip()
            doc.Close(SaveChanges=False)
            return text
        except Exception as e:
            raise FileAccessError(Path(self.file_path), "чтение текста") from e

    def extract_metadata(self) -> dict:
        """Извлечение метаданных"""
        try:
            doc = self.word_app.Documents.Open(self.file_path)
            props = {
                "title": doc.BuiltInDocumentProperties("Title").Value,
                "author": doc.BuiltInDocumentProperties("Author").Value,
                "company": doc.BuiltInDocumentProperties("Company").Value,
                "created": doc.BuiltInDocumentProperties("Creation Date").Value
            }
            doc.Close(SaveChanges=False)
            return props
        except Exception as e:
            return {"error": str(e)}

    def extract_images(self) -> List[bytes]:
        """Извлечение изображений (заглушка)"""
        return []

    def __del__(self):
        """Завершение работы Word"""
        if self.word_app:
            self.word_app.Quit()
            self.word_app = None