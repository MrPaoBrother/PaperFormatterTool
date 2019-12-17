# -*- coding:utf8 -*-
from win32com import client

def convert_doc_to_docx(src, dst):
    """
        将doc转化成docx
    """
    word = client.Dispatch('Word.Application')
    doc = word.Documents.Open(src)
    doc.SaveAs(dst, 16)
    doc.Close()
    word.Quit()