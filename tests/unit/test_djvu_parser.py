# tests/unit/test_djvu_parser.py

import pytest
from pathlib import Path
from src.parsers.djvu_parser import DJVUParser
from src.utils.exceptions import InvalidFileError


class TestDJVUParser:

    @pytest.fixture(scope="module")
    def valid_djvu(self):
        return Path("tests/data/valid/sample.djvu")

    @pytest.fixture(scope="module")
    def invalid_djvu(self):
        return Path("tests/data/invalid/corrupted.djvu")

    def test_basic_parsing(self, valid_djvu):
        """Тестирование извлечения текста из корректного DJVU файла"""
        parser = DJVUParser(valid_djvu)
        text = parser.extract_text()

        assert isinstance(text, str)
        assert len(text) > 0
        assert "Пример текста" in text

    def test_metadata_extraction(self, valid_djvu):
        """Тестирование извлечения метаданных из DJVU файла"""
        parser = DJVUParser(valid_djvu)

        metadata = parser.extract_metadata()

        assert isinstance(metadata, dict)
        assert "title" in metadata  # Проверка наличия заголовка
        assert "author" in metadata  # Проверка наличия автора
        assert "creationDate" in metadata  # Проверка даты создания

    def test_invalid_file(self, invalid_djvu):
        """Тестирование обработки некорректного DJVU файла"""
        with pytest.raises(InvalidFileError):
            DJVUParser(invalid_djvu).extract_text()