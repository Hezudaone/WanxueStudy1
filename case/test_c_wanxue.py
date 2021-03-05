# coding=utf-8

import unittest
import warnings

from base.c_wanxue import CWanXue


class TestCWanXue(unittest.TestCase):
    def get_screenshot(self):
        self.imgs.append(self.page.driver.get_screenshot_as_base64())
        return True

    @classmethod
    def setUpClass(cls):
        cls.imgs = []
        while True:
            try:
                cls.page = CWanXue()
                cls.page.get()
                break
            except:
                ...

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self):
        self.page.get()

    def test_a_login(self):
        '''wx98登录c.wanxue.cn'''
        try:
            self.page.login('wx98', '888888')
            assert self.page.c_arr1.text == 'wx98', print(f'账号{page.arr1.text}登录失败')
        except:
            self.get_screenshot()
            raise Exception

    def test_b_studyzhineng(self):
        '''学习中心'''
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

    # 校本课程
    def test_d_jiaobenkecheng(self):
        '''校本课程'''
        try:
            self.page.jiaobenkecheng()
        except:
            self.get_screenshot()
            raise Exception

    # 科研转化
    def test_e_keyanzhuanhua(self):
        '''科研转化'''
        try:
            self.page.keyanzhuanhua()
        except:
            self.get_screenshot()
            raise Exception

    # 求职招聘
    def test_f_qiuzhizhaopin(self):
        '''求职招聘'''
        try:
            self.page.qiuzhizhaopin()
        except:
            self.get_screenshot()
            raise Exception

    # 创业实训
    def test_g_chuangyeshixun(self):
        '''创业实训'''
        try:
            self.page.chuangyeshixun()
        except:
            self.get_screenshot()
            raise Exception

    # 创业活动
    def test_h_chuangyehuodong(self):
        '''创业活动'''
        try:
            self.page.chuangyehuodong()
        except:
            self.get_screenshot()
            raise Exception

    # 创客矩阵
    def test_i_chuangkejuzhen(self):
        '''创客矩阵'''
        try:
            self.page.chuangkejuzhen()
        except:
            self.get_screenshot()
            raise Exception

    # 创业项目
    def test_j_chuangyexiangmu(self):
        '''创业项目'''
        try:
            self.page.chuangyexiangmu()
        except:
            self.get_screenshot()
            raise Exception

    # 创业知识
    def test_k_chuangyezhishi(self):
        '''创业知识'''
        try:
            self.page.chuangyezhishi()
        except:
            self.get_screenshot()
            raise Exception

    # 创业书库
    def test_l_chuangyeshuku(self):
        '''创业书库'''
        try:
            self.page.chuangyeshuku()
        except:
            self.get_screenshot()
            raise Exception

    # 创业大数据
    def test_m_chuangyedashuju(self):
        '''创业大数据'''
        try:
            self.page.chuangyedashuju()
        except:
            self.get_screenshot()
            raise Exception

    # 创业资讯
    def test_n_chuangyezixun(self):
        '''创业资讯'''
        try:
            self.page.chuangyezixun()
        except:
            self.get_screenshot()
            raise Exception

    @classmethod
    def tearDownClass(cls):
        cls.page.driver.quit()


if __name__ == '__main__':
    unittest.main()
