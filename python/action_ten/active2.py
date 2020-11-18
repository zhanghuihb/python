import os

def createFolder():
    # 创建文件目录
    fPath = r"E:\data\python"
    print("=" * 20,"创建文件夹开始","=" * 20,"\n")
    folderNum = int(input("请输入创建文件夹的个数："))
    for index,item in enumerate(range(folderNum)):
        os.makedirs(os.path.join(fPath,str(item + 1)))
    print("\n","=" * 20,"创建文件夹成功","=" * 20,"\n")
if __name__ == '__main__':
    try:
        createFolder()
    except Exception as e:
        print("出错了，原因是：",e)