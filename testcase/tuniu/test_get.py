#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import unittest

r=requests.get(url='https://api.tuniu.com/hotel/hotel/detail?c=%7b%22cc%22%3a1602%2c%22ct%22%3a10%2c%22p%22%3a14588%2c%22ov%22%3a20%2c%22dt%22%3a0%2c%22v%22%3a%2210.23.0%22%7d&d=%7b%22hotelId%22%3a61124%7d')
print(r.json())
# print(r.json()['success'])

# class detail(unittest.TestCase):、
#
# 	def test_detail(self):
# 		'''验证success返回值是否为true'''
# 		self.assertEqual(r.json()['success'],True)
#
# if __name__ == '__main__':
# 	unittest.main(verbosity=2)