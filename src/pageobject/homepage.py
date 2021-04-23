from src.pageobject.loginpage import LoginPage
from selenium.webdriver.common.by import By


# 主页面
class HomePage(LoginPage):
    # 元素集

    # '未完成任务'按钮
    incomplete = (By.XPATH, "//div[text()='未完成任务']")
    # '未完成任务'按钮
    completed = (By.XPATH, "//div[text()='已完成任务']")
    # 荣誉榜按钮
    honors = (By.XPATH, "//span[text()='荣誉榜']")
    # 修改密码按钮
    modifypassword = (By.XPATH, "//span[text()='修改密码']")
    # 修改信息按钮
    modifyinformation = (By.XPATH, "//span[text()='修改信息']")
    # 退出系统按钮
    logout = (By.XPATH, "//span[text()='退出系统']")
    # 单词量测试按钮
    wordtest = (By.XPATH, "//div[text()='单词量测试']")

    # 验证元素
    # 荣誉榜-总排行
    total_tanking = (By.XPATH, "//li[text()='总排行']")
    # 修改密码-确认密码
    confirm_password = (By.CLASS_NAME, "title")
    # 修改信息-姓名
    name = (By.CLASS_NAME, "title.short")
    # 单词量测试-学段测试
    stage_test = (By.XPATH, "//div[text()='学段测试']")

    def __init__(self, driver):
        LoginPage.__init__(self, driver)

    # 点击'未完成任务'
    def click_incomplete(self):
        self.click(self.incomplete)

    # 点击'已完成任务'
    def click_completed(self):
        self.click(self.completed)

    # 点击'荣誉榜'
    def click_honors(self):
        self.click(self.honors)

    # 点击'修改密码'
    def click_modifypassword(self):
        self.click(self.modifypassword)

    # 点击'修改信息'
    def click_modifyinformation(self):
        self.click(self.modifyinformation)

    # 点击'退出系统'
    def click_logout(self):
        self.click(self.logout)

    # 点击'单词量测试'
    def click_wordtest(self):
        self.click(self.wordtest)
