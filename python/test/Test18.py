# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
from functools import reduce

num = int(input("请输入一个数字："))
n = int(input("请输入相加的项的个数："))
items = []
total = 0
print("s =", end="")
for i in range(1, n + 1):
    temp = ''
    for j in range(i):
        temp = temp + str(num)
    if i == n:
        print(" %s " % (temp), end="")
    else:
        print(" %s +" % (temp), end="")
    total += int(temp)
    items.append(int(temp))
print("= %s" % (total))

sum = reduce(lambda x, y: x + y, items)
print(sum)


