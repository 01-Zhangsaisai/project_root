# tests/unit/test_doc_parser.py

import pytest
from pathlib import Path
from src.parsers.doc_parser import DOCParser
from src.utils.exceptions import InvalidFileError


class TestDOCParser:

    @pytest.fixture(scope="module")
    def valid_doc(self):
        """Фикстура для корректного DOC файла"""
        return Path("tests/data/valid/sample.doc")

    @pytest.fixture(scope="module")
    def invalid_doc(self):
        """Фикстура для поврежденного DOC файла"""
        return Path("tests/data/invalid/corrupted.doc")

    def test_extract_text_success(self, valid_doc):
        """Тестирование успешного извлечения текста"""
        parser = DOCParser(valid_doc)
        text = parser.extract_text()

        assert isinstance(text, str)
        assert len(text) > 0
        assert "Пример текста" in text  # Заменить на реальное содержимое

    def test_invalid_doc_raises_exception(self, invalid_doc):
        """Тестирование обработки поврежденного файла"""
        with pytest.raises(InvalidFileError):
            DOCParser(invalid_doc).extract_text()