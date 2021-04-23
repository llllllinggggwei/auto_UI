from src.pageobject.homepage import HomePage
from src.framework.logger import Logger
from src.framework import common
from config import readCofig

from selenium import webdriver

import unittest


class TestHomePage(unittest.TestCase):
    logger = Logger('home page').getlog()
    webdriver_path = common.file_abspath() + 'tools/chromedriver_mac'
    url = readCofig.test_url()
    account = readCofig.test_account()
    password = readCofig.test_password()

    def setUp(self) -> None:
        # 指定chrome的webdriver路由
        self.driver = webdriver.Chrome(executable_path=self.webdriver_path)
        self.home_page = HomePage(driver=self.driver)
        self.home_page.open_url(url=self.url)
        self.home_page.input_account(self.account)
        self.home_page.input_password(self.password)
        self.home_page.click_login()
        self.home_page.max()
        self.home_page.sleep(2)
        # self.home_page.open_url(url=self.url + '/#/homepage/')

    def tearDown(self) -> None:
        self.driver.quit()

    # @unittest.skip
    # 测试荣誉榜
    def testHonors(self):
        self.home_page.click_honors()
        self.home_page.sleep(1)
        self.assertTrue(self.home_page.ifElementExist(self.home_page.total_tanking))
        self.home_page.sleep(1)
        self.home_page.close(self.home_page.close_button, num=2)
        self.home_page.sleep(1)

    # @unittest.skip
    # 测试修改密码
    def testModifyPassword(self):
        self.home_page.click_modifypassword()
        self.home_page.sleep(1)
        self.assertTrue(self.home_page.ifElementExist(self.home_page.confirm_password))
        self.home_page.sleep(1)
        self.home_page.close(self.home_page.close_button, num=1)
        self.home_page.sleep(1)

    # 测试修改用户信息
    def testModifyInformation(self):
        self.home_page.click_modifyinformation()
        self.home_page.sleep(1)
        self.assertTrue(self.home_page.ifElementExist(self.home_page.name))
        self.home_page.sleep(1)
        self.home_page.close(self.home_page.close_button, num=1)
        self.home_page.sleep(1)

    # 测试登出系统
    def testLogout(self):
        self.home_page.click_logout()
        self.home_page.sleep(1)
        self.assertTrue(self.home_page.ifElementExist(self.home_page.login_button))
        self.home_page.sleep(1)

    # 测试"单词量测试"
    def testWordTest(self):
        self.home_page.click_wordtest()
        self.home_page.sleep(1)
        self.assertTrue(self.home_page.ifElementExist(self.home_page.stage_test))
        self.home_page.sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=1)
