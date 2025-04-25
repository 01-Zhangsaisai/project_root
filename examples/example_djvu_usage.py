from pathlib import Path
from src.parsers.djvu_parser import DJVUParser

def main():
    djvu_file = Path("C:/Users/zss/project_root/tests/data/valid/sample.djvu")  # 替换为实际路径
    
    parser = DJVUParser(djvu_file)
    
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