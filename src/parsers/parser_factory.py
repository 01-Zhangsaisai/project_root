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

    _registry = {
        # Формат: (MIME-тип, расширение, класс парсера)
        'pdf': ('application/pdf', '.pdf', PDFParser),
        'docx': ('application/vnd.openxmlformats-officedocument.wordprocessingml.document', '.docx', DOCXParser),
        'html': ('text/html', '.html', HTMLParser),
        'djvu': ('image/vnd.djvu', '.djvu', DJVUParser),
        'doc': ('application/msword', '.doc', DOCParser)
    }

    @staticmethod
    def get_parser(file_path: Path) -> object:
        """
        Безопасное создание парсера
        :param file_path: Объект пути к файлу
        :return: Инициализированный экземпляр парсера
        """
        try:
            # Определение характеристик файла
            mime_type, _ = mimetypes.guess_type(str(file_path))
            suffix = file_path.suffix.lower()

            # Двойная проверка соответствия
            for fmt, (mime, ext, parser_cls) in ParserFactory._registry.items():
                if mime_type == mime or suffix == ext:
                    return parser_cls(str(file_path))

            raise ParserException(f"Формат {suffix} не поддерживается")

        except KeyError as e:
            raise ParserException(f"Ошибка конфигурации парсера: {str(e)}") from e