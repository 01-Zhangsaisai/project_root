# tests/unit/test_html_parser.py

import pytest
from pathlib import Path
from src.parsers.html_parser import HTMLParser
from src.utils.exceptions import InvalidFileError


class TestHTMLParser:

    @pytest.fixture(scope="module")
    def valid_html(self):
        return Path("tests/data/valid/sample.html")

    @pytest.fixture(scope="module")
    def invalid_html(self):
        return Path("tests/data/invalid/corrupted.html")

    def test_basic_parsing(self, valid_html):
        """Тестирование базового парсинга HTML"""
        parser = HTMLParser(valid_html)
        text = parser.extract_text()

        assert isinstance(text, str)
        assert len(text) > 0
        assert "Тестовый контент" in text  # Заменить реальным содержимым

    def test_metadata_extraction(self, valid_html):
        """Тестирование извлечения метаданных"""
        parser = HTMLParser(valid_html)

        meta = parser.extract_metadata()

        assert isinstance(meta, dict)
        assert "title" in meta  # Проверка заголовка
        assert "charset" in meta  # Проверка кодировки

    def test_invalid_file(self, invalid_html):
        """Тестирование обработки некорректного HTML"""
        with pytest.raises(InvalidFileError):
            HTMLParser(invalid_html).extract_text()