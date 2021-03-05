# coding=utf-8

import unittest

from base.des_wanxue import DesWanXue


class TestdesWanXue(unittest.TestCase):

    def get_screenshot(self):
        self.imgs.append(self.page.driver.get_screenshot_as_base64())

    @classmethod
    def setUpClass(cls):
        cls.imgs = []
        cls.page = DesWanXue()
        cls.page.get()

    def test_a_login(self):
        '''使用wxs011登录des.wanxue.cn'''
        try:
            self.page.login('wxs011', '888888')
            usernamearr = self.page.des_arr1.text
            assert usernamearr == 'wxs011', print(f'账号{usernamearr}登录失败')
        except:
            self.get_screenshot()
            raise Exception

    def tearDown(self):
        self.page.get()

    # 学习中心
    def test_b_study_center(self):
        '''学习中心'''
        try:
            self.page.study_center()
        except:
            self.get_screenshot()
            raise Exception

    # # 数字经济讲堂
    # def test_c_shuzi_jjjt(self):
    #     self.page.shuzi_jjjt()
    # 背景介绍
    def test_d_beijing_jianjie(self):
        '''背景介绍'''
        try:
            self.page.beijing_jianjie()
        except:
            self.get_screenshot()
            raise Exception

    # 产品服务
    def test_e_chanpin_fuwu(self):
        '''产品服务'''
        try:
            self.page.chanpin_fuwu()
        except:
            self.get_screenshot()
            raise Exception

    # 知识精华
    def test_f_zhishi_jinghua(self):
        '''知识精华'''
        try:
            self.page.zhishi_jinghua()
        except:
            self.get_screenshot()
            raise Exception

    # 名企解析
    def test_g_mingqi_jiexi(self):
        '''名企解析'''
        try:
            self.page.mingqi_jiexi()
        except:
            self.get_screenshot()
            raise Exception

    # 求职招聘
    def test_h_qiuzhi_zhaopin(self):
        '''求职招聘'''
        try:
            self.page.qiuzhi_zhaopin()
        except:
            self.get_screenshot()
            raise Exception

    # 资讯
    def test_i_zixun(self):
        '''资讯'''
        try:
            self.page.zixun()
        except:
            self.get_screenshot()
            raise Exception

    # 行业专家
    def test_k_hangye_zhuangjian(self):
        '''行业专家'''
        try:
            self.page.hangye_zhuangjian()
        except:
            self.get_screenshot()
            raise Exception

    # 数字经济活动
    def test_l_szjjhd(self):
        '''数字经济活动'''
        try:
            self.page.szjjhd()
        except:
            self.get_screenshot()
            raise Exception

    # 数字经济项目
    def test_m_szjjxm(self):
        '''数字经济项目'''
        try:
            self.page.szjjxm()
        except:
            self.get_screenshot()
            raise Exception

    # 职业规划
    def test_n_zhiye_guhua(self):
        '''职业规划'''
        try:
            self.page.zhiye_guhua()
        except:
            self.get_screenshot()
            raise Exception

    @classmethod
    def tearDownClass(cls):
        cls.page.driver.quit()


if __name__ == '__main__':
    unittest.main()
