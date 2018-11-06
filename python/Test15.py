# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
while True:
    score = int(input("请输入学生学习成绩:"))
    subject = "";
    if score >= 90:
        subject = "A"
    elif score >= 60:
        subject = "B"
    else:
        subject = "C"
    print("%d 属于 %s" %(score, subject))