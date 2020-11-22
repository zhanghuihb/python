# 暂停一秒输出，并格式化当前时间
import time

print("暂停开始")
time.sleep(1)
print("暂停结束")

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))