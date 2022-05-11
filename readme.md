***1、更新最新插件***

插件名写入requirements.txt （没写版本号默认最新）

在terminal执行：pip install -r requirements.txt 

验证：pytest --version


出现错误： expected str, bytes or os.PathLike object, not int

在terminal执行： pip install package_name --no-cache-dir



***2.确保excel文件夹的位置和名称正确***

excel文件夹位置：test-excel-conformity 文件夹下（生成的excel也在这个文件夹下）

excel文件夹名称：'银行余额自动更新测试/{name}-2022年银行日记账{date}.xlsx'



***3.文件及作用***

主要文件为 .py 结尾的python文件，每个文件的 main 方法处左边有绿色的小箭头，
点击箭头，选择 Run 'main' 即为一次运行

main 方法可编辑相关日期，excel文件名上的日期随时间变动，则 excelname_date 每次都需要编辑

main.py 用于测试环境是否安装成功，运行一次，打印出 Hi, PyCharm 则安装成功

ExcelRead.py 用于读取文件并整合目标参数，运行一次，打印出相关模块则运行成功

ExcelWrite.py 用于生成汇总的银行余额表excel文件，运行一次，生成 银行余额表{date}.xlsx 则运行成功