# -*- encoding: utf-8 -*-
"""
@File    : tc_001.py
@Time    : 2020/5/31 11:53
@Author  : zhangwei
@Email   : 782144334@qq.com
@Software: PyCharm
"""
import unittest
from base_aw.framework import MyUnitTest


class MyTestCase(MyUnitTest):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
