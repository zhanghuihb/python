# 输入三个整数x,y,z，请把这三个数由小到大输出。
l = []
for i in range(3):
    x = int(input("请输入一个整数:"))
    l.append(x)
print(l)
l.sort()
print(l)
