# -*- coding: utf-8 -*-
import os, sys, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lib.page.abstract_page import AbstractPage


class DocPage(AbstractPage):
    def get_doc_num(self):
        self.driver.get(self.base_url + "/doc-browse.html")
        time.sleep(1)
        num = self.driver.find_element_by_xpath(u'//*[@id="docList"]/tfoot/tr/td/div/strong[1]').text
        return int(num)

    def create_doc(self):
        self.driver.get(self.base_url + "/doc-browse.html")
        time.sleep(1)
        create_doc_btn = u'//*[@id="featurebar"]/div[1]/a'
        self.driver.find_element_by_xpath(create_doc_btn).click()
        time.sleep(3)

        doc_title = "测试doc_" + time.strftime("%Y-%m-%d %H:%M:%S")
        self.driver.find_element_by_id('title').clear()
        self.driver.find_element_by_id('title').send_keys(doc_title.decode('utf-8'))
        time.sleep(1)

        if self.driver.name == 'internet explorer':
            self.driver.find_element_by_xpath(u'//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').click()
            os.system(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/data/upload/doc_ie.exe')
        elif self.driver.name == 'firefox':
            self.driver.find_element_by_xpath(u'//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').click()
            os.system(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/data/upload/doc_firefox.exe')
        else:
            file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/data/upload/a.doc'
            self.driver.find_element_by_xpath(u'//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').send_keys(file_path)
        time.sleep(1)

        self.driver.execute_script(r'scrollTo(0,3000)')
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_id('submit')).click().perform()
        time.sleep(3)
