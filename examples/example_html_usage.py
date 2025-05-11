from pathlib import Path
from src.parsers.html_parser import HTMLParser


def main():
    html_file = Path("C:/Users/zss/project_root/tests/data/valid/sample.html")  # замените на реальный путь

    parser = HTMLParser(html_file)

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