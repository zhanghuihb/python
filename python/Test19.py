# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

# 1.先求出所有能被整除的数，本身排除
def calPrimes(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    return l

for i in range(2, 1000 + 1):
    ll = prime = calPrimes(i)
    total = 0
    for j in ll:
        total = total + j
    if i == total:
        print(i)
        print(ll)