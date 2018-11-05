# 将一个列表的数据复制到另一个列表中

def copy(l1):
    return l1[:]

l1 = [1, 3, 5]
l2 = list(copy(l1))
print(l2.sort())