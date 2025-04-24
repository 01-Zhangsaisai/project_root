# src/core/file_processor.py

from .parser_factory import ParserFactory


class FileProcessor:

    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def process(self) -> dict:
        parser = ParserFactory.get_parser(self.file_path)
        
        text = parser.extract_text()
        metadata = parser.extract_metadata()
        
        images = parser.extract_images()
        
        return {
            "text": text,
            "metadata": metadata,
            "images": images,
        }