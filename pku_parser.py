# -*- coding:utf8 -*-
class PKUParser(object):
    def __init__(self, doc, paper):
        self.doc = doc
        self.paper = paper
    
    def format_head(self):
        """
            格式化头部
        """
        pass

    def format_content(self):
        pass

    def format_tail(self):
        pass

    def parse(self):
        self.format_head()
        self.format_content()
        self.format_tail()

        return self.paper