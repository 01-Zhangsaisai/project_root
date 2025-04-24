# tests/unit/test_html_parser.py

import pytest
from pathlib import Path
from src.parsers.html_parser import HTMLParser
from src.utils.exceptions import InvalidHTMLException

class TestHTMLParser:

    @pytest.fixture(scope="module")
    def valid_html(self):
        return Path("tests/data/valid/sample.html")

    @pytest.fixture(scope="module")
    def invalid_html(self):
        return Path("tests/data/invalid/corrupted.html")

    def test_basic_parsing(self, valid_html):
        parser = HTMLParser(valid_html)
        text = parser.extract_text()
        
        assert isinstance(text, str)
        assert len(text) > 0  
        assert "Test Content" in text  # 替换为实际预期内容或关键字
    
    def test_metadata_extraction(self, valid_html):
        parser = HTMLParser(valid_html)
        
        meta = parser.extract_metadata()
        
        assert isinstance(meta, dict)
    
    def test_invalid_file(self, invalid_html):
         with pytest.raises(InvalidHTMLException):
             HTMLParser(invalid_html).extract_text()
