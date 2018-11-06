# 判断101-200之间有多少个素数，并输出所有素数
# 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数
l = []
for num in range(101, 201):
    sign = 0
    for i in range(2, num):
        if num % i == 0:
            sign = 1
            break;
    if sign == 0:
        l.append(num)

print(l)