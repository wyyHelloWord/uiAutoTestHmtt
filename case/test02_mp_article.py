from time import sleep
import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestMpArticle:

    def setup_class(self):
        driver = GetDriver.get_web_driver(page.mp_login_url)
        self.page_in = PageIn(driver)
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        self.article = self.page_in.page_get_PageMpArticle()

    def teardown_class(self):
        sleep(2)
        log.info('正在关闭driver')
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize('input_title,input_content,select_channel,expect', read_yaml('mp_article.yaml'))
    def test_mp_article(self, input_title, input_content, select_channel, expect):
        self.article.page_click_warring_close()
        self.article.page_mp_article(input_title, input_content, select_channel)
        try:
            # print(expect)
            # print(self.article.page_get_tips())
            log.info('正在判断{}和{}是否相等'.format(expect, self.article.page_get_tips()))
            assert self.article.page_get_tips() == expect
        except Exception as e:
            log.error('断言失败,原因:{}'.format(e))
            self.article.base_get_img(page.img_article_doc)
            raise


if __name__ == '__main__':
    TestMpArticle().test_mp_article()
