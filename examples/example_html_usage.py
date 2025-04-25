from pathlib import Path
from src.parsers.html_parser import HTMLParser

def main():
    html_file = Path("C:/Users/zss/project_root/tests/data/valid/sample.html")  # 替换为实际路径
    
    parser = HTMLParser(html_file)
    
    try:
        text = parser.extract_text()
        print("Extracted Text:")
        print(text)
        
        metadata = parser.extract_metadata()
        print("Metadata:")
        print(metadata)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()