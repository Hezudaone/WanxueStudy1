from selenium.webdriver import ActionChains

from base.browser import CHROME
from setting import *
from util.file_reader import YamlReader


class Page:
    url = None
    # 定位器
    locators = {}
    browser = CHROME

    def __init__(self, page=None):
        if page:
            self.driver = page.driver
        else:
            self.driver = self.browser().browser

    def __getattr__(self, loc):
        if loc not in self.locators.keys():
            raise Exception

        by, val = self.locators[loc]
        return self.driver.find_element(by, val)
# -------------------------------------------------------------使用继承方式实现
    # 子类重写,获取通用配置文件中具体项目的元素配置文件的字典
    elements_yml = {}
    # 缓存动态读取的yaml元素配置文件的解析结果
    elements_pool = {}
    # driver = None

    def _locator(self, expression: str = 'cp.username'):
        '''
        解析元素表达式的方法
        :param expression:
        :return:
        '''
        name, value = expression.split('.')
        if name not in self.elements_yml:
            raise Exception('元素配置文件的别名: {}无法识别!'.format(name))

        if name not in self.elements_pool:
            self.elements_pool[name] = YamlReader(self.elements_yml[name]).data

            if self.elements_pool[name][value][0] not in BY_RULES:
                raise Exception(
                    f'无法识别定位方法:{self.elements_pool[name][value]}'
                )
            return self.elements_pool[name][value]
        return self.elements_pool[name][value]

    @classmethod
    def cls_locator(cls, expression: str = 'cp.username'):
        '''

        :param expression:
        :return:
        '''
        name, value = expression.split('.')
        if name not in cls.elements_yml:
            raise Exception('元素配置文件的别名: {}无法识别!'.format(name))

        if name not in cls.elements_pool:
            cls.elements_pool[name] = YamlReader(cls.elements_yml[name]).data

            if cls.elements_pool[name][value][0] not in BY_RULES:
                raise Exception(
                    f'无法识别定位方法:{cls.elements_pool[name][value]}'
                )
            return cls.elements_pool[name][value]
        return cls.elements_pool[name][value]

    def element(self, loc: str):
        '''
        定位元素的方法
        :param loc:
        :return:
        '''
        return self.driver.find_element(*self._locator(loc))

    def elements(self, loc: str):
        '''
        定位元素组的方法
        :param loc:
        :return:
        '''
        return self.driver.find_elements(*self._locator(loc))

    @classmethod
    def cls_element(cls, loc: str):
        '''
        定位元素类方法
        :param loc:
        :return:
        '''
        return cls.driver.find_element(*cls.cls_locator(loc))

    @classmethod
    def cls_elements(cls, loc: str):
        '''
        定位元素类方法
        :param loc:
        :return:
        '''
        return cls.driver.find_elements(*cls.cls_locator(loc))

    def perform(self, loc: str):
        '''
        鼠标悬停在该元素
        :return:
        '''
        el = self.driver.find_element(*self._locator(loc))
        ActionChains(self.driver).move_to_element(el).perform()

    # # 获取新打开的窗口
    # def get_new_handle(self):
    #     all_handels = self.driver.window_handles
    #     self.driver.switch_to_window(all_handels[-1])
    #     return self.driver.current_window_handle
    #
    # # 返回第一个窗口
    # def get_one_handle(self):
    #     self.driver.close()
    #     all_handels = self.driver.window_handles
    #     self.driver.switch_to_window(all_handels[0])
    #
    # # 关闭最后一个选择最后一个
    # def close_handle(self):
    #     all_handels = self.driver.window_handles
    #     self.driver.switch_to_window(all_handels[-1])
    #     self.driver.close()
    #     self.driver.switch_to_window(all_handels[-2])
