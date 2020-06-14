# -*- encoding: utf-8 -*-
"""
@File    : framework.py
@Time    : 2020/5/31 11:56
@Author  : zhangwei
@Email   : 782144334@qq.com
@Software: PyCharm
"""

import pytest
from commom.logger import Log


class TestMyPyTest(object):
    """
    脚本基类
    """
    logge = logger()

    @classmethod
    def setup_class(cls):
        return

    @classmethod
    def teardown_class(cls):
        return

    def setup_method(self):
        try:
            print("======================初始化============================")
            self.pre_function()
        except Exception as e:
            print("环境准备失败")

    def teardown_method(self):
        self.end_function()

    def pre_function(self):
        return True

    def end_function(self):
        return True

    def global_init(self):
        print('全局初始化')

    def global_end(self):
        print('全局结束')

    @pytest.fixture(scope='session', autouse=True)
    def global_func(self):
        self.global_init()
        yield
        self.global_end()
