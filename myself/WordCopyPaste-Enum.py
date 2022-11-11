# from docx import Document
#
# if __name__ == '__main__':
#
#     document = Document("/Users/zhaotong/Desktop/日报.docx")
#     all_tables = document.tables
#     print(type(all_tables))
#
#     i = 0
#     j = 0
#     for table in all_tables:
#         i = len(table.rows)
#         for row in table.rows:
#             j = len(row.cells)
#             for cell in row.cells:
#                 cell.text
#
#     print(i)
#     print(j)

# import calendar
#
#
# def get_daylis(year, month):
#     """
#     获取当月日期列表
#     parameter:
#         month 202011
#     return:
#         [20201101,...,20201130]
#     """
#     day_lis = []
#     for day in range(calendar.monthrange(year, month)[1] + 1)[1:]:
#         day_lis.append('%s%s%s' % (year, '%02d' % month, '%02d' % (day)))
#     return day_lis
#
#
# if __name__ == '__main__':
#     print(get_daylis(2020, 6))



import enum
class GroupInfo(enum.Enum):
    FIRST = 1, '一组', '1111'
    SECOND = 2, '二组', '2222'

    def __init__(self,group_id, group_name, group_url):
        self._group_id = group_id
        self._group_name = group_name
        self._group_url = group_url
    @property
    def group_id(self):
        return self._group_id

    @property
    def group_url(self):
        return self._group_url

    @property
    def group_name(self):
        return self._group_name


# 访问FEMALE的name
print('SECOND的name:', GroupInfo.SECOND.name)

# 访问FEMALE的value
print('SECOND的value:', GroupInfo.SECOND.value)

# 访问自定义的cn_name属性
print('SECOND的group_name:', GroupInfo.SECOND.group_name)

# 访问自定义的desc属性
print('SECOND的group_url:', GroupInfo.SECOND.group_url)
id = GroupInfo.FIRST.name
print(GroupInfo[id].group_id)
print(GroupInfo[id].name)