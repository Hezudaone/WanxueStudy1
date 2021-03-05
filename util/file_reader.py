# coding=utf-8
from os.path import exists
from yaml import safe_load_all, safe_load
from xlrd import open_workbook


class File:

    def __init__(self, file_path: str):
        if not exists(file_path):
            raise FileNotFoundError
        self._file_path = file_path
        self._data = None


class YamlReader(File):

    def __init__(self, yml_path: str, multi: bool = False):
        '''  
        :param yml_path: 文件路径
        :param multi: 分节处理 true 为多节
        '''
        super(YamlReader, self).__init__(yml_path)
        self._multi = multi

    @property
    def data(self):
        if not self._data:
            with open(self._file_path, 'rb') as fp:
                if self._multi:
                    self._data = list(safe_load_all(fp))
                else:
                    self._data = safe_load(fp)

        return self._data


class ExcelReader(File):
    def __init__(self, excel_path: str, sheet: [str, int], excel_title: bool = True):
        '''

        :param excel_path: 路径
        :param sheet: 表
        :param excel_title: 是否读取表头
        '''
        super(ExcelReader, self).__init__(excel_path)
        self._sheet = sheet
        self._excel_title = excel_title
        self._data = []

    @property
    def data(self):
        if not self._data:
            work_book = open_workbook(self._file_path)
            if not isinstance(self._sheet, (int, str)):
                raise TypeError(
                    'excel文件的表格: {}不存在'.format(self._sheet)
                )
            if isinstance(self._sheet, int):
                s = work_book.sheet_by_index(self._sheet)
            else:
                s = work_book.sheet_by_name(self._sheet)

            if self._excel_title:
                '''
                    [{a:a1,b:b1},{a:a2,b:b2}]
                '''
                title = s.row_values(0)
                for col in range(1, s.nrows):
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                '''
                    [[a1,b1],[b2,b2]]
                '''
                for col in range(0, s.nrows):
                    self._data.append(s.row_values(col))

        return self._data

# obj = YamlReader(r'D:\xuexi\SuperStudy\newstudy\config\demo.yml')
# print(obj.data)


# obj = ExcelReader(r'D:\xuexi\SuperStudy\newstudy\config\demodata.xlsx',
#                   sheet=0, excel_title=False).data
# print(obj)
