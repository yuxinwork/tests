
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver


class f4(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(30)
		cls.driver.get('https://www.nubia.com/cn/')
	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
	
	'''测试nubia首页链接'''
	
	def test_user_001(self):
		'''首页链接测试: 验证机型play的链接'''
		self.driver.find_element_by_link_text('Play').click()
		# print(self.driver.current_url)
		self.assertEqual(self.driver.current_url,'https://www.nubia.com/nubiaPlay?a=show.product.show')
		self.driver.back()
	
	def test_uesr_002(self):
		'''首页链接测试：验证机型Z系列链接'''
		self.driver.find_element_by_partial_link_text('Z').click()
		self.assertEqual(self.driver.current_url, 'https://www.nubia.com/phone/z')
		self.driver.back()
	#
	# def test_uesr_003(self):
	# 	'''首页链接测试：验证机型红魔系列链接'''
	# 	self.driver.find_element_by_partial_link_text('魔').click()
	# 	self.driver.back()
	#
	# def test_user_004(self):
	# 	'''首页链接测试: 验证智能生态链接'''
	# 	self.driver.find_element_by_partial_link_text('态').click()
	# 	self.driver.back()
	#
	# def test_uesr_005(self):
	# 	'''首页链接测试：验证品牌链接'''
	# 	self.driver.find_element_by_partial_link_text('牌').click()
	# 	self.driver.back()
	#
	# def test_uesr_006(self):
	# 	'''首页链接测试：验证品牌链接'''
	# 	self.driver.find_element_by_partial_link_text('品').click()
	# 	self.driver.back()
	#
	# def test_uesr_007(self):
	# 	'''首页链接测试：验证服务链接'''
	# 	self.driver.find_element_by_partial_link_text('服务').click()
	# 	self.driver.back()
	#
	# def test_uesr_008(self):
	# 	'''首页链接测试：验证社区链接'''
	# 	self.driver.find_element_by_partial_link_text('区').click()
	# 	self.driver.back()
	#
	# def test_uesr_009(self):
	# 	'''首页链接测试：验证体验店链接'''
	# 	self.driver.find_element_by_partial_link_text('店').click()
	# 	self.driver.back()


if __name__ == '__main__':
	unittest.main(verbosity=2)