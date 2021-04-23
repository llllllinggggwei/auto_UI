import time
import os


def year_to_minute():
    return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


def year_to_day():
    return time.strftime('%Y%m%d', time.localtime(time.time()))


def file_abspath():
    return os.path.abspath(__file__).split('src')[0]