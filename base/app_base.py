from time import sleep
import appium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.base import Base
from tools.get_log import GetLog
from appium import webdriver

log = GetLog.get_logger()


# driver = appium.webdriver.Remote()
# print(NoSuchContextException)


class AppBase(Base):
    # 判断元素是否存在
    def app_base_is_exist(self, loc):
        log.info('正在判断元素:{}是否存在'.format(loc))
        try:
            self.base_find(loc, timeout=3)
            log.info('在app页面中,找到元素:{}'.format(loc))
            print('找到元素:{}'.format(loc))
            return True
        except:
            log.error('没有找到元素:{}'.format(loc))
            print('没有找到元素:{}'.format(loc))
            return False

    # 从左向右滑动
    def app_base_swipe_left_to_right(self, loc_area, channel_text):
        log.info('正在调用从左向右滑方法')
        # 获取元素
        el = self.base_find(loc_area)
        # location获取元素左上角坐标
        y = el.location.get('y')
        # 获取元素的宽
        width = el.size.get('width')
        # 获取元素的高
        height = el.size.get('height')
        # 获取起点x
        start_x = width * 0.8
        # 获取起点y
        start_y = y + height * 0.5
        # 获取终点x
        end_x = width * 0.2
        # 获取终点y
        end_y = y + height * 0.5
        # 定位要点击的元素
        loc = By.XPATH, '//*[@class="android.widget.HorizontalScrollView"]//*[contains(@text,"{}")]'.format(
            channel_text)
        # loc = By.XPATH, '//android.widget.HorizontalScrollView/*[contains(@text,"{}")]'.format(
        #     channel_text)
        # 循环翻页
        while True:
            # 获取页面结构信息
            page_source = self.driver.page_source
            # 捕获异常
            try:
                # 暂停2秒
                sleep(2)
                # 查找元素
                el = self.base_find(loc, timeout=3)
                # 找到元素
                print('找到元素:{}'.format(loc))
                el.click()
                break
            # 异常处理
            except:
                # 没有找到元素
                print('暂未找到元素:{}'.format(loc))
                # 滑动屏幕
                log.info('正在滑动屏幕')
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
                # 判断是否到最后一屏
            if page_source == self.driver.page_source:
                # 输出提示信息
                print('已经滑到最后一屏,没有找到元素')
                # 抛出异常
                raise NoSuchElementException

    def app_base_swipe_from_top_to_bottom(self, loc_area, article_text):
        log.info('正在调用从下向上滑方法')
        # 获取元素
        el = self.base_find(loc_area)
        # 获取元素的宽
        width = el.size.get('width')
        # 获取元素的高
        height = el.size.get('height')
        # 获取起点x
        start_x = width * 0.5
        # 获取起点y
        start_y = height * 0.8
        # 获取终点x
        end_x = width * 0.5
        # 获取终点y
        end_y = height * 0.2
        # 定位要点击的元素
        loc = By.XPATH, '//*[@bounds="[0,520][1440,2280]"//*[contains(@text,"{}")]]'.format(article_text)
        # loc = By.XPATH, '//android.widget.HorizontalScrollView/*[contains(@text,"{}")]'.format(channel_text)
        # 循环翻页
        while True:
            # 获取页面结构信息
            page_source = self.driver.page_source
            # 捕获异常
            try:
                # 暂停2秒
                sleep(2)
                # 查找元素
                el = self.base_find(loc, timeout=3)
                # 找到元素
                print('找到元素:{},文章标题为:{}'.format(loc, el.text))
                el.click()
                break
            # 异常处理
            except:
                # 没有找到元素
                print('暂未找到元素:{}'.format(loc))
                # 滑动屏幕
                log.info('正在滑动屏幕')
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
                # 判断是否到最后一屏
            if page_source == self.driver.page_source:
                # 输出提示信息
                print('已经滑到最后一屏,没有找到元素')
                # 抛出异常
                raise NoSuchElementException
