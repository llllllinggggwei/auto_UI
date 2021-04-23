import configparser
import os


config = configparser.ConfigParser()
dir = os.path.abspath('.').split('src')[0]
config.read(dir + "/config/config.ini")


# 根据配置文件获取测试url
def test_url():
    url = config.get("testServer", "URL")
    return url


def test_account():
    return config.get("account", "username")

def test_password():
    return config.get("account", "password")