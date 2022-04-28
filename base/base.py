import time
from time import strftime
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from config import IMG_FILEPATH
from tools.get_log import GetLog

log = GetLog().get_logger()


# 定义基类
class Base:
    # 获取driver
    def __init__(self, driver):
        log.info('正在初始化driver:{}'.format(driver))
        self.driver = driver

    # 查找方法
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info('正在查找元素:{}'.format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()
        log.info('正在点击元素:{}'.format(loc))

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find(loc)
        log.info('正在对元素:{}执行清空操作'.format(loc))
        el.clear()
        log.info('正在对元素:{}执行输入{}操作'.format(loc, value))
        el.send_keys(value)

    # 获取元素文本方法
    def base_get_text(self, loc):
        log.info('正在获取元素:{}的文本操作'.format(loc))
        return self.base_find(loc).text

    # 截图方法
    def base_get_img(self, img_login_doc):
        img_doc = img_login_doc
        img_filepath = IMG_FILEPATH + '{}_{}.png'.format(strftime('%Y-%m-%d_%H-%M-%S'), img_doc)
        log.info('正在执行截图操作,文件名为:{}'.format(img_filepath))
        self.driver.get_screenshot_as_file(img_filepath)
        time.sleep(2)
        log.info('正在将图片写入allure报告中,文件名为:{}'.format(img_filepath))
        self.__base_write_img(img_filepath, img_doc)

    # 将截图写入allure报告
    # def __base_write_img(self, img_filepath, img_loc):
    #     with open(img_filepath, 'rb') as f:
    #         allure.attach(img_loc, f.read(), allure.attachment_type.PNG)
    def __base_write_img(self, img_filepath, img_allure_doc):
        with open(img_filepath, 'rb') as f:
            allure.attach(name=img_allure_doc, body=f.read(), attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    pass
