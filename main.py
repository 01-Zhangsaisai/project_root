# main.py
"""
命令行主入口模块
"""
import argparse
import sys
import traceback
from pathlib import Path
from src.core.file_processor import FileProcessor
from src.utils.exceptions import ParserException

def create_parser():
    """创建命令行参数解析器"""
    parser = argparse.ArgumentParser(
        prog="DocParser",
        description="多格式文档解析工具 v1.1",
        epilog="示例: python main.py document.pdf -t pdf",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "file_path",
        type=str,
        help="需要解析的文件路径\n(支持绝对路径和相对路径)"
    )
    parser.add_argument(
        "-t", "--type",
        required=True,
        choices=["pdf", "docx", "html", "doc", "djvu"],
        help="指定文档格式类型\n可选值：pdf, docx, html, doc, djvu"
    )
    return parser

def main():
    """主执行流程"""
    parser = create_parser()
    args = parser.parse_args()

    try:
        # 初始化处理器
        processor = FileProcessor(Path(args.file_path))

        # 执行解析操作
        result = processor.process()

        # 安全输出结果
        print("✅ 解析成功")
        print(f"文件类型: {args.type.upper()}")
        print(f"文本长度: {len(result.get('text', ''))}字符")
        print(f"元数据项: {len(result.get('metadata', {}))}条")
        print(f"图片数量: {len(result.get('images', []))}张")

    except ParserException as e:
        print(f"❌ 解析错误: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 系统错误: {e.__class__.__name__}")
        print(f"详细原因: {str(e)}")
        traceback.print_exc()  # 打印完整堆栈
        sys.exit(2)

if __name__ == "__main__":
    main()