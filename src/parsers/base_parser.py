# src/parsers/base_parser.py

from abc import ABC, abstractmethod

class BaseParser(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def extract_text(self) -> str:
        """提取文本内容"""
        pass

    @abstractmethod
    def extract_metadata(self) -> dict:
        """提取元数据"""
        pass

    @abstractmethod
    def extract_images(self) -> list:
        """提取图片，返回图片二进制列表"""
        pass
