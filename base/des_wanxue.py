# coding=utf-8
from time import sleep

from selenium.webdriver.common.keys import Keys

from common.common_wanxue_page import CommonWanXuePage
from setting import *
from util.file_reader import YamlReader


class DesWanXue(CommonWanXuePage):
    # CommonWanXuePage.locators.update(YamlReader(YAML_ELEMENT['cwp']).data)
    url = PROJECT_DES_WANXUE_URL

    locators = YamlReader(YAML_ELEMENT['dwp']).data

    def get(self):
        '''
        打开地址
        :return:
        '''
        self.driver.get(self.url)

    def login(self, username: str = 'stu101', password: str = '123456'):
        self.des_login_run.click()
        self.des_username.send_keys(username)
        self.des_password.send_keys(password)
        self.des_loginBtn.click()

    # 学习中心
    def study_center(self):
        self.d_gjxttdgj.click()
        self.d_xiangmuxuexi.click()
        self.d_xmxx_one.click()
        self.d_pay_but.click()
        self.d_xmxx_one_fanhui.click()
        self.d_xmxx_jiankong.click()
        assert self.d_xmxx_jiankong_arr.text == '高级协同团队构建',\
            print('学习中心视频监控无法进入')

        # 特训任务
        self.d_texunrenwu.click()
        assert self.d_texunrenwu_arr.text == '查看详情',\
            print('特训任务无法进入')
        self.zhidaojiaoliu()
        # 测评
        self.d_ceping.click()
        # 通知公告
        self.d_gonggao.click()
        self.d_xxzx_fanhui.click()

    def zhidaojiaoliu(self):
        # 指导与交流
        self.d_zhidaojiaoliu.click()
        self.d_zdjl_input.send_keys('要是我不习惯现在的团队，想换团队怎么办？')
        self.d_zdjl_fabu.click()
        sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()  # 确定
        self.d_zdjl_pinglun.click()
        self.d_zdjl_shanchu.click()
        self.d_zdjl_queding.click()

    # 数字经济讲堂
    def shuzi_jjjt(self):
        self.d_szjj_in.click()
        self.d_szjj_go.click()
        self.d_szjj_ketangnum.send_keys('666')
        self.d_szjj_lijijinru_but.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        assert self.d_szjj_arr.text == '高清', \
            print('没能进入数字经济大讲堂666直播间')
        self.driver.close()
        self.driver.switch_to_window(dangqian)
        self.d_szjj_x.click()

    # 背景简介
    def beijing_jianjie(self):
        self.d_bjjs_in.click()
        assert self.d_bjjs_arr.text == '万学教育建立数字经济专业站的优势',\
            print('背景简介断言失败')

    # 产品服务
    def chanpin_fuwu(self):
        self.d_cpfw_in.click()
        self.d_cpfw_g_g.click()
        self.d_cpfw_fanhui.click()
        self.d_cpfw_g_q.click()
        self.d_cpfw_fanhui.click()
        self.d_cpfw_q_g.click()
        self.d_cpfw_fanhui.click()
        self.d_cpfw_q_q.click()
        self.d_cpfw_fanhui2.click()

    # 知识精华
    def zhishi_jinghua(self):
        self.d_zsjh_in.click()
        self.d_zsjh_list.click()
        self.d_zsjh_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.d_zsjh_fanye.click()
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 名企解析
    def mingqi_jiexi(self):
        self.d_mqjx_in.click()
        self.d_mqjx_wulianwang.click()
        self.d_mqjx_sou.send_keys('卡特彼勒')
        self.d_mqjx_cha.click()
        self.d_mqjx_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        assert self.d_mqjx_arr.text == '文章正文', \
            print('名企解析,详情也异常')
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 求职招聘
    def qiuzhi_zhaopin(self):
        self.d_qzzp_in.click()
        self.d_qzzp_didian.click()
        self.d_qzzp_fenlei.click()
        self.d_qzzp_xuqiu.click()


    # 资讯
    def zixun(self):
        self.d_zx_in.click()
        self.d_zx_shengchan.click()
        self.d_zx_sou.send_keys('宝山')
        self.d_zx_cha_but.click()
        self.d_zx_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        assert self.d_zx_arr.text == '文章正文', \
            print('创业知识详情异常')
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 行业专家
    def hangye_zhuangjian(self):
        self.d_hyzj_in.click()
        self.d_hyzj_one.click()
        self.d_hyzj_fanhui.click()


    # 数字经济活动
    def szjjhd(self):
        self.d_jjhd_in.click()
        self.d_jjhd_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.d_jjhd_arr.click()
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 数字经济项目
    def szjjxm(self):
        self.d_jjxm_in.click()
        self.d_jjxm_one.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.d_jjxm_defen.click()
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 职业规划
    def zhiye_guhua(self):
        self.d_zygh_in.click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.d_zygh_arr.click()
        self.driver.close()
        self.driver.switch_to_window(dangqian)


