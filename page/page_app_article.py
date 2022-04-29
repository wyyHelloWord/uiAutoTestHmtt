import page
from base.app_base import AppBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageAppArticle(AppBase):
    # 查找频道
    def page_click_channel(self, channel_text):
        # 调用左右滑动方法
        self.app_base_swipe_left_to_right(page.app_channel, channel_text)

    # 查找文章
    def page_click_article(self, article_text):
        # 调用上下滑动
        self.app_base_swipe_from_top_to_bottom(page.app_article, article_text)

    # 组装查找文章业务
    def page_app_article(self, channel_text, article_text):
        log.info('正在调用查找文章业务方法,查找文章频道为:{},查找文章为:{}'.format(channel_text, article_text))
        self.page_click_channel(channel_text)
        self.page_click_article(article_text)
