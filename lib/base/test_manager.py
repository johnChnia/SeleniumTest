# -*- coding: utf-8 -*-

import unittest


class TestManager:
    @staticmethod
    def getTest(clz, type):
        new_classname = str(clz.__name__) + '_' + str(type).capitalize()
        new_clz = type(new_classname, (clz,), {'type': type})
        return unittest.makeSuite(new_clz)
