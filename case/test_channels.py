#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:liuyang

import pytest
from jsonpath import jsonpath
from api.api_channels import ApiChannels
from common.read_json import ReadJson
from common.write_read_token import WriteReadToken

def json_to_list():
	list_data = []
	# 获取一条数据
	data = ReadJson('channels.json').read_json()
	url = data.get('url')
	headers = data.get('headers')
	expect_result = data.get('expect_result')
	list_data.append((url, headers, expect_result))
	return list_data
	# print(list_data)

class TestChannels(object):
	@pytest.mark.run(order=2)
	@pytest.mark.parametrize('url,headers,expect_result', json_to_list())
	def test_channels(self, url, headers, expect_result):
		token = WriteReadToken('token.md').read_data()[0]
		# print(token)
		headers['Authorization'] = 'Bearer {}'.format(token)
		# print(headers)
		response = ApiChannels().api_get_channels(url=url, headers=headers)
		# print(response)
		assert expect_result == response['message']
		channel = jsonpath(response, '$.data.channels[0]')[0]
		WriteReadToken('token.md').append_data(str(channel))