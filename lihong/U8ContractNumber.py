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
addButtonPos = (287, 85)
numButtonPos = (466, 928)
nameButtonPos = (634, 928)
clickBlankPos = (1380, 900)


# 运行逻辑
def insertNumAndName(num, name):
    # 1、点击"增加按钮"（增加按钮的像素287,85）
    pyautogui.moveTo(addButtonPos)
    pyautogui.leftClick(addButtonPos)
    pyautogui.doubleClick(addButtonPos)

    # 2、在像素（466,928）位置添加"项目编号"
    pyautogui.moveTo(numButtonPos)
    pyautogui.leftClick(numButtonPos)
    # pyperclip.copy(num)
    # pyautogui.hotkey('ctrl', 'v')  # mac系统ctrl需改成command
    pyautogui.typewrite(num)
    time.sleep(1)
    pyautogui.hotkey('enter')

    # 3、在像素（634,928）位置添加"项目名称"
    pyautogui.moveTo(nameButtonPos)
    pyautogui.leftClick(nameButtonPos)
    # pyperclip.copy(name)
    # pyautogui.hotkey('ctrl', 'v')  # mac系统ctrl需改成command
    pyautogui.typewrite(name)
    time.sleep(1)
    pyautogui.hotkey('enter')

    # 4、点击空白处
    if isScreenShot:
        time.sleep(1)
        im = pyautogui.screenshot()
        im.save(fr'screenshot/{num}-{name}.png')
    pyautogui.leftClick(clickBlankPos)


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
    print('===========已完成，请校验===========')
    print('===========已完成，请校验===========')
    print('===========已完成，请校验===========')


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


'''
windows系统窗口移动快捷键 windows+左 windows+右
注释快捷键 ctrl+/
运行快捷键 鼠标点击一下run的打印窗口（就是打印出屏幕尺寸的窗口） ctrl+F5 
运行过程中强制结束快捷键 ctrl+F2

【【【测屏幕尺寸过程】】】
1、把程序放到要测的屏幕下
2、138行以后的功能注释掉
3、鼠标点击【run的打印窗口（窗口中任意位置）】后，把鼠标移动到要测的位置（这一步不要点击），ctrl+F5 快捷键运行

务必保持输入法为英文！
务必保持输入法为英文！
务必保持输入法为英文！
'''
if __name__ == '__main__':
    print(f'屏幕尺寸：{pyautogui.size()}')
    print(f'当前鼠标位置： {pyautogui.position()}')


    # pyautogui.PAUSE = 1  # 每个步骤延迟一秒执行
    nameStart = 'XSZS'  # 支持：'XSZS'、'YP'、'KJ'等
    gongShiPath = '工时记录-2022年5月份 - To 雅楠.xlsx'  # f列标题务必为"销售合同编号"
    xiaoShouPath = '销售项目-销售合同号.xlsx'  # d列标题务必为"项目名称"

    isScreenShot = False  # 是否打开屏幕截图，支持：True、False，默认开启

    startNum = selectStartNumByXiaoShou(xiaoShouPath)
    print(f'获取项目编号成功，起始项目编号为:{startNum}')
    names = selectNamesByPathAndStartStr(gongShiPath, xiaoShouPath, nameStart)
    print(f'获取项目名称成功，项目名称集合为：{names}')

    addButtonPos = (287, 85)  # 增加按键位置，默认 (287, 85)
    numButtonPos = (466, 928)  # 项目编号位置，默认 (466, 928)
    nameButtonPos = (634, 928)  # 项目名称位置，默认 (634, 928)
    clickBlankPos = (1380, 900)  # 点击U8空白处，默认 (1380, 900)
    iterateName(startNum, names)
    print(f'项目编号项目名称已录入完成，可根据控制台打印数据与U8一一核对校验')
