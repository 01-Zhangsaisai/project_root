# src/parsers/doc_parser.py
import win32com.client
from pathlib import Path
from typing import List
from .base_parser import BaseParser
from src.utils.exceptions import InvalidFileError, FileAccessError


class DOCParser(BaseParser):
    """
    Microsoft Word文档解析器 (旧版 .doc 格式)
    支持格式：application/msword, .doc
    """

    SUPPORTED_MIME_TYPES = ['application/msword']
    SUPPORTED_EXTENSIONS = ['.doc']

    def __init__(self, file_path: str):
        """
        初始化DOC解析器
        :param file_path: .doc文件路径
        :raises FileAccessError: 文件访问失败
        :raises InvalidFileError: 文件格式无效
        """
        super().__init__(file_path)
        self.word_app = None
        self._init_word_app()

    def _init_word_app(self):
        """初始化Word应用程序实例"""
        try:
            self.word_app = win32com.client.Dispatch("Word.Application")
            self.word_app.Visible = False  # 后台运行
        except Exception as e:
            raise FileAccessError(Path(self.file_path), "启动Word服务") from e

    def _validate_file(self):
        """执行DOC文件验证"""
        super()._validate_file()
        try:
            doc = self.word_app.Documents.Open(self.file_path)
            doc.Close(SaveChanges=False)
        except Exception as e:
            raise InvalidFileError("doc", Path(self.file_path), "文件损坏或密码保护") from e

    def extract_text(self) -> str:
        """
        提取文档文本内容
        :return: 去空白后的纯文本
        :raises FileAccessError: 读取失败
        """
        try:
            doc = self.word_app.Documents.Open(self.file_path)
            text = doc.Content.Text.strip()
            doc.Close(SaveChanges=False)
            return text
        except Exception as e:
            raise FileAccessError(Path(self.file_path), "读取文本") from e

    def extract_metadata(self) -> dict:
        """
        提取文档元数据
        :return: 包含标题/作者等元数据的字典
        """
        try:
            doc = self.word_app.Documents.Open(self.file_path)
            props = {
                "title": doc.BuiltInDocumentProperties("Title").Value,
                "author": doc.BuiltInDocumentProperties("Author").Value,
                "company": doc.BuiltInDocumentProperties("Company").Value,
                "created": doc.BuiltInDocumentProperties("Creation Date").Value
            }
            doc.Close(SaveChanges=False)
            return props
        except Exception as e:
            return {"error": str(e)}

    def extract_images(self) -> List[bytes]:
        """
        提取文档内嵌图片 (占位实现)
        :return: 空列表（旧版DOC图片提取需要更复杂处理）
        """
        return []

    def __del__(self):
        """清理Word应用实例"""
        if self.word_app:
            self.word_app.Quit()
            self.word_app = None