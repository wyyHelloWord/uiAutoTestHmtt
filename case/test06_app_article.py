import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestAppArticle:

    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取统一入口类PageIn对象
        self.page_in = PageIn(driver)
        # 调用app登录依赖方法
        self.page_in.page_get_AppLogin().page_app_login_success()
        # 获取PageAppArticle对象
        self.app_article = self.page_in.page_get_AppArticle()

    # 关闭driver
    def teardown_class(self):
        log.info('正在关闭driver')
        GetDriver.quit_app_driver()

    # 测试app查找文章方法
    @pytest.mark.parametrize('channel_text,article_text', read_yaml('app_article.yaml'))
    def test_app_article(self, channel_text, article_text):
        try:
            # 调用app查找文章方法
            self.app_article.page_app_article(channel_text, article_text)
        except Exception as e:
            # 日志
            log.error('没有找到元素,原因{}'.format(e))
            # 截图
            self.app_article.base_get_img(page.img_app_article)
            # 抛异常
            raise
