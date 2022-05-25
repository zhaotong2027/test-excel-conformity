import os
import pandas as pd


def excel_dos(excelname_date):
    path = 'linlin/银行余额自动更新测试/' # 修改path
    file_list = os.listdir(path)
    file_list.sort()
    fileNum = len(file_list)
    print("在该目录下有%d个xlsx文件，只合并含记账日期的文件" % fileNum)

    truefileNum = 1;
    with pd.ExcelWriter(f'银行余额表{excelname_date}.xlsx') as writer:
        for file in file_list:
            if '~$' not in file and excelname_date in file:  # 打开的文件和不含日期的文件均不在处理之列
                file_name = os.path.join(path, file)
            else:
                continue

            old_df = pd.read_excel(file_name)
            df = pd.DataFrame(old_df)
            sheet_name = file_name[18: len(file_name) - len(excelname_date) -16]
            df.to_excel(writer, sheet_name)

            print('正在合并第%d个文件 ' % truefileNum)
            print('已完成 ' + file_name)
            truefileNum += 1;

        print("已将%d个文件合并完成" % (truefileNum - 1))


if __name__ == '__main__':
    excelname_date = '2022.5.10'
    excel_dos(excelname_date)
