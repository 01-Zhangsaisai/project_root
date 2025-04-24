# src/core/parser_factory.py

import mimetypes
from pathlib import Path

from src.parsers.pdf_parser import PDFParser
from src.parsers.html_parser import HTMLParser  
from src.parsers.djvu_parser import DJVUParser
from src.parsers.doc_parser import DOCParser
from src.parsers.docx_parser import DOCXParser

class ParserFactory:

    PARSERS = [
        PDFParser,
        HTMLParser,
        DJVUParser,
	DOCParser,
	DOCXParser,
    ]

    @staticmethod
    def get_parser(file_path: str):
        path_obj = Path(file_path)
        
        if not path_obj.exists() or not path_obj.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")

        mime_type, _ = mimetypes.guess_type(file_path)
        
        for parser_cls in ParserFactory.PARSERS:
            if mime_type in getattr(parser_cls, 'SUPPORTED_MIME_TYPES', []) or \
               path_obj.suffix.lower() in getattr(parser_cls, 'SUPPORTED_EXTENSIONS', []):
                return parser_cls(file_path)

        raise ValueError(f"No suitable parser found for file: {file_path}")