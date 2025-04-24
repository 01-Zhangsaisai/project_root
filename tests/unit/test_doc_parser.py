# tests/unit/test_doc_parser.py

import pytest
from pathlib import Path
from src.parsers.doc_parser import DOCParser
from src.utils.exceptions import InvalidDOCException

class TestDOCParser:

    @pytest.fixture(scope="module")
    def valid_doc(self):
        return Path("tests/data/valid/sample.doc")

    @pytest.fixture(scope="module")
    def invalid_doc(self):
        return Path("tests/data/invalid/corrupted.doc")

    def test_extract_text_success(self, valid_doc):
        parser = DOCParser(valid_doc)
        text = parser.extract_text()
        
        assert isinstance(text, str)
        assert len(text) > 0  
        assert "Expected Text Content" in text  # 替换为实际预期内容或关键字
    
    def test_invalid_doc_raises_exception(self, invalid_doc):
         with pytest.raises(InvalidDOCException):
             DOCParser(invalid_doc).extract_text()