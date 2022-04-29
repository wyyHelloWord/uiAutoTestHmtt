from time import sleep
import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisAudit(WebBase):
    article_id = None

    # 点击信息管理
    def page_click_information_management(self):
        sleep(1)
        self.base_click(page.mis_info_manage)

    # 点击内容审核
    def page_click_content_moderation(self):
        self.base_click(page.mis_content_moderation)

    # 输入文章标题
    def page_input_article_title(self, mis_article_title):
        self.base_input(page.mis_article_title, mis_article_title)

    # 选择所属频道
    def page_select_channel(self, channel):
        self.base_input(page.mis_channel, channel)

    # 选择状态
    def page_select_state(self, placeholder='请选择', click_text='待审核'):
        self.web_base_click_select(placeholder, click_text)
        pass

    # 点击查询
    def page_click_inquire(self):
        self.base_click(page.mis_iquire)

    # 获取id
    def page_get_article_id(self):
        return self.base_get_text(page.mis_article_id)

    # 点击通过
    def page_click_pass(self):
        self.base_click(page.mis_pass)

    # 点击确认
    def page_click_confirm(self):
        self.base_click(page.mis_confirm)

    # 组装文章审核业务方法
    def page_mis_audit(self, mis_article_title, channel):
        log.info('正在调用文章审核业务方法,标题为:{},频道为:{}'.format(mis_article_title, channel))
        self.page_click_information_management()
        self.page_click_content_moderation()
        self.page_input_article_title(mis_article_title)
        self.page_select_channel(channel)
        self.page_select_state()
        self.page_click_inquire()
        self.article_id = self.page_get_article_id()
        print('获取文章id为:'.format(self.article_id))
        self.page_click_pass()
        self.page_click_confirm()

    # 组装确认审核通过业务方法
    def page_assert_audit(self):
        log.info('正在调用确认审核通过业务方法')
        # 暂停三秒
        sleep(3)
        # 修改查询状态 --> 审核通过
        self.page_select_state(click_text='审核通过')
        # 点击查询
        self.page_click_inquire()
        # 判断页面是否存在指定文章id并返回结果
        return self.web_base_is_exist(self.article_id)
