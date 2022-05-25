***1、更新最新插件***

插件名写入requirements.txt （没写版本号默认最新）

在terminal执行：pip install -r requirements.txt 

验证：pytest --version


出现错误： expected str, bytes or os.PathLike object, not int

在terminal执行： pip install package_name --no-cache-dir
