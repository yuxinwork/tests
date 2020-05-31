#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import  webdriver
import  unittest

class BaiudLink(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.get('http://www.baidu.com')

	def tearDown(self):
		self.driver.quit()

	def test_baidu_so_enabled(self):
		'''首页：百度搜索输入框可编辑'''
		so=self.driver.find_element_by_id('kw')
		self.assertTrue(so.is_enabled())

	def test_baidu_so(self):
		'''首页:测试百度的搜索功能'''
		so=self.driver.find_element_by_id('kw')
		so.send_keys('webdriver')
		self.driver.find_element_by_id('su').click()
		self.assertEqual(so.get_attribute('value'),'webdriver')

if __name__ == '__main__':
    unittest.main(verbosity=2)