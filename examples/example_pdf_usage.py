from pathlib import Path
from src.parsers.pdf_parser import PDFParser


def main():
    pdf_file = Path("C:/Users/zss/project_root/tests/data/valid/sample.pdf")  # замените на реальный путь

    parser = PDFParser(pdf_file)

    try:
        text = parser.extract_text()
        print("Извлеченный текст:")
        print(text)

        metadata = parser.extract_metadata()
        print("Метаданные:")
        print(metadata)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()