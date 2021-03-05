# 项目地址
# 项目包和文件夹的路径
# 浏览器的对象属性
# 测试套件

from os.path import dirname, join
# -------------------- 超学变量 ------------------------------
# 智能课程循环次数
COURES_FOR_NUM = 8
# 智能循环答题时间
COURES_DATI_NUM = 2
# -------------------- 超学变量 ------------------------------
# ------------------------------项目地址--------------------------
# c.wanxue地址
PROJECT_S_WANXUE_URL = 'https://s.wanxue.cn/sls/category/queryList'

PROJECT_S2_WANXUE_URL = 'https://s2.wanxue.cn/sls/category/queryList'

PROJECT_C_WANXUE_URL = 'https://c.wanxue.cn/sls/category/queryList'

PROJECT_MOOC_WANXUE_URL = 'https://mooc.wanxue.cn/sls/jwcoursemodule/queryList'

PROJECT_DES_WANXUE_URL = 'https://des.wanxue.cn/sls/category/queryList#xxzx'

# ------------------------------项目地址--------------------------

# ------------------------------项目包和文件路径--------------------------
# 项目根目录
BASE_PATH = dirname(__file__)
# 各浏览器驱动文件地址
CHROME_DRIVER_PATH = join(BASE_PATH, 'drivers/chromedriver.exe')

IE_DRIVER_PATH = join(BASE_PATH, 'drivers/IEDriverServer.exe')

FIREFOX_DRIVER_PATH = join(BASE_PATH, 'drivers/geckodriver.exe')

# 项目模块路径(可存放各种路径)

# 元素配置文件的根目录
ELEMENTS_YAML_FILE_PAGE = join(BASE_PATH, 'page')
# ------------------------------项目包和文件路径--------------------------


# ------------------------------测试套件--------------------------
# 流程一测试套件
SUIT_MODULE_1 = ['test_s_wanxue.py',
                 'test_c_wanxue.py',
                 # 'test_s2_wanxue.py',
                 'test_des_wanxue.py',
                 'test_mooc_wanxue.py'
                 ]
# 流程二测试套件

# 主测试套件(多个流程可以相加组合)
SUIT = SUIT_MODULE_1

# ------------------------------测试套件--------------------------

# ------------------------------浏览器对象属性--------------------------
# 浏览器基本属性
# 无头化
HEADLESS = True

# 隐式等待时间
IMP_WAIT_TIME = 30

# 页面加载时间
PAGE_LOAD_TIME = 20

# js异步执行超时时间
SCRIPT_TIME_OUT = 20

# 浏览器启动尺寸
WINDOWS_SIZW = (1920, 1080)

# ***********************************chrome浏览器属性******
# chrome浏览器操作开关
CHROME_METHOD_MARK = True

# chrome启动参数开关
CHROME_OPTION_MARK = True

# 无头化
CHROME_HEADLESS = True

# chrome 实验性质启动参数
CHROME_EXPERIMENTAL = {
    'excludeSwitches': ['enable-automation'],
    # 'mobileEmulation': {'deviceName': 'iPhone 6'}

}

# chrome启动最大化参数
CHROME_START_MAXIMIZED = '--start-maximized'


# chrome隐式等待时间
CHROME_IMP_TIME = 30

# chrome 页面加载时间
CHROME_PAGE_LOAD_TIME = 30

# chrome js 异步执行超时时间
CHROME_SCRIPT_TIME_OUT = 30

# chrome 分辨率
CHROME_WINDOWS_SIZW = (1920, 900)
# ********chrome浏览器属性******

# ********ie浏览器属性******

# ********ie浏览器属性******

# ********FIREFOX浏览器属性******

# ********FIREFOX浏览器属性******

# ------------------------------浏览器对象属性--------------------------

# ------------------------ YAM元素配置文件 -----------------------------
YAML_ELEMENT = {
    # 超学共用类元素
    'comwp': join(ELEMENTS_YAML_FILE_PAGE, 'common_wanxue_page.yml'),
    # s.wanxue元素
    'swp': join(ELEMENTS_YAML_FILE_PAGE, 's_wanxue_page.yml'),
    # c.wanxue元素
    'cwp': join(ELEMENTS_YAML_FILE_PAGE, 'c_wanxue_page.yml'),
    # s2.wanxue元素
    's2wp': join(ELEMENTS_YAML_FILE_PAGE, 's2_wanxue_page.yml'),
    # s2.wanxue元素
    'dwp': join(ELEMENTS_YAML_FILE_PAGE, 'des_wanxue_page.yml'),
    # s2.wanxue元素
    'mwp': join(ELEMENTS_YAML_FILE_PAGE, 'mooc_wanxue_page.yml'),
    # 数学一阶段元素
    'csjp': join(ELEMENTS_YAML_FILE_PAGE, 'common_shuxueyi_jieduan_page.yml')

}
# ------------------------ YAM元素配置文件 -----------------------------

# ------------------------ WEB 元素定位方法 -----------------------------
BY_RULES = (
    'id', 'xpath', 'link text', 'partial link text',
    'name', 'tag name', 'class name', 'css selector'
)
# ------------------------ WEB 元素定位方法 -----------------------------



