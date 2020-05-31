#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  yaml
from common.public import filepath

# class OperationYaml:
# 	def readYaml(self):
# 		with open(filepath(),'r')as f:
# 			return yaml.safe_load_all(f)
# if __name__=='__main__':
# 	obj=OperationYaml()
# 	print(obj.readYaml)
class OperationYaml:
	def readYaml(self):
		with open(filepath(),'r',encoding='utf-8')as f:
			return list(yaml.safe_load_all(f))
		
if __name__=='__main__':
	obj=OperationYaml()
	for item in obj.readYaml():
		print(item)