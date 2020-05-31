#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import time

import HTMLTestRunner

def allTest():
	suite=unittest.TestLoader().discover(
		start_dir=os.path.dirname(__file__),
		pattern='test_*.py',
		top_level_dir=None)
	return suite
# print(allTest())

# def run():
#执行所有测试用例
# 	unittest.TextTestRunner(verbosity=2).run(allTest())
# if __name__=='__main__':
# 	run()
	

#生成测试报告的方法
def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def run():
	fp=os.path.join(os.path.dirname(__file__),'report',getNowTime()+'testReport.html')
	HTMLTestRunner.HTMLTestRunner(
		stream=open(fp,'wb'),
		title='自动化测试报告',
		description='自动化测试报告详细信息').run(allTest())

if __name__ == '__main__':
	run()
	