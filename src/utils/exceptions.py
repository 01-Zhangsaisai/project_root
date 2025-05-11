# src/utils/exceptions.py
from pathlib import Path

class ParserException(Exception):
    def __init__(self, msg: str, file_path: Path = None):
        self.file_path = file_path
        self.msg = f"[{file_path}] {msg}" if file_path else msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg

class FileValidationError(ParserException):
    pass

class FileAccessError(ParserException):
    def __init__(self, file_path: Path, operation: str):
        super().__init__(
            f"Ошибка доступа к файлу: Невозможно выполнить {operation} ({file_path})",
            file_path
        )

class InvalidFileError(FileValidationError):
    def __init__(self, file_type: str, file_path: Path, reason: str):
        super().__init__(
            f"Некорректный {file_type.upper()} файл ({reason})",
            file_path
        )