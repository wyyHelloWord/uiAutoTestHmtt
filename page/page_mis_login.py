import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisLogin(WebBase):
    """后台管理登陆"""

    # 输入账号
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.mis_password, password)

    # 点击登陆
    def page_click_login_btn(self):
        # 设置js
        js = 'document.getElementById("inp1").disabled=false'
        log.info('正在设置登陆js')
        self.driver.execute_script(js)
        # 点击登陆
        self.base_click(page.mis_login_btn)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 组装后台管理登录业务
    def page_mis_login(self, username, password):
        log.info('正在调用后台管理登录业务方法')
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

    # 组装后台管理登录依赖方法
    def page_mis_login_success(self, username='testid', password='testpwd123'):
        log.info('正在调用后台管理登录依赖方法')
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
