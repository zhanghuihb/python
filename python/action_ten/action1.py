import os
import time
import module.timeUtil as timeUtil

def createFile():
    # 创建文件目录
    fPath = r"E:\data\python"
    # 判断文件目录是否存在，不存在，创建
    if not os.path.exists(fPath):
        os.makedirs(fPath)
        print("文件目录不存在，创建目录")
    else:
        print("文件目录存在")
    fNum = int(input("请输入创建文件数："))
    for n in range(fNum):
        # 根据当前时间获得文件名
        fName = timeUtil.fotmatTime(time.time()) + ".txt"
        with open(os.path.join(fPath, fName),"w") as file:
            # 防止文件一样，线程沉睡1一秒
            time.sleep(1)
    print("\n生成文件成功")
if __name__ == '__main__':
    try:
        createFile();
    except Exception as e:
        print("出错了,错误原因：", e)