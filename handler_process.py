# -*- coding:utf8 -*-

import os

import docx

import config

import util

from pku_parser import PKUParser

class HandlerProcess(object):
    def __init__(self):
        self.doc = self.fetch_doc()
        self.paper = self.init_paper()
        self.parser = self.choose_parser()

    def choose_parser(self):
        if config.school == "pku":
            return PKUParser(self.doc, self.paper)
        elif config.school == "thu":
            raise Exception("thu is not support")
        else:
            raise Exception("other school should wait for update")

    def save_paper(self):
        """
            解析完成后保存论文
        """
        paper_path = os.path.join(config.file_path, config.paper_name + config.default_suffix)
        self.paper.save(paper_path)

    def init_paper(self):
        if config.paper_name.endswith(".doc") or config.paper_name.endswith(config.default_suffix):
            raise Exception("paper path cannot be end with")

        return docx.Document()

    def fetch_doc(self):
        src = os.path.join(config.file_path, config.file_name)
        if src.endswith(".doc"):
            dst = src.replace(".doc", config.default_suffix)
            util.convert_doc_to_docx(src, dst)
        elif src.endswith(config.default_suffix):
            dst = src
        else:
            raise Exception("file must be doc or docx type")

        return docx.Document(dst)

    def process(self):
        self.paper = self.parser.parse()
        self.save_paper()

handler_process = HandlerProcess()