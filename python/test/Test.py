import parsel
import re
from pyquery import PyQuery

from spider.Spider_dzdp_comment_parse import CommentParse

shopId = 'FY3TPVv4RiiC35ir'
# shopId = 'F4nE08K09Ptc47y4'
page = 10
path_prefix = 'F:\data\python\dzdp\comment\%s\%s' % (shopId, page)
# svg文件路径
filename_svg = CommentParse().get_suffix_file(path_prefix, '.svg')
"""获取svg字体"""
with open('%s\%s' % (path_prefix, filename_svg), 'r', encoding='utf-8') as f:
    svg_text = f.read()
sel = parsel.Selector(svg_text)
# 先判断是那种加密方式
defs = sel.css('defs')
lines = []
if defs is None or len(defs) == 0:
    texts = sel.css('text')
    for text in texts:
        lines.append([int(text.css('text::attr(y)').get()), text.css('text::text').get()])
else:
    paths = sel.css('path')
    # 获取path_id和y轴映射字典
    path_id_y_dict = {}
    for path in paths:
        path_id_y_dict[path.css('path::attr(id)').get()] = path.css('path::attr(d)').get().split(' ')[1]
    # 获取所有textPath
    text_paths = sel.css('textPath')
    for text_path in text_paths:
        lines.append([int(path_id_y_dict[re.findall('.*?xlink:href="#(\d+)".*?', text_path.css('textPath').get())[0]]), text_path.css('textPath::text').get()])
"""获取所有的类名与位置"""
# css文件路径
filename_css = CommentParse().get_suffix_file(path_prefix, '.css')
# svg 字体加密前缀
encrypt_prefix = CommentParse().get_encrypt_prefix(filename_svg)
with open('%s\%s' % (path_prefix, filename_css), 'r', encoding='utf-8') as f:
    css_text = f.read()
class_map = re.findall('(%s\w+){background:-(\d+).0px -(\d+).0px;}' % encrypt_prefix, css_text)
class_map = [[cls_name, int(x), int(y)] for cls_name, x, y in class_map]

"""找到加密字体对应的字体"""
for item in class_map:
    for line in lines:
        if item[2] < line[0]:
            item.append(line[1][int(item[1] / 14)])
            break;
"""替换html中加密字体"""
# html文件路径
filename_html = CommentParse().get_suffix_file(path_prefix, '.html')
with open('%s\%s' % (path_prefix, filename_html), 'r', encoding='utf-8') as f:
    html_text = f.read()
for item in class_map:
    html_text = html_text.replace('<svgmtsi class="'+item[0]+'"></svgmtsi>', item[3])
doc = PyQuery(html_text)
items = doc(".reviews-items ul li").items()
for item in items:
    print(item)
print('成功')
