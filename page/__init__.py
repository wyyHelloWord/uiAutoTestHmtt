from selenium.webdriver.common.by import By
"""可以使用空格,来让pytest"""
# from tools.read_yaml import read_yaml

"""以下为需要的url"""
# 自媒体登陆url
mp_login_url = 'http://pc-toutiao-python.itheima.net/#/login'
# 后台管理登陆url
mis_login_url = 'http://ttmis.research.itcast.cn/#/'

"""以下为截图图说明"""
# 自媒体登陆错误截图说明
img_login_doc = '登陆失败'
# 自媒体发布文章失败
img_article_doc = '发布文章失败'
# 后台管理登陆失败截图说明
img_mis_login_doc = '登陆失败'
# 后台管理审核文章通过 失败截图说明
img_audit_doc = '审核文章通过'
# app登录失败截图
img_app_login = 'app登陆失败截图'
# app查找文章失败
img_app_article = 'app查找文章失败'


"""以下为文章相关配置数据"""
# 文章频道
# select_channel = read_yaml('mp_article.yaml')[0][2]
# 文章标题
# input_title = read_yaml('page_mp_article.yaml')[0][0]
"""以下为登陆页面元素"""
# 用户名
mp_username = By.CSS_SELECTOR, '[placeholder="请输入手机号"]'
# 验证码
mp_code = By.CSS_SELECTOR, '[placeholder="验证码"]'
# 登陆按钮
mp_login_btn = By.CSS_SELECTOR, '.el-button--primary'
# 昵称
mp_nickname = By.CSS_SELECTOR, '.user-name'

# 关闭警告按钮
mp_close_btn = By.CSS_SELECTOR, '.el-notification__closeBtn'
# 内容管理
mp_content_management = By.XPATH, '//*[text()="内容管理"]/..'
# 发布文章
mp_post_article = By.XPATH, '//*[contains(text(),"发布文章")]'
# 标题
mp_input_title = By.CSS_SELECTOR, '[placeholder="文章名称"]'
# iframe
mp_iframe = By.CSS_SELECTOR, '#publishTinymce_ifr'
# 内容
mp_input_content = By.CSS_SELECTOR, '#tinymce'
# 封面
mp_select_cover = By.XPATH, '//*[text()="自动"]/..'
# 频道
# select_channel = '数据库'
# select_channel = read_yaml('mp_article.yaml')[0][2]
# 标题 后续审核使用
# title = read_yaml('mp_article.yaml')[0][0]
# select_channel = By.XPATH, '//*[text()="数据库"]/..'
# 发表
mp_click_release = By.XPATH, '//*[text()="发表"]/..'
# 提示
# mp_tips = By.XPATH, '//*[text()="新增文章成功"]'
mp_tips = By.XPATH, '//*[contains(text(),"新增文章成功")]'

"""以下为后台管理登陆页面元素"""
# 用户名
mis_username = By.CSS_SELECTOR, '[name="username"]'
# 密码
mis_password = By.CSS_SELECTOR, '[name="password"]'
# 登陆按钮
mis_login_btn = By.CSS_SELECTOR, '#inp1'
# 昵称
mis_nickname = By.CSS_SELECTOR, ".user_info"
# 信息管理
mis_info_manage = By.XPATH, '//*[text()="信息管理"]/.'
# 文章审核
mis_content_moderation = By.XPATH, '//*[text()="内容审核"]/.'
# 文章标题
mis_article_title = By.CSS_SELECTOR, '[placeholder="请输入: 文章名称"]'
# 所属频道
mis_channel = By.CSS_SELECTOR, '[placeholder="请输入: 频道"]'
# 点击查询
mis_iquire = By.CSS_SELECTOR, '.find'
# 获取id
mis_article_id = By.CSS_SELECTOR, '.cell>span'
# 通过
mis_pass = By.XPATH, '//*[text()="通过"]'
# 确认
mis_confirm = By.CSS_SELECTOR, '.el-button--primary'

"""以下为app配置信息"""
# 包名
appPackage = 'com.android.settings'
# 界面名
appActivity = '.Settings'

"""以下为app登录页面元素"""
# 用户名
app_login_username = By.XPATH, '//*[@index="1" and @class="android.widget.EditText"]'
# 验证码
app_login_code = By.XPATH, '//*[@index="2" and @class="android.widget.EditText"]'
# 登录按钮
app_login_btn = By.XPATH, '//*[@text="登录" and @class="android.widget.Button"]'
# 我的
app_mine = By.XPATH, '//*[@index="3" and contains(@text,"我的")]'
# 频道区域
app_channel = By.XPATH, '//*[@class="android.widget.HorizontalScrollView"]'
# 文章区域
app_article = By.XPATH, '//*[@index="2" and @bounds="[0,520][1440,2280]"]'
