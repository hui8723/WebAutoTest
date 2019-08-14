import os
import time
from HTMLTestRunner import HTMLTestRunner

from config.Constant import Constant
from tools.file_utils import FileUtils


class Report(object):

    @staticmethod
    def get_report(all_case, filename="result.html"):
        """运行用例，生成测试报告"""
        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        FileUtils.make_dir(Constant.REPORT_DIR)
        file_path = os.path.join(Constant.REPORT_DIR, now + filename)

        fp = open(file_path, "wb")
        runner = HTMLTestRunner(stream=fp, title="自动化接口测试报告，测试结果如下：", description="用例执行情况")
        runner.run(all_case)
        fp.close()

    @staticmethod
    def get_report_file():
        """获取最新的测试报告"""
        lists = os.listdir(Constant.REPORT_DIR)
        lists.sort(key=lambda fn: os.path.getmtime(os.path.join(Constant.REPORT_DIR, fn)))
        print("最新报告：" + lists[-1])
        report_file = os.path.join(Constant.REPORT_DIR, lists[-1])
        return report_file
