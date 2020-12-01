import requests
import re
import os
import parsel
from pyquery import PyQuery
"""获取svg字体"""
with open('F:\data\python\dzdp\G7lZQSVUguP43EIT\G7lZQSVUguP43EIT-SVG数据.svg', 'r', encoding='utf-8') as f:
    svg_text = f.read()
sel = parsel.Selector(svg_text)
texts = sel.css('text')
lines = []
for text in texts:
    lines.append([int(text.css('text::attr(y)').get()), text.css('text::text').get()])
"""获取所有的类名与位置"""
with open('F:\data\python\dzdp\G7lZQSVUguP43EIT\G7lZQSVUguP43EIT-CSS数据.css', 'r', encoding='utf-8') as f:
    css_text = f.read()
class_map = re.findall('(wu\w+){background:-(\d+).0px -(\d+).0px;}', css_text)
class_map = [[cls_name, int(x), int(y)] for cls_name, x, y in class_map]

"""找到加密字体对应的字体"""
for item in class_map:
    for line in lines:
        if item[2] < line[0]:
            item.append(line[1][int(item[1] / 14)])
            break;
"""替换html中加密字体"""
with open('F:\data\python\dzdp\G7lZQSVUguP43EIT\G7lZQSVUguP43EIT-网页数据.html', 'r', encoding='utf-8') as f:
    html_text = f.read()
doc = PyQuery(html_text)
items = doc(".reviews-items ul li").items()
for item in items:
    print(item.find(".main-review .review-truncated-words").text())