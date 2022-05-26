from aip import AipOcr

# http://ai.baidu.com/ai-doc/OCR/wkibizyjk#安装ocr-python-sdk
# 通用文字识别（标准版）

""" 读取文件 """


def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()


if __name__ == '__main__':
    APP_ID = '26324468'
    API_KEY = 'llLZKZf6USNIcbAKRZLPL6Lr'
    SECRET_KEY = 'aEdNlnPKaqlvhzFBVgkPUZex2rVneW2Y'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    path = 'test-ocr.jpeg'
    image = get_file_content(path)

    # 调用通用文字识别（标准版）
    res_image = client.basicGeneral(image)
    for i in res_image.get('words_result'):  # 生成的msg实际是一个字典加列表的混合体，此处我们只需要用到字符串
        with open(f'{path}-baidu.txt', 'a') as f:
            f.write(i.get('words'))
            f.write('\r\n')

    print(f'图片{path}转换完成')
