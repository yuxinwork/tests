#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
#返回上层目录，两次就是返回更上一层目录
# print(os.path.dirname(os.path.dirname(__file__)))
# base_url=(os.path.dirname(os.path.dirname(__file__)))
# print(os.path.join(base_url,'data','lonin.yaml'))


def filepath(fileDir='data',fileName='login.yaml'):
	'''
	封装找到所有文件的路径
	:param fileDir: 目录
	:param fileNme: 文件的名称
	:return:
	'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

 # print(filepath())
# print(filepath('config','config.yaml'))