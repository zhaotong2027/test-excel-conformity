
***1.确保图片文件夹的位置和名称正确***

图片文件夹位置：test-excel-conformity/zizhen 文件夹下（生成的txt也在这个文件夹下）

txt文件名称：'zizhen/{img_path}-baidu/tesseract.txt'


***2.使用前的准备工作***

共提供了两种方式解析图片，一种用百度的三方库，一种用谷歌的三方库。

使用百度的库，开发者需要申请百度AI的应用账号，使用者不用。

使用谷歌的三方库，开发和使用者都需要本地下载并安装tesseract。

***3.文件及作用***

主要文件为 .py 结尾的python文件，每个文件的 main 方法处左边有绿色的小箭头，
点击箭头，选择 Run 'main' 即为一次运行

ExcelRead.py 用于读取文件并整合目标参数，运行一次，打印出相关模块则运行成功

ExcelWrite.py 用于生成汇总的银行余额表excel文件，运行一次，生成 银行余额表{date}.xlsx 则运行成功