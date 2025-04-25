from pathlib import Path
from src.parsers.doc_parser import DOCParser

def main():
    doc_file = Path("C:/Users/zss/project_root/tests/data/valid/sample.doc")  # 替换为实际路径
    
    parser = DOCParser(doc_file)
    
    try:
        text = parser.extract_text()
        print("Extracted Text:")
        print(text)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()