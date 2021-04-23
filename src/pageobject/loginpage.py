from src.pageobject.basepage import Page
from selenium.webdriver.common.by import By


# 登录页面
class LoginPage(Page):
    # 元素集

    # 账号输入框
    account_input = (By.NAME, "account")
    # 密码输入框
    password_input = (By.NAME, "password")
    # 登录按钮
    login_button = (By.XPATH, "//span[text()='登 录']")
    # 关闭窗口按钮
    close_button = (By.CLASS_NAME, "icon-close")

    # 验证元素
    # 退出系统按钮
    logout_button = (By.XPATH, "//span[text()='退出系统']")

    def __init__(self, driver):
        Page.__init__(self, driver)

    # 输入账号
    def input_account(self, account):
        self.input_text(self.account_input, account)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.password_input, password)

    # 点击登录
    def click_login(self):
        self.click(self.login_button)
