#!/usr/bin/env python
# -*- coding: utf-8 -*-

# !/usr/bin/env python
# -*- coding: utf-8 -*-

# import unittest
# import sys
# import os

# os.path.dirname(__file__)
# # sys.path.append('..')
# from Init.init import *

import unittest
from selenium import webdriver


class f4(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('https://www.nubia.com/cn/')
		
# class NubiaLink(Init):
	def test_nubia_001(self):
		print(self.driver.title, type(self.driver.title))
		'''判断title是否是努比亚手机-官方网站'''
		self.assertEqual(self.driver.title, '努比亚手机-官方网站')


# def test_nubai_002(self):
# 	self.assertEqual()

if __name__ == '__main__':
	unittest.main(verbosity=2)
