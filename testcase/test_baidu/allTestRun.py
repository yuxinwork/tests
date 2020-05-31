#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os
import HTMLTestRunner


def allTest():
	suite = unittest.TestLoader().discover(
		start_dir=os.path.dirname(__file__),
		pattern='test_*.py',
		top_level_dir=None)
	return suite
#print(allTest())

def run():
	fp=os.path.join(os.path.dirname(__file__),'report','testReport.html')
	unittest.TextTestRunner(verbosity=2).run(allTest())
	
	

# if __name__ =='__main__':
# 	run()
