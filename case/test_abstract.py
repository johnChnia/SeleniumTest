# -*- coding: utf-8 -*-
import os,sys,unittest,time
sys.path.append('E:/python_resources/code/test_zentao')
from lib.base.util import Util
from selenium import webdriver
from lib.base.driver_manager import DriverManager

class TestAbstract(unittest.TestCase):
	driver=None
	type=None
	config_file = os.path.dirname(os.path.dirname(__file__)) + '/conf/base.conf'

	@classmethod
	def setUpClass(clz):
		pass

	def setUp(self):
		self.driver = DriverManager.getDriver(self.type)

	def tearDown(self):
		self.driver.quit()

	@classmethod
	def tearDownClass(clz):
		pass

	def save_screenshot(self):
		dir_screenshot = Util.getConfig(self.config_file,'test','dir_screenshot')
		file_name = dir_screenshot + '/' + self.__class__.__name__ + '-' + self._testMethodName + '.png'
		self.driver.save_screenshot(file_name)







