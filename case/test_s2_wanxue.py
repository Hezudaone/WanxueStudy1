# coding=utf-8

import unittest

from base.s2_wanxue import S2WanXue


class TestS2WanXue(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page = S2WanXue()
        cls.page.get()

    def test_a_login(self):
        '''使用wx98登录s2.wanxue.cn'''
        self.page.login('wx98', '888888')
        usernamearr = self.page.s2_arr1.text
        assert usernamearr == 'wx98', print(f'账号{usernamearr}登录失败')

    # 智能课
    def test_b_studyzhineng(self):
        '''智能课'''
        self.page.study_center_zhineng()
        self.page.jieduan_for()
        self.page.coures_for()
        self.page.get()

    # 外挂课
    def test_c_waigua(self):
        '''外挂课'''
        self.page.study_center_zhineng()
        self.page.study_center_waigua()

    # 直播课堂
    def test_d_live_class(self):
        '''直播课堂'''
        self.page.live_class()
        self.page.gongkai()
        self.page.shipin()

    # # 资料中心
    def test_e_information_center(self):
        '''资料中心'''
        self.page.information_center_tongkao()
        self.page.information_center_feitongkao()

    # # 综合资讯
    def test_f_zonghezixun(self):
        '''综合资讯'''
        self.page.zonghezixun()

    # # 线下解题
    def test_g_xianxiajieti(self):
        '''线下解题'''
        self.page.xianxiajietijilu()

    # 辅导矩阵
    def test_h_fudaojuzhen(self):
        '''辅导矩阵'''
        self.page.fudaojuzhen()

    # 报考决策
    def test_i_baokaojuece(self):
        '''报考决策'''
        self.page.baokaojuece()

    # 超级书库
    def test_j_chaojishuku(self):
        '''超级书库'''
        self.page.chaojishuku()

    @classmethod
    def tearDownClass(cls):
        cls.page.driver.quit()


if __name__ == '__main__':
    unittest.main()
