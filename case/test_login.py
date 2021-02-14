#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:liuyang

import pytest
import jsonpath
import json
import allure
import pytest_ordering
import unittest
from api.api_login import ApiLogin
from common.read_json import ReadJson
from common.write_read_token import WriteReadToken

# def json_to_list():
# 	list_data = []
	# 获取一条数据
	# data = ReadJson('login.json').read_json()
	# url = data.get('url')
	# mobile = data.get('mobile')
	# code = data.get('code')
	# expect_result =data.get('expect_result')
	# list_data.append((url, mobile, code, expect_result))
	# return list_data


def more_json_to_list():
	list_data = []
	datas = ReadJson('login_more.json').read_json()
	for data in list(datas.values()):
		case_name = data.get('case_name')
		url = data.get('url')
		mobile = data.get('mobile')
		code = data.get('code')
		expect_result = data.get('expect_result')
		list_data.append((case_name, url, mobile, code, expect_result))
	return list_data
	# print(list_data)

@allure.feature('登录模块')
class TestLogin(object):

	@allure.feature('登录')
	@allure.step('拿到login数据，进行登录，然后把token文件写入token.md文件')
	@pytest.mark.run(order=1)
	@pytest.mark.parametrize('case_name,url,mobile,code,expect_result', more_json_to_list())
	def test_login(self, case_name, url, mobile, code, expect_result):
		response = ApiLogin().api_post_login(url=url, mobile=mobile, code=code)
		assert expect_result == response['message']
		if 'token' in json.dumps(response):
			token = jsonpath.jsonpath(response, "$.data.token")[0]
			WriteReadToken('token.md').write_data(token)
			print('token写入成功')

# # if __name__ == '__main__':
# 	unittest.main()