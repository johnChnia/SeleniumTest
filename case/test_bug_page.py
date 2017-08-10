# -*- coding: utf-8 -*-
import os,sys,unittest,time
from selenium import webdriver
from case.test_abstract import TestAbstract
from lib.base.driver_manager import DriverManager
from lib.page.bug_page import BugPage

class TestBugPage(TestAbstract):

	def test_create_bug(self):
		try:
			bug_page = BugPage(self.driver)
			bug_page.qa_login()
			old_num = bug_page.get_bug_num()
			bug_page.create_bug()
			new_num = bug_page.get_bug_num()
			self.assertEquals(1,new_num - old_num)
		except Exception as e:
			self.save_screenshot()
			self.fail(e.message)


	def test_assign_bug(self):
		try:
			bug_page = BugPage(self.driver)
			bug_page.qa_login()
			bug_page.assign_lastest_bug(user='小强')
		except Exception as e:
			self.save_screenshot()
			self.fail(e.message)






