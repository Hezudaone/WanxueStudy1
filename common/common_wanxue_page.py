from datetime import time
from time import sleep

from selenium.webdriver.common.keys import Keys

from common.page import Page
from setting import *
from util.file_reader import YamlReader


class CommonWanXuePage(Page):
    locators = YamlReader(YAML_ELEMENT['comwp']).data
    elements_yml = YAML_ELEMENT

    locators.update(YamlReader(YAML_ELEMENT['csjp']).data)

    # 阶段选择
    def jieduan_for(self):
        # 进入智能课
        self.element('comwp.go_into').click()
        # 点击开始学习按钮
        # self.driver.back()
        # self.Start_learning.click()
        # # 开始智能课程流程
        data = YamlReader(YAML_ELEMENT['csjp']).data
        for i in data:


            self.element(f'csjp.{i}').click()
            sleep(3)
            # 满足 100% 选择下一个阶段
            if self.element('comwp.go_to_study_but').text == '超级智能学习 > 已完成':
                continue
            else:
                # 不满足100% 则进入超级智能学习课程
                self.element('comwp.go_to_study_but').click()

                return

    # 教材
    def jiaocai(self):
        self.element('comwp.next_page_button').click()
        self.element('comwp.coures_next_but').click()

    # 课程
    def kecheng(self):
        self.element('comwp.pay_kecheng').click()
        sleep(2)
        self.element('comwp.coures_next_but').click()

    # 习题
    def xiti(self):
        ...

    # 解析
    def jiexi(self):
        try:
            self.element('comwp.jiexi_flag')
            sleep(3)
            self.element('comwp.coures_next_but').click()
            self.element('comwp.okgo_but').click()
        except:

            self.element('comwp.coures_next_but').click()
            self.element('comwp.rengongzhidao').click()

    # 智能课程学习循环
    def coures_for(self):
        for _ in range(COURES_FOR_NUM):
            try:  # 没有下一步按钮有两种情况  习题组提交 和 学完返回
                self.driver.implicitly_wait(COURES_DATI_NUM)
                self.element('comwp.coures_next_but')
            except:
                # 尝试提交
                self.element('comwp.coures_body').send_keys(Keys.ALT, 's')
                # self.coures_body.send_Keys(Keys.ALT, 's')
                try:
                    # 点击提交按钮,如果不存在,则返回
                    self.element('comwp.tijiao_but').click()
                except:
                    self.element('comwp.fanhui_but').click()
                    return

            if '课程' in self.element('comwp.coures_next_but').text:
                self.jiaocai()
                continue

            if '习题组' in self.element('comwp.coures_next_but').text:
                self.kecheng()
                continue

            if '学习任务包' in self.element('comwp.coures_next_but').text:
                self.jiexi()
                continue
        self.driver.implicitly_wait(CHROME_IMP_TIME)

    # 外挂课
    def study_center_waigua(self):
        element_list = ('comwp.waigua_jingxi', 'comwp.waigua_changgui', 'comwp.waigua_teshe')
        for element in element_list:
            self.element(element).click()
            self.study_center_waigua_pay()
        self.element('comwp.fanhuishouye').click()

    def study_center_waigua_pay(self):
        self.elements('comwp.waigua_study_but')[3].click()
        self.element('comwp.waigua_pay_but').click()
        self.driver.back()
        self.driver.back()

    # 直播课堂
    def live_class(self):
        self.element('comwp.go_live_class_but').click()
        self.element('comwp.my_live_class_but').click()
        self.element('comwp.my_live_class_arr')
        self.driver.back()

    # 公开
    def gongkai(self):
        gk_list = (
            'comwp.gongkaike_yingyu', 'comwp.gongkaike_shuxue',
            'comwp.gongkaike_zhengzhi', 'comwp.gongkaike_jingguan',
            'comwp.gongkaike_fashuo', 'comwp.gongkaike_yixue',
            'comwp.gongkaike_fanshuo'
        )
        for element in gk_list:
            try:
                self.element(element).click()
                sleep(2)
                self.element('comwp.live_huifang_but').click()
                all_handels = self.driver.window_handles
                self.driver.switch_to_window(all_handels[-1])
                self.driver.switch_to_frame('video')
                sleep(2)
                self.element('comwp.gongkaike_ok').click()
                self.element('comwp.gongkaike_pay_but').click()
                self.driver.switch_to_default_content()  # 回到主页面
                self.driver.close()
                self.driver.switch_to_window(all_handels[0])
            except:
                continue
            return

    # # 直播
    # def zhibo(self):
    #     ...

    # 视频
    def shipin(self):
        dangqian = self.driver.current_window_handle
        self.element('comwp.shipin_yingyu').click()
        self.element('comwp.shipin_go_in').click()
        sleep(2)
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.elements('comwp.shipin_go_look')[0].click()
        all_handles2 = self.driver.window_handles
        self.driver.switch_to_window(all_handles2[-1])
        sleep(2)
        self.element('comwp.coures_body').send_keys(Keys.SPACE)
        for handle in self.driver.window_handles:
            if handle != dangqian:
                self.driver.switch_to_window(handle)
                self.driver.close()
                self.driver.switch_to_window(dangqian)

        # sp_list =(
        #     'comwp.shipin_mianfei',
        #     'comwp.shipin_dingxiao',
        #     'comwp.shipin_zhengzhi', 'comwp.shipin_yingyu',
        #     'comwp.shipin_shuxue', 'comwp.shipin_tongkao'
        # )
        #
        # dangqian = self.driver.current_window_handle
        # for element in sp_list:
        #     try:
        #         self.element(element).click()
        #         self.element('comwp.shipin_go_in').click()
        #         all_handles = self.driver.window_handles
        #         self.driver.switch_to_window(all_handles[-1])
        #         self.elements('comwp.shipin_go_look')[0].click()
        #         all_handles2 = self.driver.window_handles
        #         self.driver.switch_to_window(all_handles2[-1])
        #         sleep(3)
        #         self.element('comwp.shipin_pay_but').click()
        #         for handle in self.driver.window_handles:
        #             if handle != dangqian:
        #                 self.driver.switch_to_window(handle)
        #                 self.driver.close()
        #                 self.driver.switch_to_window(dangqian)
        #     except:
        #         for handle in self.driver.window_handles:
        #             if handle != dangqian:
        #                 self.driver.switch_to_window(handle)
        #                 self.driver.close()
        #                 self.driver.switch_to_window(dangqian)
        #         continue
        #     return
    # 资料中心 统考
    def information_center_tongkao(self):
        self.element('comwp.information_run').click()
        self.element('comwp.tongkao_information').click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.element('comwp.information').click()
        self.element('comwp.dingdan_but')
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 资料中心 非统考
    def information_center_feitongkao(self):
        self.element('comwp.feitongkao_sheng').click()
        self.element('comwp.feitongkao_yanxiao').click()
        self.element('comwp.feitongkao_input').send_keys('金融')
        self.element('comwp.feitongkao_but').click()
        self.element('comwp.feitongkao_zhuanye').click()
        self.element('comwp.feitongkao_in').click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.element('comwp.feitongkao_zhenti').click()
        self.element('comwp.dingdan_but')
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 综合资讯
    def zonghezixun(self):
        self.element('comwp.zonghezixun').click()
        self.element('comwp.zhaoshengjianzhang').click()
        self.element('comwp.zixun_one').click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        assert self.element('comwp.wenzhangzhengwen').text == '文章正文'
        self.driver.close()
        self.driver.switch_to_window(dangqian)

    # 线下解题记录
    def xianxiajietijilu(self):
        self.element('comwp.xianxiajieti').click()
        self.element('comwp.xianxia_shuxue').click()
        self.element('comwp.xianxia_run_in').click()
        self.element('comwp.xianxia_fanhui').click()

    # 辅导矩阵
    def fudaojuzhen(self):
        self.element('comwp.fudao_juzhen').click()
        self.element('comwp.fudao_zhuanqu').click()
        self.element('comwp.fudao_fanhui').click()
        self.element('comwp.fudao_jiaoliu').click()
        self.element('comwp.fudao_jiaoliu_fanhui').click()

    # 报考决策
    def baokaojuece(self):
        self.element('comwp.baokaojuece_in').click()
        self.element('comwp.baokao_diqu').click()
        self.element('comwp.baokao_danwei').click()
        self.element('comwp.baokao_cha_but').click()
        assert self.element('comwp.baokao_arr').text == '清华大学'

    # 超级书库
    def chaojishuku(self):
        self.element('comwp.chaoji_books').click()
        self.element('comwp.shuxue_list').click()
        self.element('comwp.book_in').click()
        dangqian = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.switch_to_window(all_handles[-1])
        self.element('comwp.xiayiye').click()
        self.driver.close()
        self.driver.switch_to_window(dangqian)
    '''
    
    '''
