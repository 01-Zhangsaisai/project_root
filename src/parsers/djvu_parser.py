# src/parsers/djvu_parser.py

from pydjvu import DjVuDocument  # pip install pydjvu
from .base_parser import BaseParser
from src.utils.exceptions import InvalidDJVUException

class DJVUParser(BaseParser):
    
    SUPPORTED_MIME_TYPES = ['image/vnd.djvu']
    SUPPORTED_EXTENSIONS = ['.djvu']

    def __init__(self, file_path):
        """初始化 DJVUParser 实例。

        Args:
            file_path (str): DJVU 文件的路径。
        """
        self.file_path = file_path

    def extract_text(self) -> str:
        """从 DJVU 文件中提取文本。

        Returns:
            str: 提取的文本内容。

        Raises:
            InvalidDJVUException: 如果无法提取文本。
        """
        document = DjVuDocument(self.file_path)
        text = ""
        for page in document.pages:
            text += page.text + "\n"
        return text.strip()

    def extract_metadata(self) -> dict:
        """从 DJVU 文件中提取元数据。

        Returns:
            dict: 包含标题、作者和页数的元数据字典。

        Raises:
            InvalidDJVUException: 如果无法提取元数据。
        """
        document = DjVuDocument(self.file_path)
        metadata = {
            "title": document.title,
            "author": document.author,
            "num_pages": len(document.pages)
        }
        return metadata

    def extract_images(self, output_dir: str) -> list:
        """从 DJVU 文件中提取图像并保存到指定目录。

        Args:
            output_dir (str): 图像保存的目录路径。

        Returns:
            list: 保存的图像文件路径列表。

        Raises:
            InvalidDJVUException: 如果无法提取图像。
        """
        images = []
        document = DjVuDocument(self.file_path)
        
        for i, page in enumerate(document.pages):
            image_path = f"{output_dir}/page_{i + 1}.png"  # 保存每一页为图像
            page.save_image(image_path)  # 保存图像（根据需要调整）
            images.append(image_path)
        
        return images