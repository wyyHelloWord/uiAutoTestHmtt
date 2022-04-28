from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class WebBase(Base):
    # 选择下拉框指定元素
    def web_base_click_select(self, placeholder, click_text):
        log.info('正在调用web专属方法:点击下拉选择框')
        loc = By.CSS_SELECTOR, '[placeholder="{}"]'.format(placeholder)
        # Select(self.base_find(loc)).select_by_visible_text(click_text)
        self.base_click(loc)
        sleep(2)
        loc = By.XPATH, '//*[text()="{}"]'.format(click_text)
        self.base_click(loc)

    # 判断元素是否存在
    def web_base_is_exist(self, text):
        log.info('正在调用web专属方法:判断元素:{}是否存在'.format(text))
        loc = By.XPATH, '//*[text()="{}"]'.format(text)
        try:
            self.base_find(loc, timeout=3)
            print('找到元素:{}'.format(loc))
            return True
        except:
            print('没有找到元素:{}'.format(loc))
            return False
