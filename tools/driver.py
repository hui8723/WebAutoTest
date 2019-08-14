# coding:utf-8
import time
from selenium import webdriver


def browser(browser="chrome"):
    """
    启动指定浏览器
    usage:
    driver = browser("chrome")
    :param browser: 'firefox', 'chrome', 'ie', 'phantomjs' or 'safari'
    :return:
    """
    try:
        if browser == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif browser == "chrome":
            chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
            driver = webdriver.Chrome(executable_path=chrome_driver)
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        elif browser == "safari":
            driver = webdriver.Safari()
            return driver
        else:
            print("Not found browser! You can enter 'firefox', 'chrome', 'ie', 'phantomjs' or 'safari'")
            return
    except Exception as msg:
        print("open browser error:%s" % msg)
        return


if __name__ == '__main__':
    driver = browser("aa")
    # driver = browser("chrome")
    if driver:
        driver.get("https://www.baidu.com")
        time.sleep(2)
        driver.quit()