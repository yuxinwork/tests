#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

def conn():
	try:
		conn = pymysql.connect(
			host="127.0.0.1",
			user='root',
			passwd='',
			db='db1')
	except Exception as e:
		return e.args
	else:
		cur=conn.cursor()
		sql='select * from score where s_id=%s'
		params=(2,)
		cur.execute(sql,params)
		data=cur.fetchone()
		print(data)
	finally:
		cur.close()
		conn.close()
		
print(conn())

