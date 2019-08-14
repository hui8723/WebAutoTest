import os

from config.Constant import Constant
from tools.driver import browser
from tools.file_utils import FileUtils


def screenshot(driver, filename):
    """截屏"""
    FileUtils.make_dir(Constant.SCREEN_SHOT_DIR)
    filepath = os.path.join(Constant.SCREEN_SHOT_DIR, filename)
    print(filepath)
    driver.get_screenshot_as_file(filepath)


if __name__ == "__main__":
    driver = browser()
    driver.get("http://www.baidu.com")
    screenshot(driver, "test.png")
    driver.quit()