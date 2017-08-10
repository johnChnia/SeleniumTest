# -*- coding: utf-8 -*-
import os,time,sys
#sys.path.append('E:/python_resources/code/test_zentao')
from lib.base.util import Util

class AbstractPage(object):
	driver = None
	config_file = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/conf/base.conf'
	base_url = ""
	qa_user = {}
	rd_user = {}
	admin_user = {}

	def __init__(self,driver):
		self.driver = driver
		self.base_url = Util.getConfig(self.config_file,'zentao','url')
		self.admin_user = self.get_user('admin')
		self.qa_user = self.get_user('qa')
		self.rd_user = self.get_user('rd')

	def login(self,username,password):
		self.driver.get(self.base_url + "/user-login.html")
		self.driver.find_element_by_id('account').clear()
		self.driver.find_element_by_id('account').send_keys(username)
		self.driver.find_element_by_name('password').clear()
		self.driver.find_element_by_name('password').send_keys(password)
		self.driver.find_element_by_id('keepLoginon').click()
		time.sleep(1)
		self.driver.find_element_by_id('submit').click()


	def admin_login(self):
		self.login(self.admin_user['username'],self.admin_user['password'])

	def qa_login(self):
		self.login(self.qa_user['username'],self.qa_user['password'])

	def rd_login(self):
		self.login(self.rd_user['username'],self.rd_user['password'])

	def get_user(self,type='admin'):
		user = {}
		user['username'] = Util.getConfig(self.config_file,'zentao',type+"_user")
		user['password'] = Util.getConfig(self.config_file,'zentao',type+"_pswd")
		user['name'] = Util.getConfig(self.config_file,'zentao',type+"_name")
		return user