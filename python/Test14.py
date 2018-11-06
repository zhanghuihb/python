# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5

# 1.先求出小于该整数的所有质数，并按照升序排序
# 2.如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# 3.如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# 4.如果n不能被k整除，则用下一个质数作为k的值,重复执行第一步。

# 1.先求出小于该整数的所有质数，并按照升序排序
def calPrimes(n):
    l = []
    for i in range(2, n + 1):
        sign = True
        for j in range(2, i):
            if i % j == 0:
                sign = False
                break;
        if sign:
            l.append(i)
    return l
# 递归
# 2.如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# 3.如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# 4.如果n不能被k整除，则用下一个质数作为k的值,重复执行第一步。
def calAllPrimes(prime, i, num, ll):
    k = prime[i]
    if k == num:
        ll.append(k)
        return ll
    elif k < num:
        if num % k == 0:
            ll.append(k)
            return calAllPrimes(prime, i, num / k, ll)
        else:
            i += 1
            return calAllPrimes(prime, i, num, ll)

while True:
    print()
    num = int(input("请输入一个整数："))
    '''小于整数num的所有质数（素数）'''
    prime = calPrimes(num)
    '''该整数的所有质因数'''
    ll = []
    calAllPrimes(prime, 0, num, ll)
    print("%d = " %(num), end="")
    for i in ll:
        print("{} * ".format(i), end="")