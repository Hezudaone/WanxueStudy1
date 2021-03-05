# coding=utf-8
from time import sleep

from common.common_wanxue_page import CommonWanXuePage
from setting import *
from util.file_reader import YamlReader


class MoocWanXue(CommonWanXuePage):
    # CommonWanXuePage.locators.update(YamlReader(YAML_ELEMENT['cwp']).data)
    url = PROJECT_MOOC_WANXUE_URL

    locators = YamlReader(YAML_ELEMENT['mwp']).data

    def get(self):
        '''
        打开地址
        :return:
        '''
        self.driver.get(self.url)

    def login(self, username: str = 'stu101', password: str = '123456'):
        self.mooc_login_run.click()
        self.mooc_username.send_keys(username)
        self.mooc_password.send_keys(password)
        self.mooc_loginBtn.click()

    def mooc_study_center(self):
        self.mooc_xxzx_in.click()
        self.mooc_xxzx_one.click()
        self.mooc_xxzx_pay.click()
        self.mooc_xxzx_one_fanhui.click()
        self.mooc_xxzx_jiankong.click()
        # assert self.d_xmxx_jiankong_arr.text == '创业协同团队组建 （一）', \
        #     print('学习中心视频监控无法进入')

        # # 特训任务
        # self.d_texunrenwu.click()
        # assert self.d_texunrenwu_arr.text == '查看详情', \
        #     print('特训任务无法进入')
        self.zhidaojiaoliu()
        # 测评
        self.mooc_xxzx_cp.click()
        # 通知公告
        self.mooc_xxzx_tongzhi.click()
        self.mooc_xxzx_fanhui.click()

    def zhidaojiaoliu(self):
        # 指导与交流
        self.mooc_xxzx_zdjl.click()
        self.mooc_xxzx_input.send_keys('要是我不习惯现在的团队，想换团队怎么办？')
        self.mooc_xxzx_fabu.click()
        sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()  # 确定
        self.mooc_xxzx_one_pl.click()
        self.mooc_xxzx_del.click()
        self.mooc_xxzx_queding.click()

    # 直播课
    def mooc_live_class(self):
        self.driver.set_page_load_timeout(4)
        try:

            self.mooc_live_in.click()
            self.mooc_live_one.clicl()
        except:
            self.driver.execute_script('window.stop()')
            self.mooc_live_one.click()
        self.driver.set_page_load_timeout(30)
        # self.driver.set_page_load_timeout(4)
        #
        # try:
        #     self.mooc_live_in.click()
        #     self.c_zhibo_one.click()
        # except:
        #     self.driver.execute_script('window.stop()')
        #     self.c_zhibo_one.click()
        #     self.driver.set_page_load_timeout(30)
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.mooc_live_huifang.click()
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
        #
        # self.driver.implicitly_wait(CHROME_IMP_TIME)

    # 职业评测
    def mooc_zhiyecp(self):
        self.mooc_ceping_in.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.mooc_ceping_arr.click()
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 创业资讯
    def mooc_cyzx(self):
        self.mooc_cyzx_in.click()
        self.mooc_cyzx_xinwen.click()
        self.mooc_cyzx_sou.send_keys('中关村')
        self.mooc_cyzx_cha.click()
        self.mooc_cyzx_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        assert self.mooc_cyzx_arr.text == '文章正文', \
            print('创业知识详情异常')
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 企业通识
    def mooc_qyts(self):
        self.mooc_qyts_in.click()
        self.mooc_qyts_shangye.click()
        self.mooc_qyts_sou.send_keys('干货')
        self.mooc_qyts_cha.click()
        self.mooc_qyts_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        assert self.mooc_qyts_arr.text == '文章正文', \
            print('企业通识详情异常')
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    def mooc_jingzhunqiuzhi(self):
        self.mooc_jztz_in.click()
        sleep(2)
        self.mooc_jztz_diqu.click()
        sleep(1)
        self.mooc_jztz_fenlei.click()
        sleep(1)
        self.mooc_jztz_xuqiu.click()
        sleep(1)
        self.mooc_jztz_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        # assert self.mooc_cyzx_arr.text == '产品研发高级研究助理', \
        #     print('精准投职不对劲')
        self.driver.close()
        self.driver.switch_to_window(dangqian)

