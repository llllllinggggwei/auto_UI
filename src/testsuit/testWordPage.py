from src.pageobject.wordpage import WordPage
from src.framework.logger import Logger
from src.framework import common
from config import readCofig

from selenium import webdriver

import unittest


class TestWordPage(unittest.TestCase):
    logger = Logger('word page').getlog()
    webdriver_path = common.file_abspath() + 'tools/chromedriver_mac'
    url = readCofig.test_url()
    account = readCofig.test_account()
    password = readCofig.test_password()

    def setUp(self) -> None:
        # 指定chrome的webdriver路由
        self.driver = webdriver.Chrome(executable_path=self.webdriver_path)
        self.word_page = WordPage(driver=self.driver)
        self.word_page.open_url(url=self.url)
        self.word_page.input_account(self.account)
        self.word_page.input_password(self.password)
        self.word_page.click_login()
        self.word_page.max()
        self.word_page.sleep(2)
        self.word_page.open_url(url=self.url + '#/learnWord/')

    def tearDown(self) -> None:
        self.driver.quit()

    @unittest.skip
    # 测试单词综合测评
    def testWordsEvaluation(self):
        self.word_page.click_words_evaluation()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.words_evaluation_title))
        self.word_page.sleep(1)

    @unittest.skip
    # 测试单词强化本
    def testWordReinforcement(self):
        self.word_page.click_word_reinforcement()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.word_reinforcement_title))
        self.word_page.sleep(1)

    @unittest.skip
    # 测试单元选择
    def test_unit(self):
        self.word_page.click_unit()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.preview))
        self.word_page.sleep(1)

    @unittest.skip
    # 测试线下听写练习
    def testOfflineDictation(self):
        self.xxxurl = self.url + "#/learnWord/unitItem?unitId=30361&unitName=Unit%201-1&bookName=三年级上册&bookPar=人教版"
        print(self.xxxurl)
        # self.word_page.open_url(self.url + "#/learnWord/unitItem?unitId=30361&unitName=Unit%201-1&bookName=三年级上册&bookPar=人教版")
        self.word_page.open_url(url=self.xxxurl)
        self.word_page.click_offline_dictation()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.offline_dictation_title))
        self.word_page.sleep(1)

    # @unittest.skip
    # 测试轻松预习
    def testPreview(self):
        self.xxxurl = self.url + "#/learnWord/unitItem?unitId=26440&unitName=Unit%201-1&bookName=三年级下册&bookPar=人教版"
        print(self.xxxurl)
        # self.word_page.open_url(self.url + "#/learnWord/unitItem?unitId=30361&unitName=Unit%201-1&bookName=三年级上册&bookPar=人教版")
        self.word_page.open_url(self.xxxurl)
        self.word_page.click_preview()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.preview_title))
        self.word_page.sleep(1)

    @unittest.skip
    # 测试智能速记
    def testShorthand(self):
        self.word_page.open_url(
            self.url + "#/learnWord/unitItem?unitId=30361&unitName=Unit%201-1&bookName=三年级上册&bookPar=人教版")
        self.word_page.click_shorthand()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.shorthand_title))
        self.word_page.sleep(1)

    @unittest.skip
    # 测试智能听写
    def testDictation(self):
        self.word_page.open_url(
            self.url + "#/learnWord/unitItem?unitId=30361&unitName=Unit%201-1&bookName=三年级上册&bookPar=人教版")
        self.word_page.click_dictation()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.dictation_title))
        self.word_page.sleep(1)

    @unittest.skip
    # 测试智能默写
    def testMemoryWrite(self):
        self.word_page.open_url(
            self.url + "#/learnWord/unitItem?unitId=30361&unitName=Unit%201-1&bookName=三年级上册&bookPar=人教版")
        self.word_page.click_memory_write()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.memory_write_title))
        self.word_page.sleep(1)

    @unittest.skip
    # 测试学后测试
    def testPostTest(self):
        self.word_page.open_url(
            self.url + "#/learnWord/unitItem?unitId=30361&unitName=Unit%201-1&bookName=三年级上册&bookPar=人教版")
        self.word_page.click_post_test()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.post_test_title))
        self.word_page.sleep(1)

    @unittest.skip
    # 测试快速复习
    def testReview(self):
        self.word_page.open_url(
            self.url + "#/learnWord/unitItem?unitId=30361&unitName=Unit%201-1&bookName=三年级上册&bookPar=人教版")
        self.word_page.click_review()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.review_title))
        self.word_page.sleep(1)

    @unittest.skip
    # 测试快速复习
    def testxiaoxiaole(self):
        self.word_page.open_url(
            self.url + "#/learnWord/unitItem?unitId=30361&unitName=Unit%201-1&bookName=三年级上册&bookPar=人教版")
        self.word_page.click_xiaoxiaole()
        self.word_page.sleep(1)
        self.assertTrue(self.word_page.ifElementExist(self.word_page.xiaoxiaole_title))
        self.word_page.sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=1)
