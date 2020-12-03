import random
import os

with open("F:\data\sort_data.txt", 'a', encoding='utf-8') as f:
    # 随机生成一个数
    for num in range(100000000):
        f.write(str(int(random.random() * 100000000)) + ",")