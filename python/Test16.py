# 输出指定格式的日期
import time
import datetime

# 输出今日日期，格式为 dd/mm/yyyy
print(time.strftime("%d/%m/%Y", time.localtime(time.time())))
# 创建日期对象
today = datetime.date(2018, 11, 8)
print(today.strftime("%d/%m/%Y"))
#  日期算术运算
tomorow = today + datetime.timedelta(days=1)
print(tomorow.strftime("%d/%m/%Y"))
nextYear = today.replace(year=today.year + 1)
print(nextYear)
nextmonth = today.replace(month=today.month + 1)
print(nextmonth)