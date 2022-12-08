c = input("请输入带有符号的数值:")
print(c[0:-1])
if c[-1] in ['R', 'r']:
    c = (eval(c[0:-1])) * (eval(c[0:-1])) * 3.14
    print("计算后的数值是{:.2f}c", format(c))

