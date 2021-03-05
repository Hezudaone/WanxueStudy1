# coding=utf-8
from common.common_wanxue_page import CommonWanXuePage
from setting import *
from util.file_reader import YamlReader


class SWanXue(CommonWanXuePage):
    CommonWanXuePage.locators.update(YamlReader(YAML_ELEMENT['swp']).data)
    url = PROJECT_S_WANXUE_URL

    # locators = YamlReader(YAML_ELEMENT['swp']).data

    def get(self):
        '''
        打开地址
        :return:
        '''
        self.driver.get(self.url)

    def login(self, username: str = 'stu101', password: str = '123456'):
        self.s_login_run.click()
        self.s_username.send_keys(username)
        self.s_password.send_keys(password)
        self.s_loginBtn.click()

    def study_center_zhineng(self):
        # 选择智能课
        self.s_choice_class.click()

