from src.pageobject.loginpage import LoginPage
from selenium.webdriver.common.by import By


# 主页面
class WordPage(LoginPage):
    # 元素集

    # '单词综合测评'按钮
    words_evaluation = (By.XPATH, "//div[text()='单词综合测评']")
    # '单词强化本'按钮
    word_reinforcement = (By.XPATH, "//div[text()='单词强化本']")
    # '选择单元'按钮 e.g.:选择单元unit 1-1
    unit = (By.XPATH, "//div[text()='Unit 1-1']")
    # 线下听写练习按钮
    offline_dictation = (By.XPATH, "//span[text()='线下听写练习']")
    # 轻松预习
    preview = (By.XPATH, "//div[text()='智能听写']")
    # 智能速记
    shorthand = (By.XPATH, "//div[text()='智能速记']")
    # 智能听写
    dictation = (By.XPATH, "//div[text()='智能听写']")
    # 智能默写
    memory_write = (By.XPATH, "//div[text()='智能默写']")
    # 学后测试
    post_test = (By.XPATH, "//div[text()='学后测试']")
    # 快速复习
    review = (By.XPATH, "//div[text()='快速复习']")
    # 单词消消乐
    xiaoxiaole = (By.XPATH, "//div[text()='单词消消乐']")

    # 验证元素
    # '单词综合测评'按钮
    words_evaluation_title = (By.XPATH, "//div[text()='全选']")
    # '单词强化本'按钮
    word_reinforcement_title = (By.XPATH, "//span[text()='单词强化本，今日强化内容']")

    # '选择单元'按钮 e.g.:选择单元unit 1-1 验证有轻松预习按钮"preview"即可

    # 线下听写练习按钮
    offline_dictation_title = (By.XPATH, "//span[text()='线下听写']")
    # 轻松预习窗口
    preview_title = (By.XPATH, "//span[text()='轻松预习']")
    # 智能速记窗口
    shorthand_title = (By.XPATH, "//span[text()='智能速记']")
    # 智能听写窗口
    dictation_title = (By.XPATH, "//span[text()='智能听写']")
    # 智能默写窗口
    memory_write_title = (By.XPATH, "//span[text()='智能默写']")
    # 学后测试窗口
    post_test_title = (By.XPATH, "//span[text()='学后测试']")
    # 快速复习窗口
    review_title = (By.XPATH, "//span[text()='快速复习']")
    # 单词消消乐窗口
    xiaoxiaole_title = (By.XPATH, "//span[text()='退出']")

    # 点击'单词综合测评'按钮
    def click_words_evaluation(self):
        self.click(self.words_evaluation)

    # 点击'单词强化本'按钮
    def click_word_reinforcement(self):
        self.click(self.word_reinforcement)

    # '选择单元'按钮 e.g.:选择单元unit 1-1
    def click_unit(self):
        self.click(self.unit)

    # 线下听写练习按钮
    def click_offline_dictation(self):
        self.click(self.offline_dictation)

    # 轻松预习
    def click_preview(self):
        self.click(self.preview)

    # 智能速记
    def click_shorthand(self):
        self.click(self.shorthand)

    # 智能听写
    def click_dictation(self):
        self.click(self.dictation)

    # 智能默写
    def click_memory_write(self):
        self.click(self.memory_write)

    # 学后测试
    def click_post_test(self):
        self.click(self.post_test)

    # 快速复习
    def click_review(self):
        self.click(self.review)

    # 单词消消乐
    def click_xiaoxiaole(self):
        self.click(self.xiaoxiaole)
