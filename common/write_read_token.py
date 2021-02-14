#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:liuyang
from common.filepath import filepath

class WriteReadToken(object):
	def __init__(self, filename):
		self.filename = filepath('data', filename)

	# 写入数据后，换行
	def write_data(self, data):
		with open(self.filename, 'w', encoding='utf-8') as f:
			f.write(data+'\n')

	# 读取数据，返回数据列表
	def read_data(self):
		with open(self.filename, 'r', encoding='utf-8') as f:
			datas = f.readlines()
			listdata = []
			for str_value in datas:
				data = str_value.split('\n')[0]
				listdata.append(data)
			return listdata

	# 追加数据后，换行
	def append_data(self, data):
		with open(self.filename, 'a', encoding='utf-8') as f:
			f.write(data+'\n')

# if __name__ == '__main__':
# 	WriteReadToken('text.txt').write_data('ewqrwrqewr')
# 	WriteReadToken('text.txt').append_data('123456')
# 	t = WriteReadToken('text.txt').read_data()
# 	print(t)