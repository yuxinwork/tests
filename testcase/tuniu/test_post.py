#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import unittest

data={
	"hotelId": 61124,
	"adultNum": 2,
	"filters": [],
	"roomNum": 1,
	"childAges": [],
	"checkOut": "2020-05-06",
	"childNum": 0,
	"currentRatePlan": {
		"vendorId":'' ,
		"vendorRatePlanId":''
	},
	"vendorId": "",
	"vendorRatePlanId": 0,
	"checkIn": "2020-05-05"
}

r=requests.post('https://api.tuniu.com/hotel/hotel/rateplan?c=%7B%22cc%22%3A1602%2C%22ct%22%3A10%2C%22p%22%3A14588%2C%22ov%22%3A20%2C%22dt%22%3A0%2C%22v%22%3A%2210.23.0%22%7D',data=data)
class rateplan(unittest.TestCase):
	def test_01(self):
		''''验证success返回测试是否为false'''
		self.assertEqual(r.json()['success'],False)
		
if __name__ == '__main__':
	unittest.main(verbosity=2)