from pathlib import Path
from src.parsers.pdf_parser import PDFParser
from src.parsers.docx_parser import DOCXParser
from src.parsers.html_parser import HTMLParser
from src.parsers.doc_parser import DOCParser
from src.parsers.djvu_parser import DJVUParser

def main():
    # 用户输入文件类型和路径
    file_type = input("请输入文件类型 (pdf, docx, html, doc, djvu): ").strip().lower()
    file_path = input("请输入文件路径: ").strip()

    # 根据文件类型选择相应的解析器
    parser = None

    if file_type == 'pdf':
        parser = PDFParser(Path(file_path))
    elif file_type == 'docx':
        parser = DOCXParser(Path(file_path))
    elif file_type == 'html':
        parser = HTMLParser(Path(file_path))
    elif file_type == 'doc':
        parser = DOCParser(Path(file_path))
    elif file_type == 'djvu':
        parser = DJVUParser(Path(file_path))
    else:
        print("不支持的文件类型！")
        return

    try:
        text = parser.extract_text()
        print("提取的文本:")
        print(text)

        if hasattr(parser, 'extract_metadata'):
            metadata = parser.extract_metadata()
            print("元数据:")
            print(metadata)

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()