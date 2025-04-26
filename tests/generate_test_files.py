import os
import random
import string
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document

def random_string(length=10):
    """生成指定长度的随机字符串"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def create_valid_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    c.drawString(100, 750, f"This is a valid sample PDF file: {random_string()}.")
    c.save()

def create_invalid_pdf(file_path):
    with open(file_path, 'wb') as f:
        f.write(b'\x00\x00\x00')  # 写入损坏的数据

def create_valid_doc(file_path):
    with open(file_path, 'w') as f:
        f.write(f"This is a valid sample DOC file: {random_string()}.\n")  # 简单文本内容

def create_invalid_doc(file_path):
    with open(file_path, 'wb') as f:
        f.write(b'\x00\x00\x00')  # 写入损坏的数据

def create_valid_docx(file_path):
    doc = Document()
    doc.add_heading(f'Sample DOCX File: {random_string()}', level=1)
    doc.add_paragraph(f'This is a valid sample DOCX file: {random_string()}.')
    doc.save(file_path)

def create_invalid_docx(file_path):
    with open(file_path, 'wb') as f:
        f.write(b'\x00\x00\x00')  # 写入损坏的数据

def create_valid_html(file_path):
    with open(file_path, 'w') as f:
        f.write(f"<html><body><h1>This is a valid sample HTML file: {random_string()}.</h1></body></html>")

def create_invalid_html(file_path):
    with open(file_path, 'w') as f:
        f.write("<html><body><h1>This is an invalid HTML file.")  # 缺少闭合标签

def create_valid_djvu(file_path):
    # 创建一个简单的有效 DJVU 文件（这里使用的是空文件，您可以使用其他工具生成实际内容）
    with open(file_path, 'wb') as f:
        f.write(b'DJVU\x00\x01')  # 简单的 DJVU 文件头（不完整）

def create_invalid_djvu(file_path):
    with open(file_path, 'wb') as f:
        f.write(b'\x00\x00\x00')  # 写入损坏的数据

def generate_test_files(num_files=5):  # 添加参数以指定要创建的文件数量
    base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前脚本所在目录
    valid_dir = os.path.join(base_dir, "data", "valid")
    invalid_dir = os.path.join(base_dir, "data", "invalid")

    os.makedirs(valid_dir, exist_ok=True)
    os.makedirs(invalid_dir, exist_ok=True)

    for i in range(num_files):  # 循环以创建多个有效文件
        create_valid_pdf(os.path.join(valid_dir, f"sample_{i + 1}_{random_string(5)}.pdf"))
        create_valid_doc(os.path.join(valid_dir, f"sample_{i + 1}_{random_string(5)}.doc"))
        create_valid_docx(os.path.join(valid_dir, f"sample_{i + 1}_{random_string(5)}.docx"))
        create_valid_html(os.path.join(valid_dir, f"sample_{i + 1}_{random_string(5)}.html"))
        create_valid_djvu(os.path.join(valid_dir, f"sample_{i + 1}_{random_string(5)}.djvu"))

        # 创建无效文件
        create_invalid_pdf(os.path.join(invalid_dir, f"corrupted_{i + 1}_{random_string(5)}.pdf"))
        create_invalid_doc(os.path.join(invalid_dir, f"corrupted_{i + 1}_{random_string(5)}.doc"))
        create_invalid_docx(os.path.join(invalid_dir, f"corrupted_{i + 1}_{random_string(5)}.docx"))
        create_invalid_html(os.path.join(invalid_dir, f"corrupted_{i + 1}_{random_string(5)}.html"))
        create_invalid_djvu(os.path.join(invalid_dir, f"corrupted_{i + 1}_{random_string(5)}.djvu"))

if __name__ == "__main__":
    generate_test_files(num_files=10)  # 调用时指定要创建的文件数量