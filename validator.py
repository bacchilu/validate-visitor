#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
validator.py - https://github.com/bacchilu/validate-visitor

An example of encapsulating a validation logic inside an object
(sort of Visitor Design Pattern)


Luca Bacchi <bacchilu@gmail.com> - http://www.lucabacchi.it
"""


class ValidatorException(Exception):

    pass


class Validator(object):

    def __init__(self, data):
        self.data = data
        self.errorMsg = None
        self.errorCode = 0

    def checkEmpty(self):
        if len(self.data) == 0:
            self.errorCode = 1
            self.errorMsg = u'Non pu\xc3\xb2 essere vuoto'
            raise ValidatorException()

    def checkSize(self):
        if len(self.data) < 3:
            self.errorCode = 2
            self.errorMsg = u'Troppo corto'
            raise ValidatorException()
        if len(self.data) > 10:
            self.errorCode = 3
            self.errorMsg = u'Troppo lungo'
            raise ValidatorException()

    def checkWhitespace(self):
        if len([c for c in self.data if c.isspace()]) > 0:
            self.errorCode = 4
            self.errorMsg = u'Niente spazi'
            raise ValidatorException()

    def validate(self):
        try:
            self.checkEmpty()
            self.checkSize()
            self.checkWhitespace()
            return True
        except ValidatorException:
            return False


if __name__ == '__main__':
    v = Validator('Cai a ')
    if not v.validate():
        print (u'%s (%d)' % (v.errorMsg, v.errorCode)).encode('utf-8')
