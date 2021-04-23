from time import sleep


# pages基类
from selenium.common.exceptions import NoSuchElementException


class Page(object):
    """
        Page基类，所有page都应该继承该类
    """

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    # 寻找单元素或唯一元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 输入元素输入
    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    # 点击框点击
    def click(self, loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title

    # 打开url站点
    def open_url(self, url):
        self.driver.get(url)

    # 获取当前url
    def current_url(self):
        self.driver.current_url()

    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 清空输入框
    def clear(self):
        self.driver.clear()

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 强制等待
    def sleep(self, seconds):
        return sleep(seconds)

    # 屏幕最大化
    def max(self):
        self.driver.maximize_window()

    # 判断元素是否存在于页面
    def ifElementExist(self, loc):
        try:
            self.driver.find_element(*loc)
        except NoSuchElementException:
            # 打印异常信息
            print("NoSuchElementException")
            # 发生异常，说明页面中未找到该元素，返回False
            return False
        else:
            print("HaveSuchElement{}".format(loc))
            # 无异常，说明在页面中找到了该元素，返回True
            return True

    # 寻找多元素返回
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 关闭窗口
    def close(self, loc, num):
        self.find_elements(*loc)[num].click()
