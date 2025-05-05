# Project Root

## Introduction  
This project provides document analysis functionality for multiple formats, including PDF, DOCX, HTML, DOC, and DJVU files.  

---

## Environment Requirements  
Ensure the following software is installed on your system:  
- **Python 3.8+**  
- **Required Libraries** (see `requirements.txt`)  

---

## Installation Guide  

### 1. Clone the Repository  
```bash  
git clone https://github.com/01-Zhangsaisai/project_root.git  
cd project_root
``` 
### 2. Install Dependencies
```bash
pip install -r requirements.txt 
``` 

Usage Instructions
Command-Line Execution
Run the program with the following syntax:

```bash
python main.py <file_path> -t <file_type> 
``` 
Arguments:
<file_path>: Absolute or relative path to the document.

-t/--type: Document type (pdf, docx, html, doc, djvu).

Example:
```bash
python main.py "tests/data/valid/sample.pdf" -t pdf  
```
Output
Successful parsing will display:

text
✅ Parsing succeeded  
File Type: PDF  
Text Length: 1500 characters  
Metadata Items: 3 entries  
Images Extracted: 2  
Key Files
main.py: Entry point for document parsing.

README.md: Updated with installation, usage, and troubleshooting details.

Troubleshooting
Dependency Issues: Reinstall using pip install -r requirements.txt.

File Access Errors: Ensure the path is correct and the file is not locked.

Unsupported Formats: Verify the file type matches the registered parsers.
