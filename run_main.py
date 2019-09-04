import unittest

from selenium.webdriver import DesiredCapabilities

from config.Constant import Constant
from testcase import *
from testcase.login import test_login_case
from tools import email_utils
from tools.driver_grid import RemoteDriver
from tools.report_utils import Report

if __name__ == "__main__":
    # testunit = unittest.TestSuite()
    # testunit.addTest(unittest.makeSuite(login_test_case.LoginTestCase))
    remoteDriver = RemoteDriver()
    list = {"http://localhost:6666/wd/hub": DesiredCapabilities.CHROME,
            "http://localhost:7777/wd/hub": DesiredCapabilities.INTERNETEXPLORER
            }
    for hub, capabilities in list.items():
        driver = remoteDriver.driver_multi(remote_address=hub, capabilities=capabilities)
        testunit = unittest.defaultTestLoader.discover(Constant.TEST_CASE_DIR, pattern="test*.py")
        Report.get_report(testunit)

    # email_utils.send_email(Report.get_report_file())
