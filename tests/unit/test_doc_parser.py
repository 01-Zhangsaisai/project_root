# tests/unit/test_doc_parser.py

import pytest
from pathlib import Path
from src.parsers.doc_parser import DOCParser
from src.utils.exceptions import InvalidDOCException

class TestDOCParser:

    @pytest.fixture(scope="module")
    def valid_doc(self):
        """Fixture for a valid DOC file."""
        return Path("tests/data/valid/sample.doc")

    @pytest.fixture(scope="module")
    def invalid_doc(self):
        """Fixture for an invalid (corrupted) DOC file."""
        return Path("tests/data/invalid/corrupted.doc")

    def test_extract_text_success(self, valid_doc):
        """测试成功提取文本的情况。

        参数:
            valid_doc: 有效的 DOC 文件路径。

        断言:
            - 返回的文本是字符串。
            - 文本长度大于 0。
            - 文本中包含预期内容。
        """
        parser = DOCParser(valid_doc)
        text = parser.extract_text()
        
        assert isinstance(text, str)
        assert len(text) > 0  
        assert "Expected Text Content" in text  # 替换为实际预期内容或关键字
    
    def test_invalid_doc_raises_exception(self, invalid_doc):
        """测试从无效 DOC 文件提取文本时引发异常的情况。

        参数:
            invalid_doc: 无效的 DOC 文件路径。

        断言:
            - 调用 extract_text 方法时应引发 InvalidDOCException。
        """
        with pytest.raises(InvalidDOCException):
            DOCParser(invalid_doc).extract_text()  