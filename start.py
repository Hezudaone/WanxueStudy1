# coding=utf-8
# 测试套件  -- 包含待测的模块,类,测试方法
# 测试加载器  --决定测试模块,测试类,测试方法的加载
# 测试运行器  --记录测试过程,输出测试结果
import datetime
import os
from HwTestReport import HTMLTestReport
from os.path import join, dirname
import unittest
from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport

from setting import SUIT

CASE_PAGE = join(dirname(__file__), './case')

# 测试套件初始化
suit = unittest.TestSuite()
# 测试加载器初始化
loader = unittest.defaultTestLoader

# 加载目录下全部case
for test in SUIT:
    test_suit = loader.discover(start_dir=CASE_PAGE, pattern=test)
    # 添加进测试套件
    suit.addTest(test_suit)

now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
filename = '测试报告' + str(now)
root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
report_dir = root_dir + '/report'


with open(f'./report/{filename}.html', 'wb') as fp:
    runner = HTMLTestReport(stream=fp, verbosity=2, images=True, title='HwTestReport 测试',
                                description='带截图，带饼图，带详情', tester='狄尧')
    # 测试运行
    runner.run(suit)


# with open('./report.txt', 'w') as fp:
#     # 运行器初始化
#     runner = unittest.TextTestRunner(fp, verbosity=2)
# # 测试运行
#     runner.run(suit)

# with open(f'./report/{filename}.html', 'wb') as fp:
#     runner = HTMLTestRunner(fp, verbosity=2, tester='狄尧')
#     # 测试运行
#     runner.run(suit)

# BeautifulReport(suit).report(description='测试', filename=filename, log_path=report_dir)
