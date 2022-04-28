from time import sleep
import page
from base.base import Base
from tools.get_log import GetLog

log = GetLog().get_logger()


class PageMpLogin(Base):
    # 输入用户名方法
    def page_input_username(self, username):
        self.base_input(page.mp_username, username)

    # 输入验证码方法
    def page_input_code(self, code):
        self.base_input(page.mp_code, code)

    # 点击登陆按钮方法
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取昵称方法
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # 截图方法并写入allure方法
    def page_get_img(self, img_doc):
        self.base_get_img(img_doc)

    # 组装业务方法
    # def page_mp_login(self, username, code):
    def page_mp_login(self):
        sleep(1)
        # log.info('正在执行登陆业务,用户名为{},验证码为{}'.format(username, password))
        log.info('正在调用自媒体登陆业务方法')
        # self.page_input_username(username)
        # sleep(1)
        # self.page_input_code(code)
        # sleep(1)
        self.page_click_login_btn()

    def page_mp_login_success(self):
        sleep(1)
        # log.info('正在执行登陆业务,用户名为{},验证码为{}'.format(username, password))
        log.info('正在调用自媒体登陆业务方法')
        # self.page_input_username(username)
        # sleep(1)
        # self.page_input_code(code)
        # sleep(1)
        self.page_click_login_btn()
