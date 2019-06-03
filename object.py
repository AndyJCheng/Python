#!/usr/bin/env python
# encoding: utf-8

"""
@author: Andy Cheng
@license: Apache Licence 
@file: object.py
@time: 2019/6/3 23:34
"""


class Document:
    WELCOME_STR = 'WELCOME PYTHON {}'

    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.__content = content

    def get_content_length(self):
        return len(self.__content)

    def intercept_content(self, length):
        return self.__content[:length]

    @classmethod
    def create_book(cls, title, author):
        return cls(title=title, author=author, content='nothing')

    @staticmethod
    def get_welcome(content):
        return Document.WELCOME_STR.format(content)





