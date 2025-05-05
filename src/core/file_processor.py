# src/core/file_processor.py
"""
文件处理核心模块
"""
from pathlib import Path
from typing import Dict, Any
from src.parsers.parser_factory import ParserFactory
from src.utils.exceptions import ParserException

class FileProcessor:
    """
    文件处理器
    功能：协调解析流程，处理异常
    """
    
    def __init__(self, file_path: Path):
        """
        初始化文件处理器
        :param file_path: 文件路径对象
        :raises FileNotFoundError: 文件不存在
        """
        if not file_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")
        self.file_path = file_path

    def process(self) -> Dict[str, Any]:
        """
        安全执行解析流程
        :return: 标准化结果字典
        :raises ParserException: 解析相关错误
        """
        try:
            parser = ParserFactory.get_parser(self.file_path)
            return {
                "text": self._safe_extract(parser.extract_text),
                "metadata": self._safe_extract(parser.extract_metadata),
                "images": self._safe_extract(parser.extract_images)
            }
        except Exception as e:
            raise ParserException(str(e)) from e

    def _safe_extract(self, func: callable) -> Any:
        """
        安全执行提取操作
        :param func: 提取方法
        :return: 提取结果或错误信息
        """
        try:
            return func()
        except Exception as e:
            return f"提取失败: {e.__class__.__name__}"