# src/parsers/djvu_parser.py
import subprocess
import os
import fitz
from pathlib import Path
from .base_parser import BaseParser
from src.utils.exceptions import InvalidFileError, FileAccessError


class DJVUParser(BaseParser):
    """
    Парсер документов DjVu
    Поддерживаемые форматы: image/vnd.djvu, .djvu
    """

    SUPPORTED_MIME_TYPES = ['image/vnd.djvu']
    SUPPORTED_EXTENSIONS = ['.djvu']

    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.pdf_path = None
        self._validate_file()
        self.pdf_path = self._convert_to_pdf()

    def _validate_file(self):
        super()._validate_file()
        path = Path(self.file_path)
        with open(path, 'rb') as f:
            header = f.read(4)

            if header not in [b'FORM', b'AT&T', b'DJVI']:
                raise InvalidFileError(
                    "djvu",
                    path,
                    "неверный формат файла (ожидался заголовок 'FORM')"
                )

    def _convert_to_pdf(self) -> str:
        abs_file_path = str(Path(self.file_path).absolute())
        pdf_path = Path(self.file_path).with_suffix('.pdf')
        abs_pdf_path = str(pdf_path.absolute())

        subprocess.run(
            ["ddjvu", "-format=pdf", abs_file_path, abs_pdf_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if not Path(abs_pdf_path).exists():
            raise InvalidFileError(
                "djvu",
                Path(self.file_path),
                "не удалось создать PDF-файл"
            )

        return abs_pdf_path

    def extract_text(self) -> str:
        try:
            result = subprocess.run(
                ["djvutxt", self.file_path],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                check=True
            )
            return result.stdout.strip() or "⚠️ Текст не обнаружен"
        except Exception as e:
            try:
                if not Path(self.pdf_path).exists():
                    raise FileNotFoundError(f"PDF файл не найден: {self.pdf_path}")

                with fitz.open(self.pdf_path) as doc:
                    return "\n".join(page.get_text() for page in doc)
            except Exception:
                raise FileAccessError(Path(self.file_path), "извлечение текста") from e

    def extract_metadata(self) -> dict:
        try:
            with fitz.open(self.pdf_path) as doc:
                return dict(doc.metadata)
        except Exception as e:
            raise FileAccessError(Path(self.file_path), "извлечение метаданных") from e

    def extract_images(self) -> list:
        images = []
        try:
            with fitz.open(self.pdf_path) as doc:
                for page in doc:
                    images.extend(doc.extract_image(img[0])["image"] for img in page.get_images())
        except Exception as e:
            raise FileAccessError(Path(self.file_path), "извлечение изображений") from e
        return images

    def __del__(self):
        if hasattr(self, "pdf_path") and self.pdf_path and os.path.exists(self.pdf_path):
            try:
                os.remove(self.pdf_path)
            except Exception:
                pass