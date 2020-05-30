# -*- encoding: utf-8 -*-
"""
@File    : test_web.py
@Time    : 2020/5/30 19:29
@Author  : zhangwei
@Email   : 782144334@qq.com
@Software: PyCharm
"""
import time
import unittest
from LIB.Selenium.web_auto import WebDriver
from selenium import webdriver


class WebTest(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.baidu.com"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.base_lei = WebDriver(self.driver)

    def tearDown(self):
        # 清空cookies
        self.driver.delete_all_cookies()
        self.driver.quit()

    def test_001(self):
        """

        :return:
        """
        self.driver.get(self.url + "/")
        # self.driver.find_element_by_id("kw").clear()
        # self.driver.find_element_by_id("kw").send_keys("unittest")
        self.driver.find_element_by_link_text("新闻").click()

        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        title = self.driver.title
        self.assertEqual(title, u"unittest_百度搜索")
    pass
