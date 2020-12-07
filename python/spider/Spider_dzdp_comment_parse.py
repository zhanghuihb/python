import re
import parsel
from pyquery import PyQuery
import os
import module.mongo_database as md

class CommentParse():
    def get_suffix_file(self, path, suffix):
        """
        获取给定后缀的文件名
        :param path:
        :param suffix:
        :return:
        """
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(suffix):
                    return file

    def get_encrypt_prefix(self, filename):
        """
        从文件名称获取字体加密前缀
        :param filename:
        :return:
        """
        return filename.split(".")[0].split("-")[2]

    def parse(shopId, page):
        try:
            Parse = CommentParse()
            path_prefix = 'F:\data\python\dzdp\comment\%s\%s' % (shopId, page)
            # svg文件路径
            filename_svg = Parse.get_suffix_file(path_prefix, '.svg')
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
                    lines.append([int(
                        path_id_y_dict[re.findall('.*?xlink:href="#(\d+)".*?', text_path.css('textPath').get())[0]]),
                                  text_path.css('textPath::text').get()])
            """获取所有的类名与位置"""
            # css文件路径
            filename_css = Parse.get_suffix_file(path_prefix, '.css')
            # svg 字体加密前缀
            encrypt_prefix = Parse.get_encrypt_prefix(filename_svg)
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
            filename_html = Parse.get_suffix_file(path_prefix, '.html')
            with open('%s\%s' % (path_prefix, filename_html), 'r', encoding='utf-8') as f:
                html_text = f.read()
            for item in class_map:
                html_text = html_text.replace('<svgmtsi class="'+item[0]+'"></svgmtsi>', item[3])
            doc = PyQuery(html_text)
            items = doc(".reviews-items ul li").items()
            for item in items:
                # 取显示的内容
                comment = item.find(".main-review .review-truncated-words").text()
                # 如果显示内容太长，隐藏掉了，直接取隐藏的内容
                if comment.endswith('展开评价'):
                    comment = item.find(".main-review .review-words").text()
                if len(comment) > 0:
                    # 喜欢的菜
                    recommendGoods = []
                    recommends = item.find(".review-recommend a").items()
                    for recommend in recommends:
                        recommendGoods.append(recommend.text())
                    # 评论图片
                    reviewPictures = []
                    pictures = item.find(".review-pictures ul li").items()
                    for picture in pictures:
                        reviewPictures.append(picture.find("a img").attr("data-big"))
                    # 保存到数据库
                    comment_info = {
                        "shop_id": shopId,
                        "avg_price": item.find(".review-rank .score .item").text(),
                        "comment": comment,
                        "comment_time": item.find(".misc-info .time").text(),
                        "user_id": item.find(".dper-photo-aside").attr("data-user-id"),
                        "user_level": 0,
                        "user_name": item.find(".main-review .dper-info .name").text(),
                        "user_url": item.find(".dper-photo-aside img").attr("data-lazyload"),
                        "praise": item.find(".actions .praise").attr("data-click-name"),
                        "reply": item.find(".actions .reply").attr("data-click-name"),
                        "favor": item.find(".actions .favor").attr("data-click-name"),
                        "report": item.find(".actions .report").attr("data-click-name"),
                        "recommend_goods": recommendGoods,
                        "review_pictures": reviewPictures
                    }
                    # print(comment_info)
                    md.save_to_mongo(comment_info,"dzdp-comment")
            return True
        except Exception as e:
            print(e)
            return False