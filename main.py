import unittest

from src.framework.HTMLTestRunner import HTMLTestRunner
from src.framework import common

from src.testsuit.testLoginPage import TestLoginPage as TLP
from src.testsuit.testHomePage import TestHomePage as THP
from src.testsuit.testWordPage import TestWordPage as TWP

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # testunit.addTest(TLP('testLogin'))
    # testunit.addTests([THP('testHonors'), THP('testModifyPassword'), THP('testModifyInformation'), THP('testLogout'), THP('testWordTest')])
    testunit.addTests([TWP('testWordsEvaluation'), TWP('testWordReinforcement'), TWP('test_unit'), TWP('testOfflineDictation'), TWP('testPreview'), TWP('testShorthand'), TWP('testDictation'), TWP('testMemoryWrite'), TWP('testPostTest'), TWP('testReview'), TWP('testxiaoxiaole')])

    # 定义报告输出路径
    htmlPath = "./report/AI-Haoji_Report{}.html".format(common.year_to_minute())
    with(open(htmlPath, 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='AI-好记测试报告',
            description='描述'
        )
        runner.run(testunit)
