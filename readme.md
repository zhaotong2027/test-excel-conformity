***0、目录结构***

工程的根目录：test-excel-conformity

打开每个文件夹先阅读 readme.md 文件

即优先阅读 test-excel-conformity/readme.md

其次阅读 test-excel-conformity/linlin/readme.md

不同一级文件夹下各程序项目没有关联，报错时可删除不用的文件夹，比如删除linlin文件夹下所有内容

***1、更新最新插件***

插件名写入requirements.txt （没写版本号默认最新）

在terminal执行：pip install -r requirements.txt 

验证：pytest --version


出现错误： expected str, bytes or os.PathLike object, not int

在terminal执行： pip install package_name --no-cache-dir

***2、确认环境配置成功***

本工程的根目录（test-excel-conformity）下的 main.py 用于测试环境是否安装成功

打开 main.py 第13行 main 方法处左边有绿色的小箭头，

点击箭头，选择 Run 'main' 即为一次运行，打印出 Hi, PyCharm 则安装成功
