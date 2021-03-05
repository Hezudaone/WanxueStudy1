# coding=utf-8

import unittest
import warnings

from base.mooc_wanxue import MoocWanXue


class TestmoocWanXue(unittest.TestCase):

    def get_screenshot(self):
        self.imgs.append(self.page.driver.get_screenshot_as_base64())

    @classmethod
    def setUpClass(cls):
        cls.imgs = []
        cls.page = MoocWanXue()
        try:
            cls.page.get()
        except:
            cls.page.driver.execute_script('window.stop()')
            cls.page.get()

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self):
        self.page.get()

    def test_a_login(self):
        '''使用wxs011,登录mooc.wanxue.cn'''
        try:
            self.page.login('wxs011', '888888')
            usernamearr = self.page.mooc_arr1.text
            assert usernamearr == 'wxs011', print(f'账号{usernamearr}登录失败')
        except:
            self.get_screenshot()
            raise Exception

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    # 学习中心
    def test_b_(self):
        '''学习中心'''
        try:
            self.page.mooc_study_center()
        except:
            self.get_screenshot()
            raise Exception

    # 直播课堂
    def test_c_(self):
        '''直播课堂'''
        try:
            self.page.mooc_live_class()
        except:
            self.get_screenshot()
            raise Exception

    # 职业测评
    def test_d_(self):
        '''职业测评'''
        try:
            self.page.mooc_zhiyecp()
        except:
            self.get_screenshot()
            raise Exception

    # 创业资讯
    def test_e_(self):
        '''创业资讯'''
        try:
            self.page.mooc_cyzx()
        except:
            self.get_screenshot()
            raise Exception

    # 企业通识
    def test_f_(self):
        '''企业通识'''
        try:
            self.page.mooc_qyts()
        except:
            self.get_screenshot()
            raise Exception

    # 精准求职
    def test_g_(self):
        '''精准求职'''
        try:
            self.page.mooc_jingzhunqiuzhi()
        except:
            self.get_screenshot()
            raise Exception

    @classmethod
    def tearDownClass(cls):
        cls.page.driver.quit()


if __name__ == '__main__':
    unittest.main()
