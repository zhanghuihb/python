# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 1-50  2-25 3-12.5 4-6.25
# 1-100 2-100 3-50 4-25   5-12.5

def calHigh(i):
    high = 100
    return high/(2**i)

while True:
    n = int(input("请输入第几次："))
    print("第%d次反弹： %s 米" % (n, calHigh(n)))
    total = 0
    for i in range(1, n + 1):
        if i == 1:
            total = 100
        else:
            total = total + calHigh(i - 1) * 2
    print("第%d次落地时，共经过： %d 米" % (n, total))