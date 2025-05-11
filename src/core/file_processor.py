# src/core/file_processor.py
"""
Основной модуль обработки файлов
"""
from pathlib import Path
from typing import Dict, Any
from src.parsers.parser_factory import ParserFactory
from src.utils.exceptions import ParserException


class FileProcessor:
    """
    Обработчик файлов
    Функционал: координация процесса парсинга, обработка исключений
    """

    def __init__(self, file_path: Path):
        """
        Инициализация обработчика файлов
        :param file_path: Объект пути к файлу
        :raises FileNotFoundError: Файл не существует
        """
        if not file_path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        self.file_path = file_path

    def process(self) -> Dict[str, Any]:
        """
        Безопасное выполнение процесса парсинга
        :return: Стандартизированный словарь результатов
        :raises ParserException: Ошибки парсинга
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
        Безопасное выполнение операции извлечения
        :param func: Метод извлечения
        :return: Результат извлечения или сообщение об ошибке
        """
        try:
            return func()
        except Exception as e:
            return f"Ошибка извлечения: {e.__class__.__name__}"