# tests/unit/test_djvu_parser.py

import pytest
from pathlib import Path
from src.parsers.djvu_parser import DJVUParser
from src.utils.exceptions import InvalidDJVUException

class TestDJVUParser:

    @pytest.fixture(scope="module")
    def valid_djvu(self):
        return Path("tests/data/valid/sample.djvu")

    @pytest.fixture(scope="module")
    def invalid_djvu(self):
        return Path("tests/data/invalid/corrupted.djvu")

    def test_basic_parsing(self, valid_djvu):
        parser = DJVUParser(valid_djvu)
        text = parser.extract_text()
        
        assert isinstance(text, str)
    
    def test_metadata_extraction(self, valid_djvu):
        parser = DJVUParser(valid_djvu)
        
        metadata = parser.extract_metadata()
        
        assert isinstance(metadata, dict)

    
    def test_invalid_file(self, invalid_djvu):
         with pytest.raises(InvalidDJVUException):
             DJVUParser(invalid_djvu).extract_text()
