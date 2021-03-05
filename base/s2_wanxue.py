# coding=utf-8
from common.common_wanxue_page import CommonWanXuePage
from setting import *
from util.file_reader import YamlReader


class S2WanXue(CommonWanXuePage):
    # CommonWanXuePage.locators.update(YamlReader(YAML_ELEMENT['cwp']).data)
    url = PROJECT_S2_WANXUE_URL

    locators = YamlReader(YAML_ELEMENT['s2wp']).data

    def get(self):
        '''
        打开地址
        :return:
        '''
        self.driver.get(self.url)

    def login(self, username: str = 'stu101', password: str = '123456'):
        self.s2_login_run.click()
        self.s2_username.send_keys(username)
        self.s2_password.send_keys(password)
        self.s2_loginBtn.click()

    def study_center_zhineng(self):
        # 选择智能课
        self.s2_choice_class.click()
