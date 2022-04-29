import page
from base.app_base import AppBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageAppLogin(AppBase):

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.app_login_username, username)

    # 输入验证码
    def page_input_code(self, code):
        self.base_input(page.app_login_code, code)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 判断页面是否存在 我的 菜单
    def page_mine_is_exist(self):
        self.app_base_is_exist(page.app_mine)

    # 组合app登录业务方法
    def page_app_login(self, username, code):
        log.info('正在调用app登录业务方法,用户名为:{},验证码为:{}')
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

    def page_app_login_success(self, username='13812345678', code='246810'):
        log.info('正在调用app登录业务依赖方法,用户名为:{},验证码为:{}')
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()
