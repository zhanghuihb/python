import time;
# 判断现在是这一年的第几天？

print(time.localtime(time.time()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
print("it is the ", time.strftime("%j", time.localtime(time.time())), " day")