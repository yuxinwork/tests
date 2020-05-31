#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pytest

# def add(a,b):
# 	return a+b
#
# @pytest.mark.parametrize('a,b,result',[
# 	(1,2,3),
# 	(2,4,6)
# ])
# def test_add(a,b,result):
# 	assert add(a,b)==result
#
# if __name__=='__main__':
# 	pytest.main(["-v","test_login.py"])


import json
import pytest
from base.method import Requests
from utils.operationYaml import OperationYaml

obj=Requests()
objYaml=OperationYaml()


@pytest.mark.parametrize('datas',objYaml.readYaml())
def test_login(datas):
	# print(datas['data'])
	# print(type(datas['data']))
	
	# print(datas['expect'])
	
	r=obj.post(
		url=datas['url'],
		json=datas['data'])


#  序列化使字典显示为字符串
	print(json.dumps(r.json(),ensure_ascii=False))
 
	# assert datas['expect'] in json.dumps(r.json(),ensure_ascii=False)前面的包含后面的
	assert json.dumps(r.json(), ensure_ascii=False)
	
if __name__=='__main__':
    pytest.main(["-s","-v","test_login.py"])


