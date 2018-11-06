# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 兔子的规律为数列1,1,2,3,5,8,13,21....
def foo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return foo(n - 1) + foo(n - 2)

while True:
    print()
    n = float(input("请输入月数："))
    for i in range(1, n + 1):
        print("%12ld" % foo(i), end="")
        if i % 6 == 0:
            print()