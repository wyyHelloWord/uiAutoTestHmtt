from time import sleep

import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpArticle(WebBase):

    # 关闭警告
    def page_click_warring_close(self):
        sleep(2)
        self.base_click(page.mp_close_btn)

    # 点击 内容管理
    def page_click_content_management(self):
        sleep(2)
        self.base_click(page.mp_content_management)

    # 点击 发布文章
    def page_click_post_article(self):
        sleep(1)
        self.base_click(page.mp_post_article)

    # 输入标题
    def page_input_title(self, mp_title):
        sleep(1)
        self.base_input(page.mp_input_title, mp_title)

    # 输入内容
    def page_input_content(self, content_text):
        # 切换iframe #publishTinymce_ifr
        sleep(1)
        self.driver.switch_to.frame(self.base_find(page.mp_iframe))
        # 输入内容
        sleep(1)
        self.base_input(page.mp_input_content, content_text)
        # 回到默认iframe
        self.driver.switch_to.default_content()

    # 点击选择封面
    def page_click_select_cover(self):
        sleep(1)
        self.base_click(page.mp_select_cover)

    # 选择频道 数据库
    def page_click_select_channel(self, select_channel):
        sleep(1)
        self.web_base_click_select(placeholder='请选择', click_text=select_channel)

    # 点击发布
    def page_click_release(self):
        sleep(1)
        self.base_click(page.mp_click_release)

    # 获取提示信息
    def page_get_tips(self):
        return self.base_get_text(page.mp_tips)

    # 组装发布文章业务用例
    def page_mp_article(self, input_title, input_content, select_channel):
        log.info('正在调用发布文章业务,文章标题为:{},内容为:{}'.format(input_title, input_content))
        self.page_click_content_management()
        self.page_click_post_article()
        self.page_input_title(input_title)
        self.page_input_content(input_content)
        self.page_click_select_cover()
        self.page_click_select_channel(select_channel)
        self.page_click_release()
