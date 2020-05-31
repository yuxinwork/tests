#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest
import time as t
from selenium import webdriver

driver = webdriver.Chrome()


def test_nubia_title(selenium):
	'''nubia title'''
	selenium.get('https://www.nubia.com/cn/')
	# assert selenium.title=='努比亚手机-官方网站'
	print(driver.title)


def test_nubia_login_001(selenium):
	'''账户名密码都为空'''
	selenium.get('https://account.nubia.com/profile/login?back_url=https%3A%2F%2Fwww.nubia.com%2Forder%2Fmember')
	selenium.find_element_by_id('username').send_keys('')
	t.sleep(2)
	selenium.find_element_by_id('password').send_keys('')
	t.sleep(2)
	selenium.find_element_by_partial_link_text('立即登录')
	div = selenium.find_element_by_xpath('//*[@id="login_confirm_voice_not_clear"]').text
	assert div == '请输入邮箱/手机号码/用户名'


def test_nubia_login_002(selenium):
	'''密码为空'''
	selenium.get('https://account.nubia.com/profile/login?back_url=https%3A%2F%2Fwww.nubia.com%2Forder%2Fmember')
	selenium.find_element_by_id('username').send_keys('testing')
	t.sleep(2)
	selenium.find_element_by_id('password').send_keys('')
	t.sleep(2)
	selenium.find_element_by_partial_link_text('立即登录').click
	div = selenium.find_element_by_xpath('//*[@id="login_confirm_voice_not_clear"]').text
	assert div == '请输入密码'