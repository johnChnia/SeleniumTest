# -*- coding: utf-8 -*-
import os,sys,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lib.page.abstract_page import AbstractPage
class BugPage(AbstractPage):

	def get_bug_num(self):
		self.driver.get(self.base_url + "/bug-browse.html")
		num = self.driver.find_element_by_xpath(u'//*[@id="bugList"]/tfoot/tr/td/div[2]/div/strong[1]').text
		return int(num)


	def create_bug(self):
		self.driver.get(self.base_url + "/bug-browse.html")
		time.sleep(1)
		create_bug_btn = u'//*[@id="featurebar"]/div[1]/div[2]/a[2]'
		self.driver.find_element_by_xpath(create_bug_btn).click()
		time.sleep(3)

		self.driver.find_element_by_id("project_chosen").click()
		time.sleep(1)
		input_project = u'//*[@id="project_chosen"]/div/div/input'
		self.driver.find_element_by_xpath(input_project).send_keys('测试项目001'.decode('utf-8'))
		self.driver.find_element_by_xpath(input_project).send_keys(Keys.ENTER)
		time.sleep(1)

		self.driver.find_element_by_id("openedBuild_chosen").click()
		time.sleep(1)
		input_build = u'//*[@id="openedBuild_chosen"]/ul/li/input'
		self.driver.find_element_by_xpath(input_build).clear()
		self.driver.find_element_by_xpath(input_build).send_keys('Trunk')
		self.driver.find_element_by_xpath(input_build).send_keys(Keys.ENTER)
		time.sleep(1)

		self.driver.find_element_by_id("assignedTo_chosen").click()
		time.sleep(1)
		input_assign = u'//*[@id="assignedTo_chosen"]/div/div/input'
		self.driver.find_element_by_xpath(input_assign).clear()
		self.driver.find_element_by_xpath(input_assign).send_keys(self.rd_user['name'].decode('utf-8'))
		self.driver.find_element_by_xpath(input_assign).send_keys(Keys.ENTER)
		time.sleep(1)

		bug_title = "测试bug_" + time.strftime("%Y-%m-%d %H:%M:%S")
		self.driver.find_element_by_id('title').clear()
		self.driver.find_element_by_id('title').send_keys(bug_title.decode('utf-8'))
		#self.driver.find_element_by_id('title').send_keys(Keys.ENTER)
		time.sleep(1)

		self.driver.execute_script(r'scrollTo(0,3000)')
		actions = ActionChains(self.driver)
		actions.move_to_element(self.driver.find_element_by_id('submit')).click().perform()
		time.sleep(3)

	def assign_lastest_bug(self,user='大叔'):
		self.driver.get(self.base_url + "/bug-browse.html")
		time.sleep(1)
		self.driver.find_element_by_xpath(u'//*[@id="bugList"]/tbody/tr[1]/td[9]/a[1]').click()
		time.sleep(1)
		self.driver.switch_to_frame('modalIframe')
		self.driver.find_element_by_id("assignedTo_chosen").click()
		input_assign = u'//*[@id="assignedTo_chosen"]/div/div/input'
		self.driver.find_element_by_xpath(input_assign).clear()
		self.driver.find_element_by_xpath(input_assign).send_keys(user.decode('utf-8'))
		self.driver.find_element_by_xpath(input_assign).send_keys(Keys.ENTER)
		time.sleep(1)
		self.driver.find_element_by_id('submit').click()
		time.sleep(3)