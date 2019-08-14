import os


class Constant(object):
    ROOT = os.path.dirname(os.path.dirname(__file__))

    LOGGER = "WebAutoTest"  # 日志名

    LOG_DIR = os.path.join(ROOT, "Log")               # 日志地址

    SCREEN_SHOT_DIR = os.path.join(ROOT, "screenshot")   # 截屏保存地址

    REPORT_DIR = os.path.join(ROOT, "report")         # 测试报告地址

    TEST_CASE_DIR = os.path.join(ROOT, "testcase")     # 测试用例地址