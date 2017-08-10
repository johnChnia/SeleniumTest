# -*- coding: utf-8 -*-
import os, sys, unittest, time
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from case.test_abstract import TestAbstract
from lib.page.doc_page import DocPage


class TestDocPage(TestAbstract):
    def test_create_doc(self):
        try:
            doc_page = DocPage(self.driver)
            doc_page.qa_login()
            old_num = doc_page.get_doc_num()
            doc_page.create_doc()
            new_num = doc_page.get_doc_num()
            self.assertEquals(1, new_num - old_num)
        except Exception as  e:
            print(e)
            self.save_screenshot()
            self.fail(e.message)
