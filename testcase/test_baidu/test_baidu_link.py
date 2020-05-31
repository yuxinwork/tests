#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import  webdriver
import  unittest

class BaiudLink(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.get('http://www.baidu.com')
	
	#@unittest.skip('忽略该测试用例的执行')
	def tearDown(self):
		self.driver.quit()

	def test_baidu_news(self):
		
		'''首页测试:点击新闻是否可正常的跳转'''
		self.driver.find_element_by_link_text('新闻').click()
		self.assertEqual(self.driver.current_url,'http://news.baidu.com')
		# self.driver.back()

	def test_baidu_map(self):
		'''首页测试:点击地图是否可正常的跳转'''
		self.driver.find_element_by_link_text('地图').click()
		self.assertEqual(self.driver.current_url,' https://map.baidu.com')
		# self.driver.back()
if __name__ == '__main__':
    unittest.main(verbosity=2)