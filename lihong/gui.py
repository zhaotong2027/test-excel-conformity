# 1、点击"增加按钮"（增加按钮的像素-,-）
# 2、在像素（-,-）位置添加"项目编号"
# 3、在像素（-,-）位置添加"项目名称"
# 4、点击空白处

# 5、遍历项目名称（待讨论）

import pyautogui


def autoGuiOnce(num, name):
    # print(f'屏幕尺寸：{pyautogui.size()}')
    # print(f'当前鼠标位置： {pyautogui.position()}')

    # 1、点击"增加按钮"（增加按钮的像素-,-）
    addButtonPos = (144, 181)
    pyautogui.moveTo(addButtonPos)
    pyautogui.leftClick(addButtonPos)
    pyautogui.doubleClick(addButtonPos)

    # 2、在像素（-,-）位置添加"项目编号"
    numButtonPos = (491, 453)
    pyautogui.moveTo(numButtonPos)
    pyautogui.leftClick(numButtonPos)
    pyautogui.typewrite(num)
    pyautogui.hotkey('enter')

    # 3、在像素（-,-）位置添加"项目名称"
    nameButtonPos = (491, 453)
    pyautogui.leftClick(nameButtonPos)
    pyautogui.typewrite(name)
    pyautogui.hotkey('enter')

    # 4、点击空白处
    im = pyautogui.screenshot(region=(0, 0, 1480, 1000))
    im.save(fr'screenshot/{num}-{name}.png')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('delete')
    pyautogui.leftClick((1380, 885))


def iterateName(startNum, names):
    if (len(names) != 0):
        for name in names:
            autoGuiOnce(str(startNum), name)
            startNum += 1


if __name__ == '__main__':
    # pyautogui.PAUSE = 1
    startNum = 4289  # 起始编号
    names = ["Porsche", "Volvo", "uuu"]
    iterateName(startNum, names)
