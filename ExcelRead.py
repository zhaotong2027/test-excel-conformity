import pandas as pd


def excel_find_row(date):
    dates = date.split('.')
    month = dates[1]
    day = dates[2]
    demo_df = pd.read_excel(f'银行余额自动更新测试/（周莹莹）聚英-2022年银行日记账2022.5.10.xlsx')
    for indexs in demo_df.index:
        for i in range(len(demo_df.loc[indexs].values)):
            if (str(demo_df.loc[indexs].values[i]) == month and str(demo_df.loc[indexs].values[i + 1]) == day):
                row = (int)(str(indexs - 1).rstrip('L'))
                return row


def excel_print(excelAdd, row_num):
    result = pd.read_excel(excelAdd)
    name = result.columns[0]
    print(name)
    result = pd.read_excel(excelAdd, header=1)
    data = result.iloc[row_num:row_num + 1]
    print(data[0:8])
    print()


def excel_print2(excelAdd, row_num):
    result = pd.read_excel(excelAdd)
    name = result.columns[0]
    result = pd.read_excel(excelAdd, header=1)
    data = result.iloc[row_num:row_num + 1]
    # print(result.columns[0:6])
    sum = {'name': name,
           'data': data}
    return sum

def excel_new(date):
    nan_excel = pd.DataFrame()
    new_name = f'银行余额表{date}'
    # nan_excel.to_excel(new_name)
    # writer = pd.ExcelWriter(f'银行余额表{date}')
    # writer.save()
    # writer.close()


# def excel_write(find_date, sum):
#     nan_excel = pd.DataFrame()
#     nan_excel.to_excel(f'银行余额表{find_date}')
#     writer = pd.ExcelWriter(f'银行余额表{find_date}')
#     writer.save()
#     writer.close()


def excel_dos(find_date, excelname_date, names):
    # excel_new(find_date)
    row_num = excel_find_row(find_date)
    for name in names:
        # print(f'正在读取：{name}-2022年银行日记账{date}.xlsx')
        excelAdd = f'银行余额自动更新测试/{name}-2022年银行日记账{excelname_date}.xlsx'
        excel_print(excelAdd, row_num)


if __name__ == '__main__':
    find_date = '2022.5.6'
    excelname_date = '2022.5.10'
    names = ['（焦剑利）万圣', '（张晨光）坤宜', '（周莹莹）聚英']
    excel_dos(find_date, excelname_date, names)
