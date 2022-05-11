import os

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
    new_name = f'银行余额表汇总{date}'
    # nan_excel.to_excel(new_name)
    # writer = pd.ExcelWriter(f'银行余额表{date}')
    # writer.save()
    # writer.close()


def excel_dos(find_date, excelname_date, path):
    file_list = os.listdir(path)
    file_list.sort()
    fileNum = len(file_list)
    row_num = excel_find_row(find_date)
    print("在该目录下有%d个xlsx文件，只合并含记账日期的文件" % fileNum)

    for file in file_list:
        if '~$' not in file and excelname_date in file:  # 打开的文件和不含日期的文件均不在处理之列
            excelAdd = os.path.join(path, file)
        else:
            continue
        excel_print(excelAdd, row_num)


if __name__ == '__main__':
    # find_date = '2022.5.6'  # 需要计算的日期
    excelname_date = '2022.5.10'  # excel文件名上的日期
    find_date = excelname_date
    path = '银行余额自动更新测试/'
    excel_dos(find_date, excelname_date, path)
