# src/parsers/parser_factory.py
import mimetypes
from pathlib import Path
from src.utils.exceptions import ParserException
from .pdf_parser import PDFParser
from .docx_parser import DOCXParser
from .html_parser import HTMLParser
from .doc_parser import DOCParser
from .djvu_parser import DJVUParser


class ParserFactory:
    """
    解析器工厂类（修正版）
    功能：根据文件类型返回正确的解析器实例
    """

    _registry = {
        # 格式: (MIME类型, 扩展名, 解析器类)
        'pdf': ('application/pdf', '.pdf', PDFParser),
        'docx': ('application/vnd.openxmlformats-officedocument.wordprocessingml.document', '.docx', DOCXParser),
        'html': ('text/html', '.html', HTMLParser),
        'djvu': ('image/vnd.djvu', '.djvu', DJVUParser),
        'doc': ('application/msword', '.doc', DOCParser)
    }

    @staticmethod
    def get_parser(file_path: Path) -> object:
        """
        安全获取解析器实例
        :param file_path: 文件路径对象
        :return: 初始化后的解析器实例
        """
        try:
            # 获取文件特征
            mime_type, _ = mimetypes.guess_type(str(file_path))
            suffix = file_path.suffix.lower()

            # 双重匹配逻辑
            for fmt, (mime, ext, parser_cls) in ParserFactory._registry.items():
                if mime_type == mime or suffix == ext:
                    return parser_cls(str(file_path))

            raise ParserException(f"不支持 {suffix} 格式")

        except KeyError as e:
            raise ParserException(f"解析器配置错误: {str(e)}") from e