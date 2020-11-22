# 暂停一秒输出
# 使用 time 模块的 sleep() 函数
import time

l1 = [1, 2, 3, 4]
for i in range(4):
    time.sleep(1)
    print(l1[i])
