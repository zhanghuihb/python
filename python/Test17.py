# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

while True:
    str = input("请输入一行文字：")
    letters = 0
    space = 0
    digital = 0
    others = 0
    i = 0;
    while i < len(str):
        c = str[i]

        if c.isalpha(): # 英文字母
            letters += 1
        elif c.isspace(): # 空格
            space += 1
        elif c.isdigit(): # 数字
            digital += 1
        else: # 其他字符
            others += 1
        i += 1
    print("英文字母 %d 个，空格 %d 个，数字 %d 个，其他字符 %d 个" % (letters, space, digital, others))