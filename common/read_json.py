#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:liuyang

'''
1、导包  os json
2、新建读取json类
	定义初始化方法，获取要读取的json文件
	定义一个读取json文件的方法
		1）打开json文件，获取文件流
		2）使用json对象调用load方法，加载文件流
		3）返回数据    (字典类型)
'''
import json
from common.filepath import filepath

class ReadJson(object):
	def __init__(self, filename):
		self.filename = filepath('data', filename)
		# print(self.filename)

	def read_json(self):
		with open(self.filename, "r", encoding="utf-8") as f:
			data = json.load(f)
		return data

# print(ReadJson('login.json').read_json(), type(ReadJson('login.json').read_json()))




# print(ReadJson('channels.json').read_json())
