print("\n","="*30,"蚂蚁庄园动态","="*30)
# file = open("message.txt","w")
# 写入一条语句
# file.write("练习python操作文件!")
# with open("message.txt","r+") as file:
#     print(file.read())
# for i in range(50):
#     file.write("这是第" + str(i) + "行，内容为：蚂蚁庄园的第" + str(i) + "条动态\n" )
# print("\n即将显示......\n")
# file.close()
# with open("message.txt", "r") as file:
#     # 循环，直到最后一行
#     while True:
#         message = file.readline();
#         if message == '':
#             break;
#         print(message)
'''读取全部行'''
with open("message.txt","r") as file:
    message = file.readlines()
    for m in message:
        print(m)
print("\n", "=" * 30, "over", "=" * 30)
