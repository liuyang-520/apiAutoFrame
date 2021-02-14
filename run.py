#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:liuyang
import pytest
import os
import

# if __name__ =="__main__":
#     # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
#     pytest.main(['--alluredir', './temp'])
#     # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
#     os.system('allure generate ./temp -o ./report --clean')

if __name__ == '__main__':
    pytest.main(["-s", '-v', './case', '--alluredir', './report/tmp'])
    os.system('allure generate ./report/tmp -o ./report/report --clean')