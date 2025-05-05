# src/parsers/base_parser.py
from abc import ABC, abstractmethod
from pathlib import Path
from src.utils.exceptions import InvalidFileError, FileAccessError

class BaseParser(ABC):
    """
    文档解析器抽象基类
    """

    def __init__(self, file_path: str):
        """
        初始化解析器实例
        :param file_path: 文件路径字符串
        :raises FileAccessError: 文件访问失败
        """
        self.file_path = file_path
        self._validate_file()

    def _validate_file(self):
        """
        执行基础文件验证
        :raises FileAccessError: 文件不存在或无法访问
        """
        path = Path(self.file_path)
        if not path.exists():
            raise FileAccessError(path, "读取")
        if not path.is_file():
            raise InvalidFileError("通用", path, "路径指向目录而非文件")

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
        """提取图片列表"""
        pass