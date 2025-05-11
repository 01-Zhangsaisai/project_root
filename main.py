import argparse
import sys
import traceback
from pathlib import Path
from src.core.file_processor import FileProcessor
from src.utils.exceptions import ParserException


def create_parser():
    """Создание парсера аргументов командной строки"""
    parser = argparse.ArgumentParser(
        prog="DocParser",
        description="Многоформатный анализатор документов v1.1",
        epilog="Пример: python main.py document.pdf -t pdf",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "file_path",
        type=str,
        help="Путь к анализируемому файлу\n(поддерживаются абсолютные и относительные пути)"
    )
    parser.add_argument(
        "-t", "--type",
        required=True,
        choices=["pdf", "docx", "html", "doc", "djvu"],
        help="Укажите тип формата документа\nДопустимые значения: pdf, docx, html, doc, djvu"
    )
    return parser


def main():
    """Основной процесс выполнения"""
    parser = create_parser()
    args = parser.parse_args()

    try:
        # Инициализация обработчика
        processor = FileProcessor(Path(args.file_path))

        # Выполнение процедуры анализа
        result = processor.process()

        # Безопасный вывод результатов
        print("\n✅ Анализ успешно завершен")
        print(f"Тип файла: {args.type.upper()}")
        print(f"Длина текста: {len(result.get('text', ''))} символов")
        print(f"Элементы метаданных: {len(result.get('metadata', {}))} записей")
        print(f"Извлеченные изображения: {len(result.get('images', []))} шт")

        print("\n================ СОДЕРЖАНИЕ ФАЙЛА ================")
        content = result.get('text', '')
        if isinstance(content, str) and len(content) > 0:
            print(content)
        elif isinstance(content, str) and "Ошибка извлечения" in content:
            print(f"❌ Ошибка извлечения содержимого: {content}")
        else:
            print("⚠️ Не обнаружено значимого текстового содержимого")

    except ParserException as e:
        print(f"\n❌ Ошибка анализа: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Системная ошибка: {e.__class__.__name__}")
        print(f"Подробная причина: {str(e)}")
        traceback.print_exc()
        sys.exit(2)


if __name__ == "__main__":
    main()