# -*- encoding: utf-8 -*-
"""
@File    : tc_001.py
@Time    : 2020/5/31 11:53
@Author  : zhangwei
@Email   : 782144334@qq.com
@Software: PyCharm
"""
from base_aw.framework import TestMyPyTest


class Test001(TestMyPyTest):
    """

    """
    def pre_function(self):
        print("环境准备")
        return True

    def post_function(self):
        print("用例执行")
        return True

    def end_function(self):
        print("环境恢复")
        return True

    def test_001(self):
        print("test_001")


