#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:liuyang

import requests

class ApiChannels(object):
	def api_get_channels(self, url, headers):
		return requests.get(url=url, headers=headers).json()