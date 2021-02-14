#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:liuyang

'''
封装登录接口类
'''
import requests


class ApiLogin(object):

	def api_post_login(self, url, mobile, code):
		# 定义headers
		headers = {"Content_Type": "application/json"}
		# 定义参数
		data = {"mobile": mobile, "code": code, 'xieyi': True}
		# 调用post方法并返回登录结果
		return requests.post(url=url, headers=headers, json=data).json()


'''
步骤：
1、导包
2、新建接口对象类
3、新建登录方法
	定义headers、data
	调用post并返回

'''