# -*- encoding: utf-8 -*-
"""
@File    : test_send_email.py
@Time    : 2020/5/31 9:59
@Author  : zhangwei
@Email   : 782144334@qq.com
@Software: PyCharm
"""

from LIB.E_mail import e_mail
import unittest

class SendEmail(unittest.TestCase):

    def setUp(self) -> None:
        self.send = e_mail.SendEmail

    def tearDown(self) -> None:
        pass

    def test_001(self):
        self.send.send_email("E:\G\zhangwei\AutoTest\pip_install.bat")
