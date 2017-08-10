# -*- coding: utf-8 -*-
import os
from selenium import webdriver


class DriverManager:
    type = 'chrome'

    @staticmethod
    def getType():
        return DriverManager.type

    @staticmethod
    def setType(type):
        DriverManager.type = type

    @staticmethod
    def getDriver(type=None):
        driver = None
        if (None == type):
            type = DriverManager.getType()
        if (type == "chrome"):
            driver = webdriver.Chrome()
        elif (type == "firefox"):
            driver = webdriver.Firefox()
        elif (type == "ie"):
            driver = webdriver.Ie()
        else:
            raise Exception("ERROR____: unknown driver type:" + str(type))
        driver.implicitly_wait(30)
        driver.delete_all_cookies()
        driver.maximize_window()
        return driver
