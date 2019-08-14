import time

from testcase.base_case import BaseCase
from page.login_page import LoginPage
from tools import screen_utils


class LoginTestCase(BaseCase):

    def test_login01_empty(self):
        """用户名和密码没有输入"""
        self.po = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        self.po.login_action("", "")
        if not (self.po.is_username_tips_show() and self.po.is_pwd_tips_show()):
            screen_utils.screenshot(self.driver, "test_login01_empty.png")
        self.assertEqual(True, self.po.is_username_tips_show())
        self.assertEqual(True, self.po.is_pwd_tips_show())

    def test_login02_no_user(self):
        """用户名未输入，密码正常输入"""
        self.po = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        self.po.login_action("aaa", "")
        if not ((not self.po.is_username_tips_show()) and self.po.is_pwd_tips_show()):
            screen_utils.screenshot(self.driver, "test_login02_no_user.png")
        self.assertEqual(False, self.po.is_username_tips_show())
        self.assertEqual(True, self.po.is_pwd_tips_show())

    def test_login03_no_pwd(self):
        """用户名正常输入，密码未输入"""
        self.po = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        self.po.login_action("", "bbb")
        self.assertEqual(True, self.po.is_username_tips_show())
        self.assertEqual(False, self.po.is_pwd_tips_show())

    def test_login04_input_photo_error(self):
        """用户名未输入正确的电话号码"""
        self.po = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        self.po.login_action("aaa", "bbb")
        if not self.po.is_username_error_show():
            screen_utils.screenshot(self.driver, "test_login04_input_photo_error.png")
        self.assertEqual(True, self.po.is_username_error_show())

    def test_login05_input_email_error(self):
        """用户名未输入正确的邮箱地址"""
        self.po = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        self.po.login_action("aaa@", "bbb")
        if not self.po.is_username_error_show():
            screen_utils.screenshot(self.driver, "test_login05_input_email_error.png")
        self.assertEqual(True, self.po.is_username_error_show())

    def test_login06_normal(self):
        """用户名和密码正常输入"""
        self.po = LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        self.po.login_action("xxxxxx", "xxxxxxx")
        if not "xxx".__eq__(self.po.get_nickname()):
            screen_utils.screenshot(self.driver, "test_login06_normal.png")
        self.assertEqual("xxxx", self.po.get_nickname())
