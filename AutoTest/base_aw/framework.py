# -*- encoding: utf-8 -*-
"""
@File    : framework.py
@Time    : 2020/5/31 11:56
@Author  : zhangwei
@Email   : 782144334@qq.com
@Software: PyCharm
"""
import pytest


class TestMyPyTest:
    """
    脚本基类
    """
    def setup_class(self):
        print("-------->setup_class")

    def teardown_class(self):
        print("-------->teardown_class")

    def setup(self):
        print("---->setup")

    def teardown(self):
        print("---->teardown")

    def test_001(self):
        print("test_001")

    def test_002(self):
        print("test_002")

    def test_003(self):
        print("test_003")

    def pre_function(self):
        print("环境准备")
        return True

    def post_function(self):
        print("用例执行")
        return True

    def end_function(self):
        print("环境恢复")
        return True
