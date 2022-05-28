"""
基础逻辑:
一、运行前准备
a、获取起始编号(startNum)
   i、获取 销售项目表c列(项目编号)
  ii、取最大值加一，并返回结果
b、获取待输入的项目名称(name)
   i、获取 工时记录表的f列(销售合同编号) 和 销售项目表d列(项目名称)
  ii、取差集（只要工时记录表里比销售项目表多的内容）
 iii、筛选出'XSZS*'数据，并返回结果
c、默认屏幕截图功能开启
    在main主程序中关闭

二、运行逻辑
1、点击"增加按钮"（增加按钮的像素-,-）
2、在像素（-,-）位置添加"项目编号"
3、在像素（-,-）位置添加"项目名称"
4、点击空白处
5、根据项目编号(num)项目名称(name)遍历
"""

import pyautogui
import pandas as pd
import time

isScreenShot = True


# print(f'isScreenShot：{isScreenShot}')

# 运行逻辑
def insertNumAndName(num, name):
    # 1、点击"增加按钮"（增加按钮的像素287,85）
    addButtonPos = (287, 85)
    pyautogui.moveTo(addButtonPos)
    pyautogui.leftClick(addButtonPos)
    pyautogui.doubleClick(addButtonPos)

    # 2、在像素（466,928）位置添加"项目编号"
    numButtonPos = (466, 928)
    pyautogui.moveTo(numButtonPos)
    pyautogui.leftClick(numButtonPos)
    pyautogui.typewrite(num)
    pyautogui.hotkey('enter')

    # 3、在像素（634,928）位置添加"项目名称"
    nameButtonPos = (634, 928)
    pyautogui.moveTo(nameButtonPos)
    pyautogui.leftClick(nameButtonPos)
    pyautogui.typewrite(name)
    pyautogui.hotkey('enter')

    # 4、点击空白处
    if isScreenShot:
        time.sleep(1)
        im = pyautogui.screenshot(region=(0, 0, 1480, 1000))
        im.save(fr'screenshot/{num}-{name}.png')
    pyautogui.leftClick((1380, 900))


# 匹配 项目编号 和 项目名称
def iterateName(startNum, names):
    print('===========数据整理完成，准备录入===========')
    print('===========数据整理完成，准备录入===========')
    print('===========数据整理完成，准备录入===========')
    num = int(startNum)
    remainCount = len(names)
    if (len(names) != 0):
        for name in names:
            insertNumAndName(str(num), name)
            remainCount -= 1
            doneCount = len(names) - remainCount
            print(f'数据{num}-{name}已完成录入，共录入{doneCount}个，还有{remainCount}个待录入；')
            num += 1


# b、获取待输入的项目名称(name)
def selectNamesByPathAndStartStr(gongShiPath, xiaoShouPath, nameStart):
    # i、获取 工时记录表的f列(销售合同编号) 和 销售项目表d列(项目名称)
    gongShiExcel = pd.read_excel(gongShiPath, usecols="f")
    xiaoShouExcel = pd.read_excel(xiaoShouPath, usecols="d")
    gongShiList = set(gongShiExcel['销售合同编号'])
    xiaoShouList = set(xiaoShouExcel['项目名称'])

    # ii、取差集（只要工时记录表里比销售项目表多的内容）
    diffList = gongShiList - xiaoShouList  # 工时表比销售表多的部分
    # diffList = xiaoShouList - gongShiList  # 销售表比工时表多的部分

    # iii、筛选出'XSZS*'数据，并返回结果
    names = []
    for i in diffList:
        if str(i).startswith(nameStart):
            names.append(i)
    print(f'待提交的项目名称个数：{len(names)}')
    return names


# a、获取起始编号(startNum)
def selectStartNumByXiaoShou(xiaoShouPath):
    # i、获取 销售项目表c列(项目编号)
    xiaoShouExcel = pd.read_excel(xiaoShouPath, usecols="c")
    nums = set(xiaoShouExcel['项目编号'])
    # ii、取最大值加一，并返回结果
    if len(nums) == 0:  # 如果销售项目表没内容，则设置起始值为：00001
        return str(1).zfill(5)
    startNum = max(nums) + 1
    return str(startNum)


if __name__ == '__main__':
    print(f'屏幕尺寸：{pyautogui.size()}')
    print(f'当前鼠标位置： {pyautogui.position()}')

    # pyautogui.PAUSE = 1  # 每个步骤延迟一秒执行
    nameStart = 'XSZS'  # 支持：'XSZS'、'YP'、'KJ'等
    gongShiPath = '工时记录-2022年4月份 - To 雅楠.xlsx'
    xiaoShouPath = '销售项目-销售合同号.xlsx'

    # isScreenShot = False  # 是否打开屏幕截图，支持：True、False，默认开启
    # print(f'isScreenShot-main：{isScreenShot}')

    startNum = selectStartNumByXiaoShou(xiaoShouPath)
    print(f'获取项目编号成功，起始项目编号为:{startNum}')
    names = selectNamesByPathAndStartStr(gongShiPath, xiaoShouPath, nameStart)
    print(f'获取项目名称成功，项目名称集合为：{names}')
    iterateName(startNum, names)
    print('===========已完成，请校验===========')
    print('===========已完成，请校验===========')
    print('===========已完成，请校验===========')
