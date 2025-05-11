# src/parsers/base_parser.py
from abc import ABC, abstractmethod
from pathlib import Path
from src.utils.exceptions import InvalidFileError, FileAccessError

class BaseParser(ABC):
    """
    Абстрактный базовый класс парсера документов
    """

    def __init__(self, file_path: str):
        """
        Инициализация экземпляра парсера
        :param file_path: Путь к файлу (строка)
        :raises FileAccessError: Ошибка доступа к файлу
        """
        self.file_path = file_path
        self._validate_file()

    def _validate_file(self):
        """
        Базовая проверка файла
        :raises FileAccessError: Файл не существует или недоступен
        """
        path = Path(self.file_path)
        if not path.exists():
            raise FileAccessError(path, "чтение")
        if not path.is_file():
            raise InvalidFileError("общий", path, "путь указывает на директорию")

    @abstractmethod
    def extract_text(self) -> str:
        """Извлечение текстового содержимого"""
        pass

    @abstractmethod
    def extract_metadata(self) -> dict:
        """Извлечение метаданных"""
        pass

    @abstractmethod
    def extract_images(self) -> list:
        """Извлечение списка изображений"""
        pass