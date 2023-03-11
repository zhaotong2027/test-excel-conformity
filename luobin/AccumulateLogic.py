x = 1
y = 1
k = 0

while (k < 6):
    print(k, x, y)
    s = x - y
    t = x + y
    x = s
    y = t
    k = k + 1

print(k, x, y)
