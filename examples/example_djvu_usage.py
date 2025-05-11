from pathlib import Path
from src.parsers.djvu_parser import DJVUParser


def main():
    djvu_file = Path("C:/Users/zss/project_root/tests/data/valid/sample.djvu")  # замените на реальный путь

    parser = DJVUParser(djvu_file)

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