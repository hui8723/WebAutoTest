import unittest

from tools.driver import browser


class BaseCase(unittest.TestCase):

    def setUp(self):
        print("测试用例开始执行！")
        self._initial()

    def _initial(self):
        self.driver = browser()

    def tearDown(self):
        print("测试用例执行完毕！")
        # self._clean()

    def _clean(self):
        if self.driver:
            self.driver.quit()
