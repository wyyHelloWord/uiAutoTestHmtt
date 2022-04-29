import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMisLogin:

    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.mis_login_url)
        # 获取PageMisLogin对象
        self.mis = PageIn(driver).page_get_PageMisLogin()

    def teardown_class(self):
        # 关闭drive
        log.info('正在关闭driver')
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize('username,password,expect', read_yaml('mis_login.yaml'))
    def test_mis_login(self, username, password, expect):
        # 调用后台管理登陆方法
        self.mis.page_mis_login(username, password)
        # 断言
        try:
            # 实际结果是否和预期一致
            log.info('正在判断实际结果:{}和预期结果:{}是否一致'.format(self.mis.page_get_nickname(), expect))
            assert self.mis.page_get_nickname() == expect
        except Exception as e:
            # 截图并写入报告
            self.mis.base_get_img(page.img_mis_login_doc)
            # 抛出异常
            log.error('断言失败,原因:{}'.format(e))
            raise


if __name__ == '__main__':
    TestMisLogin()
