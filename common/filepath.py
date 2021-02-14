#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:liuyang
import os

def filepath(dirname=None, filename=None):
	return os.path.dirname(os.path.dirname(__file__))+r"\{}".format(dirname)+r"\{}".format(filename)

# filepath('report', 'report.html')