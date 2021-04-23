from src.pageobject.loginpage import LoginPage
from src.framework.logger import Logger
from src.framework import common
from config import readCofig

from selenium import webdriver

import unittest


class TestLoginPage(unittest.TestCase):
    logger = Logger('loggin page').getlog()
    webdriver_path = common.file_abspath() + 'tools/chromedriver_mac'
    url = readCofig.test_url()
    account = readCofig.test_account()
    password = readCofig.test_password()

    def setUp(self) -> None:
        # 指定chrome的webdriver路径
        self.driver = webdriver.Chrome(executable_path=self.webdriver_path)

    def tearDown(self) -> None:
        self.driver.quit()

    # 测试登录
    def testLogin(self):
        driver = self.driver
        login_page = LoginPage(driver=driver)
        login_page.open_url(self.url)
        login_page.max()
        login_page.input_account(account=self.account)
        login_page.input_password(password=self.password)
        login_page.click_login()
        login_page.sleep(1)
        self.assertTrue(login_page.ifElementExist(login_page.logout_button))
        login_page.sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=1)
