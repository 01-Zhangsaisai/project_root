# tests/unit/test_pdf_parser.py
import pytest
from pathlib import Path
from src.parsers.pdf_parser import PDFParser
from src.utils.exceptions import InvalidFileError


class TestPDFParser:

    @pytest.fixture(scope="module")
    def valid_pdf(self):
        return Path("tests/data/valid/sample.pdf")

    @pytest.fixture(scope="module")
    def invalid_pdf(self):
        return Path("tests/data/invalid/corrupted.pdf")

    def test_extract_text_success(self, valid_pdf):
        parser = PDFParser(valid_pdf)
        text = parser.extract_text()

        assert isinstance(text, str)
        assert len(text) > 0
        assert "Пример текста" in text

    def test_extract_metadata_success(self, valid_pdf):
        parser = PDFParser(valid_pdf)
        metadata = parser.extract_metadata()

        assert isinstance(metadata, dict)
        assert metadata.get('title') == "Пример заголовка"

    def test_invalid_pdf_raises_exception(self, invalid_pdf):
        with pytest.raises(InvalidFileError):
            PDFParser(invalid_pdf).extract_text()

    def test_empty_pdf_raises_exception(self, tmp_path):
        empty_pdf_file = tmp_path / "empty.pdf"
        empty_pdf_file.write_bytes(b"%PDF-1.4\n%EOF\n")

        with pytest.raises(InvalidFileError):
            PDFParser(empty_pdf_file).extract_text()