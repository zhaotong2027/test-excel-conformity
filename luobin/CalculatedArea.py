s = input("请输入带符号的半径值:")
print(s[-2:])
if s[-2:] == "cm":
    a = 3.14 * (eval(s[-3:-2])) * (eval(s[-3:-2])) * 100
if s[-2:] == "mm":
    a = 3.14 * (eval(s[-3:-2])) * (eval(s[-3:-2]))
print(str(a) + "平方毫米")

