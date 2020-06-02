#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

class Requests:
	def request(self,url,method='get',**Kwargs):
		if method=='get':
			return requests.request(url=url,method=method,**Kwargs)
		elif method=='post':
			return requests.request(url=url,method=method,**Kwargs)
		elif method == 'put':
			return requests.request(url=url,method='put',**Kwargs)
		elif method == 'delete':
			return requests.request(url=url,method='delete',**Kwargs)
		
		
	def get(self,url,**Kwargs):
		return self.request(url=url,**Kwargs)
	
	def post(self,url,**Kwargs):
		return self.request(url=url,method='post',**Kwargs)
	
	def put(self,url,**Kwargs):
		return self.request(url=url,method='put',**Kwargs)
	
		