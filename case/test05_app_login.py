import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestAppLogin:

    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取PageAppLogin对象
        self.app_login = PageIn(driver).page_get_AppLogin()

    def teardown_class(self):
        # 关闭driver
        log.info('正在关闭driver')
        GetDriver.quit_app_driver()

    # 测试app登录业务方法
    @pytest.mark.parametrize('username,code', read_yaml('app_login.yaml'))
    def test_app_login(self, username, code):
        self.app_login.page_app_login(username, code)
        try:
            log.info('正在断言元素是否存在')
            assert self.app_login.page_mine_is_exist()
        except Exception as e:
            self.app_login.base_get_img(page.img_app_login)
            log.error('断言失败, 原因:', e)
            raise
