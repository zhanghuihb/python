import requests
import re
import os
from module import timeUtil
import module.mongo_database as md

headers = {
    'Cookie': 'cy=1; cye=shanghai; _lxsdk_cuid=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _lxsdk=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _hc.v=0267b309-3904-cc87-7f6f-06a52aa7e104.1605662001; aburl=1; s_ViewType=10; ctu=9094b28b3618ed0de6c888c89606527ac522f7d11957b989ed480f33132407ab; _dp.ac.v=22055be9-2aa0-46cf-9ec5-8f2d27e0824f; fspop=test; ua=dpuser_7445491144; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1606709351,1606789303,1606870537,1607043371; dper=8bb62f838991f97ed3b646e608021773f274389a4c56b05eb02b81a83279d45ca773790ac9516419fafa9847c05c2455ded6138f143b42afb4d6857943d459de64568be2029160909b5c83b3f6299945109db52b572fe0fdf49c8a825af320ee; ll=7fd06e815b796be3df069dec7836c3df; uamo=17321437793; dplet=4a57d5b07af13fc99d8c3b20d5b45db5; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1607049623; _lxsdk_s=1762b9f0281-53e-09f-821%7C%7C252',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
    'Host': 'www.dianping.com',
    'Referer': 'http://www.dianping.com/shop/G7lZQSVUguP43EIT'
}
class CommentDownload():
    page = 1
    shop_id = ""
    path_prefix = ""
    comment_url = ""
    def create_dirs(self,shopId, page):
        """
        1.创建目录
        """
        path = 'F:\data\python\dzdp\comment\%s\%s' % (shopId, page)
        if not os.path.exists(path):
            os.makedirs(path)
        self.page = page
        self.shop_id = shopId
        self.path_prefix = path
        self.comment_url = 'http://www.dianping.com/shop/%s/review_all/p%s' % (self.shop_id, self.page)
    def get_html(self):
        """
        2.获取html网页内容
        """
        response = requests.get(self.comment_url, headers=headers)
        with open('%s\%s-网页数据.html' % (self.path_prefix, self.shop_id), 'w', encoding='utf-8') as f:
            f.write(response.text)
        return response
    def get_css(self,html_text):
        """
        3.获取css文件
        """
        # 拿到含有字体的css_url
        pattern_css = re.compile('<head>.*href="(//s3plus.*?.css)">.*?</head>', re.S)
        css_url = re.findall(pattern_css, html_text)
        css_response = requests.get('http:' + css_url[0])
        with open('%s\%s-CSS数据.css' % (self.path_prefix, self.shop_id), 'w', encoding='utf-8') as f:
            f.write(css_response.text)
        return css_response
    def get_svg(self,css_text):
        """
        4.获取svg内容
        """
        # 获取svgmtsi标签class前两位

        pattern_svg = re.compile(r'svgmtsi\[class\^="(.*?)"\].*?background-image: url\((.*?)\)', re.S)
        svg_url = re.findall(pattern_svg, css_text)
        svg_response = requests.get('http:' + svg_url[0][1])
        with open('%s\%s-SVG数据-%s.svg' % (self.path_prefix, self.shop_id, svg_url[0][0]), 'w', encoding='utf-8') as f:
            f.write(svg_response.text)
        return svg_response
    def download(shopId, page):
        """
        下载页面相关信息
        :param shopId:
        :param page:
        :return:
        """
        try:
            # 1.创建目录
            download = CommentDownload()
            download.create_dirs(shopId, page)
            # 2.获取html网页内容
            html_response = download.get_html()
            # 3.获取css文件
            css_response = download.get_css(html_response.text)
            # 4.获取svg内容
            download.get_svg(css_response.text)

            return True
        except Exception as e:
            print("下载发生异常:", e)
            record = {
                "type": 2,  # 失败类型 type: 1-保存商品信息失败 2-访问评论页面失败
                "url": download.comment_url ,
                "status": 0,  # 重试状态 status: 0-未重试 1-重试成功 n-具体重试失败次数，比如2，代表重试失败1次，3代表重试失败2次
                "createTime": timeUtil.fotmatCurrentTimeWithFormat("%Y-%m-%d %H:%M:%S"),
                "retryTime": timeUtil.fotmatCurrentTimeWithFormat("%Y-%m-%d %H:%M:%S")
            }
            md.save_fail_record(record)
            return False