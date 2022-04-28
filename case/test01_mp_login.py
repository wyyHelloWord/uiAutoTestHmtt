from time import sleep
import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog().get_logger()


class TestMpLogin:
    # 获取driver
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.mp_login_url)
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 关闭driver
    def teardown_class(self):
        sleep(2)
        GetDriver.quit_web_driver()

    # 测试业务方法
    # def test_mp_login(self):
    #     self.mp.page_mp_login('13911111111', '246810')
    #     try:
    #         assert self.mp.page_get_nickname() == 'java'
    #     except Exception as e:
    #         # self.mp.page_get_img()
    #         raise
    # def test_mp_login(self):
    #     self.mp.page_mp_login()
    #     try:
    # print(self.mp.page_get_nickname())
    # print(type(self.mp.page_get_nickname()))
    # assert self.mp.page_get_nickname() == 'java'
    # self.mp.page_get_img()
    # except Exception as e:
    # self.mp.page_get_img()
    # raise

    @pytest.mark.parametrize('username,code,expect', read_yaml('mp_login.yaml'))
    # @pytest.mark.parametrize('expect', read_yaml('mp_login.yaml'))
    # def test_mp_login(self, expect):
    def test_mp_login(self, username, code, expect):
        self.mp.page_mp_login()
        try:
            # print(self.mp.page_get_nickname())
            # print(type(self.mp.page_get_nickname()))
            # print(expect[0])
            # assert expect[0] == self.mp.page_get_nickname()
            log.info('正在断言{}和{}是否相等'.format(expect, self.mp.page_get_nickname()))
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            log.error('断言失败,错误原因{}'.format(e))
            self.mp.page_get_img(page.img_login_doc)
            raise
