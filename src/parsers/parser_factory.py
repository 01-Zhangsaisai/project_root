import mimetypes
from pathlib import Path
from src.utils.exceptions import ParserException
from .pdf_parser import PDFParser
from .docx_parser import DOCXParser
from .html_parser import HTMLParser
from .doc_parser import DOCParser
from .djvu_parser import DJVUParser


class ParserFactory:
    _registry = [
        {
            "mime_types": ['application/pdf'],
            "extensions": ['.pdf'],
            "parser_cls": PDFParser
        },
        {
            "mime_types": ['application/vnd.openxmlformats-officedocument.wordprocessingml.document'],
            "extensions": ['.docx'],
            "parser_cls": DOCXParser
        },
        {
            "mime_types": ['application/msword'],
            "extensions": ['.doc'],
            "parser_cls": DOCParser
        },
        {
            "mime_types": ['text/html', 'application/xhtml+xml'],
            "extensions": ['.html', '.htm'],
            "parser_cls": HTMLParser
        },
        {
            "mime_types": ['image/vnd.djvu'],
            "extensions": ['.djvu'],
            "parser_cls": DJVUParser
        }
    ]

    @staticmethod
    def get_parser(file_path: Path) -> object:
        """
        Безопасное создание парсера
        :param file_path: Объект пути к файлу
        :return: Инициализированный экземпляр парсера
        """
        try:
            mime_type, _ = mimetypes.guess_type(str(file_path))
            suffix = file_path.suffix.lower()

            for item in ParserFactory._registry:
                if (mime_type and mime_type in item["mime_types"]) or suffix in item["extensions"]:
                    return item["parser_cls"](str(file_path))

            raise ParserException(f"Формат {suffix} не поддерживается")
        except Exception as e:
            raise ParserException(f"Ошибка конфигурации парсера: {str(e)}") from e
