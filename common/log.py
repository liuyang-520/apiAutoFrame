#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:liuyang

import logging
from common.filepath import filepath


def log(log_content):
	# 定义日志文件
	logFile = logging.FileHandler(filename=filepath('log', 'log.txt'), mode='a', encoding='utf-8')
	# 设置lofFile的格式
	fmt = logging.Formatter(fmt='[%(asctime)s %(levelname)s] %(message)s')
	logFile.setFormatter(fmt)

	# 定义日志级别
	logger = logging.Logger(name='logTest', level=logging.DEBUG)
	logger.addHandler(logFile)
	logger.debug(log_content)

# print(filepath('log', 'log.txt'))

