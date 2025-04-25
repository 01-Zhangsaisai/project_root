# tests/unit/test_docx_parser.py

import pytest
from pathlib import Path
from src.parsers.docx_parser import DOCXParser
from src.utils.exceptions import InvalidDOCXException

class TestDOCXParser:

    @pytest.fixture(scope="module")
    def valid_docx(self):
        return Path("tests/data/valid/sample.docx")

    @pytest.fixture(scope="module")
    def invalid_docx(self):
        return Path("tests/data/invalid/corrupted.docx")

    def test_extract_text_success(self, valid_docx):
        parser = DOCXParser(valid_docx)
        text = parser.extract_text()
        
        assert isinstance(text, str)
        assert len(text) > 0  
        assert "Expected Text Content" in text  # 替换为实际预期内容或关键字
    
    def test_extract_metadata_success(self, valid_docx):
        parser = DOCXParser(valid_docx)
        
        metadata = parser.extract_metadata()
        
        assert isinstance(metadata, dict)
        assert metadata.get('title') == "Expected Title"  # 替换为实际预期标题
    
    def test_invalid_docx_raises_exception(self, invalid_docx):
         with pytest.raises(InvalidDOCXException):
             DOCXParser(invalid_docx).extract_text()  
