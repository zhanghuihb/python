import re
html = '口味aaa bbb'

list = re.findall('口味(.*?) ', html)
print(list)