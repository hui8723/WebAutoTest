import time

from testcase.base_case import BaseCase
from tools.driver import browser


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        # self.url = "http://localhost/login/"
        self.open_pwd()
        self.username = self.driver.find_element_by_name('username')
        self.password = self.driver.find_element_by_name('password')
        self.button = self.driver.find_element_by_xpath(r'//*[@id="root"]/div/main/div/div/div[2]/div/form/button')
        self.username_empty = self.driver.find_element_by_xpath(
            r'//*[@id="root"]/div/main/div/div/div[2]/div/form/div[2]/div[2]/div[2]')
        self.pwd_empty = self.driver.find_element_by_xpath(r'//*[@id="root"]/div/main/div/div/div[2]/div/form/div[3]/div/div[2]')
        self.username_error_mask = self.driver.find_element_by_xpath(r'//*[@id="root"]/div/main/div/div/div[2]/div/form/div[2]/div[2]/div[2]')
        self.nickname = self.driver.find_element_by_name('nickname')

    def open_pwd(self):
        self.driver.get(self.url)
        time.sleep(2)
        login_form = self.driver.find_element_by_tag_name('form')
        tab_pwd = self.driver.find_element_by_xpath(r'//*[@id="root"]/div/main/div/div/div[2]/div/form/div[1]/div[2]')
        tab_pwd.click()
        time.sleep(2)

    # 定义用户名输入框元素
    def type_username(self, username):
        self.username.send_keys(username)

    # 定义密码输入框元素
    def type_pwd(self, password):
        self.password.send_keys(password)

    # 定义Submit按钮元素和点击方法
    def type_action(self):
        self.button.click()

    def type_username_hint(self):
        return self.username.text

    def type_pwd_hint(self):
        return self.password.text

    # 用户名为空提示是否显示
    def is_username_tips_show(self):
        return self.username_empty.is_displayed()

    # 密码为空提示是否显示
    def is_pwd_tips_show(self):
        return self.pwd_empty.is_displayed()

    def is_username_error_show(self):
        return self.username_error_mask.is_displayed()

    # 定义用户名内容
    def type_username_value(self):
        return self.username.get_attribute('value')

    def type_nickname_value(self):
        return self.nickname.get_attribute('value')

    # 登录操作
    def login_action(self, username, password):
        self.type_username(username)
        self.type_pwd(password)
        self.type_action()

    # 获取登录昵称
    def get_nickname(self):
        return self.type_nickname_value()