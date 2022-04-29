import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMisAudit:
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.mis_login_url)
        # 获取统一入口类对象
        log.info('正在获取PageIn对象')
        self.page_in = PageIn(driver)
        # 调用后台管理登录依赖方法
        self.page_in.page_get_PageMisLogin().page_mis_login_success()
        # 获取后台管理审核对象
        self.audit = self.page_in.page_get_PageMisAudit()

    def teardown_class(self):
        # 关闭driver
        log.info('正在关闭driver')
        GetDriver.quit_web_driver()

    # 审核文章业务测试方法
    @pytest.mark.parametrize('input_title,input_content,select_channel,expect', read_yaml('mp_article.yaml'))
    def test_mis_audit(self, input_title, input_content, select_channel, expect):
        # 调用app登录方法
        self.audit.page_mis_audit(input_title, input_content)
        try:
            log.info('正在断言')
            assert self.audit.page_assert_audit()
        except Exception as e:
            # 日志
            log.info('断言失败,原因{}'.format(e))
            # 截图
            self.audit.base_get_img(page.img_audit_doc)
            # 抛异常
            raise

        # 审核文章业务测试方法

    # def test_mis_audit(self):
    #     self.audit.page_mis_audit(page.input_title, page.select_channel)
    #     try:
    #         assert self.audit.page_assert_audit()
    #     except Exception as e:
    #         self.audit.base_get_img(page.img_audit_doc)
    #         raise
