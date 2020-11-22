# 斐波那契数列
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
'''
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n== 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

while True:
    l = []
    n = int(input("请输入一个数字:"))
    for i in range(n):
        l.append(fib(i))
    print("斐波那契数列前", n, "项:",l)