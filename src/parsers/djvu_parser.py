# src/parsers/djvu_parser.py
import subprocess
import fitz  # PyMuPDF
import os
from .base_parser import BaseParser
from src.utils.exceptions import InvalidDJVUException


class DJVUParser(BaseParser):
    SUPPORTED_MIME_TYPES = ['image/vnd.djvu']
    SUPPORTED_EXTENSIONS = ['.djvu']

    def __init__(self, file_path):
        self.file_path = file_path
        self.pdf_path = os.path.splitext(file_path)[0] + ".pdf"

        # 转换 DJVU 到 PDF
        subprocess.run([
            "ddjvu",
            "-format=pdf",
            self.file_path,
            self.pdf_path
        ], check=True)

    def extract_text(self) -> str:
        """从 PDF 提取文本"""
        doc = fitz.open(self.pdf_path)
        text = "".join([page.get_text() for page in doc])
        doc.close()
        return text

    def extract_metadata(self) -> dict:
        """从 PDF 提取元数据"""
        doc = fitz.open(self.pdf_path)
        metadata = {
            "title": doc.metadata.get("title", "Unknown"),
            "author": doc.metadata.get("author", "Unknown"),
            "num_pages": doc.page_count
        }
        doc.close()
        return metadata

    def extract_images(self, output_dir: str) -> list:
        """从 PDF 提取图像"""
        doc = fitz.open(self.pdf_path)
        images = []
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_path = os.path.join(output_dir, f"page_{page_num + 1}_img_{img_index}.{base_image['ext']}")
                with open(image_path, "wb") as f:
                    f.write(base_image["image"])
                images.append(image_path)
        doc.close()
        return images