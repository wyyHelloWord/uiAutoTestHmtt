from page.page_app_article import PageAppArticle
from page.page_app_login import PageAppLogin
from page.page_mis_audit import PageMisAudit
from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        log.info('正在获取PageMpLogin对象')
        return PageMpLogin(self.driver)

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        log.info('正在获取PageMpArticle对象')
        return PageMpArticle(self.driver)

    # 获取PageMisLogin对象
    def page_get_PageMisLogin(self):
        log.info('正在获取PageMisLogin对象')
        return PageMisLogin(self.driver)

    # 获取PageMisAudit对象
    def page_get_PageMisAudit(self):
        log.info('正在获取PageMisAudit对象')
        return PageMisAudit(self.driver)

    # 获取PageAppLogin对象
    def page_get_AppLogin(self):
        log.info('正在获取PageAppLogin对象')
        return PageAppLogin(self.driver)

    # 获取PageAppArticle对象
    def page_get_AppArticle(self):
        log.info('正在获取PageAppArticle对象')
        return PageAppArticle(self.driver)
