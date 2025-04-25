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
        """测试从有效 DJVU 文件中提取文本"""
        parser = DJVUParser(valid_djvu)
        text = parser.extract_text()
        
        assert isinstance(text, str)
        assert len(text) > 0  # 确保提取的文本不为空
        assert "Expected Content" in text  # 替换为实际预期内容或关键字
    
    def test_metadata_extraction(self, valid_djvu):
        """测试从有效 DJVU 文件中提取元数据"""
        parser = DJVUParser(valid_djvu)
        
        metadata = parser.extract_metadata()
        
        assert isinstance(metadata, dict)
        assert "title" in metadata  # 确保元数据中包含标题
        assert "author" in metadata  # 确保元数据中包含作者（如果适用）
        assert "num_pages" in metadata  # 确保元数据中包含页数
    
    def test_invalid_file(self, invalid_djvu):
        """测试处理无效 DJVU 文件时抛出异常"""
        with pytest.raises(InvalidDJVUException):
            DJVUParser(invalid_djvu).extract_text()