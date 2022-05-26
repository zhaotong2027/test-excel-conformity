
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

# https://blog.csdn.net/u010698107/article/details/121736386
# 列出支持的语言

if __name__ == '__main__':

    print(pytesseract.get_languages(config=''))
    print(pytesseract.image_to_string(Image.open('test-ocr.jpeg'), lang='chi_sim+eng'))

