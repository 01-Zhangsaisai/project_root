from pathlib import Path
from src.parsers.doc_parser import DOCParser


def main():
    doc_file = Path("C:/Users/zss/project_root/tests/data/valid/sample.doc")  # замените на реальный путь

    parser = DOCParser(doc_file)

    try:
        text = parser.extract_text()
        print("Извлеченный текст:")
        print(text)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()