# -*- encoding: utf-8 -*-
"""
@File    : web_auto.py
@Time    : 2020/5/30 18:54
@Author  : zhangwei
@Email   : 782144334@qq.com
@Software: PyCharm
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class WebDriver(webdriver):
    """
    web基类
    """
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        """
        locator = ("id","kw")，查找某元素
        :param locator:
        :return:
        """
        element = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*locator))
        return element

    def send(self, locator, text):
        """
        输入框传值
        :param locator:
        :param text:
        :return:
        """
        self.find(locator).send_keys(text)

    def click(self, locator):
        """
        点击事件
        :param locator:
        :return:
        """
        self.find(locator).click()

    def is_element_exist(self, locator):
        """
        判断元素是否存在
        :param locator:
        :return:
        """
        els = self.finds(locator)
        # 计算元素个数
        count = len(els)
        if len(els) < 1:
            return False
        else:
            print("定位到的元素个数：%s" % count)
            return True
