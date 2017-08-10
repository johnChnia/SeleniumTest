#coding:utf-8
import os,shutil
import unittest
import xmlrunner
from lib.base.util import Util
from lib.base.test_manager import TestManager
from case.test_bug_page import TestBugPage
from case.test_doc_page import TestDocPage

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(TestManager.getTest(TestBugPage,'chrome'))
	suite.addTest(TestManager.getTest(TestDocPage,'chrome'))

	suite.addTest(TestManager.getTest(TestBugPage,'firefox'))
	suite.addTest(TestManager.getTest(TestDocPage,'firefox'))

	suite.addTest(TestManager.getTest(TestBugPage,'ie'))
	suite.addTest(TestManager.getTest(TestDocPage,'ie'))

	dir_screenshot = Util.getConfig('conf/base.conf','test','dir_screenshot')
	if(os.path.exists(dir_screenshot)):
		shutil.rmtree(dir_screenshot)
	os.mkdir(dir_screenshot)

	if(os.path.exists(os.path.dirname(__file__) + '/test-reports')):
		shutil.rmtree(os.path.dirname(__file__) + '/test-reports')
	runner = xmlrunner.XMLTestRunner(output='test-reports',verbose = 1)
	#runner = unittest.TextTestRunner(verbosity = 1)
	runner.run(suite)

