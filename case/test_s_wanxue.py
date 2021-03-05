# coding=utf-8

import unittest
import warnings
from base.s_wanxue import SWanXue


class TestSWanXue(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.page = SWanXue()
        cls.page.get()

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.imgs = []

    def test_a_login(self):
        '''使用wx98,登录s.wanxue.cn'''
        try:
            self.page.login('wx98', '888888')
            usernamearr = self.page.s_arr1.text
            assert usernamearr == 'wx98', print(f'账号{usernamearr}登录失败')
        except:
            self.get_screenshot()
            raise Exception

    def tearDown(self):
        self.page.get()

    def get_screenshot(self):
        self.imgs.append(self.page.driver.get_screenshot_as_base64())
        return True

    # 智能课
    def test_b_studyzhineng(self):
        '''智能课'''
        try:
            self.page.study_center_zhineng()
            self.page.jieduan_for()
            self.page.coures_for()
            self.page.get()
        except:
            self.get_screenshot()
            raise Exception

    # 外挂课
    def test_c_waigua(self):
        '''外挂课'''
        try:
            self.page.study_center_zhineng()
            self.page.study_center_waigua()
        except:
            self.get_screenshot()
            raise Exception

    # 直播课堂
    def test_d_live_class(self):
        '''直播课堂'''
        try:
            self.page.live_class()
            self.page.gongkai()
            # self.page.shipin()
        except:
            self.get_screenshot()
            raise Exception

    # # 资料中心
    def test_e_information_center(self):
        '''资料中心'''
        try:
            self.page.information_center_tongkao()
            self.page.information_center_feitongkao()
        except:
            self.get_screenshot()
            raise Exception

    # # 综合资讯
    def test_f_zonghezixun(self):
        '''综合资讯'''
        try:
            self.page.zonghezixun()
        except:
            self.get_screenshot()
            raise Exception

    # # 线下解题
    def test_g_xianxiajieti(self):
        '''线下解题'''
        try:
            self.page.xianxiajietijilu()
        except:
            self.get_screenshot()
            raise Exception

    # 辅导矩阵
    def test_h_fudaojuzhen(self):
        '''辅导矩阵'''
        try:
            self.page.fudaojuzhen()
        except:
            self.get_screenshot()
            raise Exception

    # 报考决策
    def test_i_baokaojuece(self):
        '''报考决策'''
        try:
            self.page.baokaojuece()
        except:
            self.get_screenshot()
            raise Exception

    # 超级书库
    def test_j_chaojishuku(self):
        '''超级书库'''
        try:
            self.page.chaojishuku()
        except:
            self.get_screenshot()
            raise Exception

    @classmethod
    def tearDownClass(cls):
        cls.page.driver.quit()


if __name__ == '__main__':
    unittest.main()
