import appium.webdriver
# from appium import webdriver
from selenium import webdriver

import page


class GetDriver:
    # web驱动初始化
    __web_driver = None
    # app驱动初始化
    __app_driver = None

    @classmethod
    def get_web_driver(cls, mp_login_url):
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(mp_login_url)
        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
            cls.__web_driver = None

    @classmethod
    def get_app_driver(cls):
        # 判断__appdriver 是否为空
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填且正确 平台名称
            desired_caps['platformName'] = 'Android'
            # 必填且正确 平台版本
            desired_caps['platformVersion'] = '5.1'
            # 必填 设备名称
            desired_caps['deviceName'] = '192.168.51.101:5555'
            # app包名
            desired_caps['appPackage'] = page.appPackage
            # app界面名(启动名)
            desired_caps['appActivity'] = page.appActivity
            # desired_caps = {'platformName': 'Android', 'platformVersion': '5.1', 'deviceName': '192.168.56.101:5555',
            #                 'appPackage': page.appPackage, 'appActivity': page.appActivity}
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                                                       desired_capabilities=desired_caps)
        # 返回cls.__app_driver
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        # 判断driver不为空
        if cls.__app_driver:
            # 关闭driver
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None


if __name__ == '__main__':
    GetDriver.get_app_driver()
