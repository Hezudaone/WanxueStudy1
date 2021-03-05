# coding=utf-8
from time import sleep

from common.common_wanxue_page import CommonWanXuePage
from setting import *
from util.file_reader import YamlReader


class CWanXue(CommonWanXuePage):

    CommonWanXuePage.locators.update(YamlReader(YAML_ELEMENT['cwp']).data)
    url = PROJECT_C_WANXUE_URL
    # locators = YamlReader(YAML_ELEMENT['cwp']).data

    def get(self):
        '''
        打开地址
        :return:
        '''
        self.driver.get(self.url)

    def login(self, username: str = 'stu101', password: str = '123456'):
        self.c_login_run.click()
        self.c_username.send_keys(username)
        self.c_password.send_keys(password)
        self.c_loginBtn.click()

    def study_center_zhineng(self):
        # 选择智能课
        self.c_choice_class.click()

    # 直播课堂
    def c_live_class(self):
        self.driver.set_page_load_timeout(4)

        try:
            self.c_zhibo_in.click()
            self.c_zhibo_one.click()
        except:
            self.driver.execute_script('window.stop()')
            self.c_zhibo_one.click()
            self.driver.set_page_load_timeout(30)
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.c_zhibo_huifang.click()
        sleep(2)
        all_handles2 = self.driver.window_handles
        self.driver.switch_to_window(all_handles2[-1])
        # self.c_zhibo_queding.click()
        # self.c_zhibo_pay_but.click()
        # self.element('comwp.coures_body').send_keys(Keys.SPACE)

        for handle in self.driver.window_handles:
            if handle != dangqian:
                self.driver.switch_to_window(handle)
                self.driver.close()
                self.driver.switch_to_window(dangqian)

        self.driver.implicitly_wait(CHROME_IMP_TIME)


    # 校本课程
    def jiaobenkecheng(self):
        self.c_jiaoben_in.click()
        self.c_jb_gaojixietong.click()
        self.c_jb_xuexi.click()
        self.c_jb_zhidao.click()
        self.c_jb_ceping.click()
        self.c_jb_gonggao.click()
        self.c_jb_fanhui.click()
        self.c_jb_chuangxin.click()
        self.c_jb_jiaoben.click()
        self.c_jb_zhineng.click()

    # 职业规划
    def zhiyeguihua(self):
        self.c_zygh_in.click()
        assert self.c_zygh_arr.text == '查看报告',\
            print('职业规划没跳转成功')

    # 科研转化
    def keyanzhuanhua(self):
        self.c_kyzh_in.click()
        self.c_kyzh_chengguo.click()
        self.c_kyzh_jiaoliu.click()
        self.c_kyzh_fanhui.click()

    # 求职招聘
    def qiuzhizhaopin(self):
        self.c_qzzp_in.click()
        self.c_qzzp_qiye.click()
        self.c_qzzp_jingzong.click()
        self.c_qzzp_jingzong_in.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 创业实训
    def chuangyeshixun(self):
        self.c_cysx_in.click()
        self.c_cusx_shixun.click()
        self.c_cusx_fanhui.click()

    # 创业活动
    def chuangyehuodong(self):
        self.c_cyhd_in.click()
        self.c_cyhd_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.c_cyhd_baoming_but.click()
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 创客矩阵
    def chuangkejuzhen(self):
        # self.driver.get('https://class.wanxue.cn/index.php/Home/Index/jlsuqare.html')
        self.c_ckjz_in.click()
        self.c_ckjz_xq.click()
        self.c_ckjz_arr.click()
        self.driver.back()

    # 创业项目
    def chuangyexiangmu(self):
        self.c_cyxm_in.click()
        self.c_cyxm_xiangqing.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.c_cyxm_defen.click()
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 创业知识
    def chuangyezhishi(self):
        self.c_cyzs_in.click()
        self.c_cyzs_zlgh.click()
        self.c_cyzs_sou.send_keys('大学生')
        self.c_cyzs_cha_but.click()
        self.c_cyzs_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        assert self.c_cyzs_arr.text == '文章正文',\
            print('创业知识详情异常')
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 创业书库
    def chuangyeshuku(self):
        self.c_cysk_in.click()
        self.c_cysk_one.click()
        self.c_cysk_next.click()
        self.driver.back()

    # 创业大数据
    def chuangyedashuju(self):
        self.c_cydsj_in.click()
        self.c_cydsj_diyu.click()
        self.c_cydsj_hangye.click()
        self.c_cydsj_zhibiao.click()

    # 创业资讯
    def chuangyezixun(self):
        self.c_cyzx_in.click()
        self.c_cyzx_xinwen.click()
        self.c_cyzx_shuru.send_keys('中关村')
        self.c_cyzx_cha_but.click()
        self.c_cyzx_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        assert self.c_cyzx_arr.text == '文章正文',\
            print('创业知识详情异常')
        self.driver.close()
        self.driver.switch_to_window(dangqian)
