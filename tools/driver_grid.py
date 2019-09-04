from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class RemoteDriver():

    def driver_multi(self, remote_address, capabilities):
        driver = webdriver.Remote(remote_address, desired_capabilities=capabilities)
        return driver


if __name__ == '__main__':
    remoteDriver = RemoteDriver()
    list = {"http://localhost:6666/wd/hub": DesiredCapabilities.CHROME,
            "http://localhost:7777/wd/hub": DesiredCapabilities.INTERNETEXPLORER
            }
    for hub, capabilities in list.items():
        driver = remoteDriver.driver_multi(remote_address=hub, capabilities=capabilities)
        driver.get('http://www.baidu.com')
        print(driver.title)
