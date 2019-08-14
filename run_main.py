import unittest

from config.Constant import Constant
from testcase import *
from testcase.login import test_login_case
from tools import email_utils
from tools.report_utils import Report

if __name__ == "__main__":
    # testunit = unittest.TestSuite()
    # testunit.addTest(unittest.makeSuite(login_test_case.LoginTestCase))
    testunit = unittest.defaultTestLoader.discover(Constant.TEST_CASE_DIR, pattern="test*.py")
    Report.get_report(testunit)
    # email_utils.send_email(Report.get_report_file())
