# 浏览器的类型
# 浏览器的启动参数
# 浏览器的属性

from selenium.webdriver import *
from typing import Type, Union

from setting import *


# 自定义异常
class BrowserTypeError(Exception):
    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f'unsupported browser type: {self._type}'


class BROWSER:
    # driver驱动路径
    CHROME_DRIVER_PATH = CHROME_DRIVER_PATH
    FIREFOX_DRIVER_PATH = FIREFOX_DRIVER_PATH
    IE_DRIVER_PATH = IE_DRIVER_PATH
    # 分辨率
    WINDOWS_SIZW = WINDOWS_SIZW
    # 隐式等待时间
    IMP_TIME = IMP_WAIT_TIME
    # 页面加载时间
    PAGE_LOAD_TIME = PAGE_LOAD_TIME
    # js执行时间
    SCRIPT_TIME_OUT = SCRIPT_TIME_OUT
    # 无头化
    HEADLESS = True

    def __init__(self, browser_type: Type[Union[Firefox, Chrome, Ie, Edge, Opera]] = Chrome,
                 option_type: Type[Union[FirefoxOptions, ChromeOptions, IeOptions]] = ChromeOptions,
                 driver_path: str = CHROME_DRIVER_PATH):
        if not issubclass(browser_type, (Firefox, Chrome, Ie, Edge, Opera)):
            raise BrowserTypeError(browser_type)

        if not issubclass(option_type, (FirefoxOptions, ChromeOptions, IeOptions)):
            raise BrowserTypeError(option_type)

        if not isinstance(driver_path, str):
            raise TypeError

        self._path = driver_path
        self._browser = browser_type
        self._option = option_type

    @property
    def options(self):
        '''
        浏览器特等的操作,在子类中实现
        :return:
        '''
        return

    def browser(self):
        '''
        启动浏览器,返回浏览器实例
        :return:
        '''
        return


class CHROME(BROWSER):

    # 启动参数开关
    OPTION_MARK = CHROME_OPTION_MARK

    # 操作开关
    METHOD_MARK = CHROME_METHOD_MARK

    # 无头化
    HEADLESS = CHROME_HEADLESS
    # 隐式等待时间
    IMP_TIME = CHROME_IMP_TIME
    # 页面加载时间
    PAGE_LOAD_TIME = CHROME_PAGE_LOAD_TIME
    # js 异步执行超时时间
    SCRIPT_TIME_OUT = CHROME_SCRIPT_TIME_OUT
    # 分辨率
    WINDOWS_SIZW = CHROME_WINDOWS_SIZW
    # 全屏启动参数
    START_MAX = CHROME_START_MAXIMIZED

    EXP = CHROME_EXPERIMENTAL

    @property
    def options(self):
        if self.OPTION_MARK:
            chrome_option = self._option()
            chrome_option.add_argument(self.START_MAX)

            for k, v in self.EXP.items():
                chrome_option.add_experimental_option(k, v)
            chrome_option.headless = self.HEADLESS
            return chrome_option
        return

    @property
    def browser(self):
        if self.options:
            chrome = self._browser(self._path, options=self.options)
        else:
            chrome = self._browser(self._path)

        if self.METHOD_MARK:
            chrome.implicitly_wait(self.IMP_TIME)
            chrome.set_script_timeout(self.SCRIPT_TIME_OUT)
            chrome.set_page_load_timeout(self.PAGE_LOAD_TIME)
            chrome.set_window_size(*self.WINDOWS_SIZW)
            chrome.desired_capabilities["pageLoadStrategy"] = "none"
        return chrome


# with CHROME().browser as _chrome:
#     _chrome.get('https://s.wanxue.cn/sls/category/queryList')
#     from time import sleep
#     sleep(5)

class IE(BROWSER):

    CLEAN_SESSION = True

    def __init__(self):
        super(IE, self).__init__(
            browser_type=Ie,
            option_type=IeOptions,
            driver_path=super().IE_DRIVER_PATH
        )
    @property
    def options(self):
        ie_option = self._option()
        ie_option.ensure_clean_session = self.CLEAN_SESSION
        return ie_option

    @property
    def browser(self):
        ie = self._browser(self._path, options=self.options)
        ie.implicitly_wait(self.IMP_TIME)
        ie.set_page_load_timeout(self.PAGE_LOAD_TIME)
        ie.set_script_timeout(self.SCRIPT_TIME_OUT)
        ie.maximize_window()
        return ie


# with IE().browser as _ie:
#     _ie.get('https://s.wanxue.cn/sls/category/queryList')
#     from time import sleep
#     sleep(5)
