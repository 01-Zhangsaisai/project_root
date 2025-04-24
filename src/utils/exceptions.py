# src/utils/exceptions.py

class ParserException(Exception):
    """所有解析异常的基类"""
    pass

class InvalidPDFException(ParserException):
    """无效或损坏的PDF文件异常"""
    pass

class InvalidHTMLException(ParserException):
    """无效或损坏的HTML文件异常"""
    pass

class InvalidDOCXException(ParserException):
    """无效或损坏的DOCX文件异常"""
    pass

class InvalidDOCException(ParserException):
    """无效或损坏的DOC文件异常"""
    pass

class InvalidDJVUException(ParserException):
    """无效或损坏的DJVU文件异常"""
    pass

