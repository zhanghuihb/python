import requests
import re
import os

headers = {
    'Cookie': 'cy=1; cye=shanghai; _lxsdk_cuid=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _lxsdk=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _hc.v=0267b309-3904-cc87-7f6f-06a52aa7e104.1605662001; aburl=1; s_ViewType=10; fspop=test; ua=dpuser_0671354772; ctu=9094b28b3618ed0de6c888c89606527ac522f7d11957b989ed480f33132407ab; _dp.ac.v=22055be9-2aa0-46cf-9ec5-8f2d27e0824f; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1606353741,1606438349,1606709351,1606789303; dper=0e0250c1188016d13ee6653a92fc7bc98d679267183d8a11e3775b945e403925981c8116d199bbcc56982dc5d5456463d42c4d543573fab173a0796cdc481687b38da55a5cd987c5ba75a0c63b12031a16d17649ed30cd9a155ce84f91090676; ll=7fd06e815b796be3df069dec7836c3df; uamo=13917041591; dplet=43c814fc53cd11ba8ee9b8d65821392b; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1606789435; _lxsdk_s=1761c6e806d-bc6-b9e-f42%7C%7C1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
    'Host': 'www.dianping.com',
    'Referer': 'http://www.dianping.com/shop/G7lZQSVUguP43EIT'
}

"""
1.创建目录
"""
path = 'F:\data\python\dzdp\G7lZQSVUguP43EIT'
if not os.path.exists(path):
    os.makedirs()
"""
2.获取html网页内容
"""
response = requests.get('http://www.dianping.com/shop/G7lZQSVUguP43EIT/review_all', headers=headers)
with open('F:\data\python\dzdp\G7lZQSVUguP43EIT\G7lZQSVUguP43EIT-网页数据.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
"""
3.获取css文件
"""
# 拿到含有字体的css_url
pattern_css = re.compile('<head>.*href="(//s3plus.*?.css)">.*?</head>', re.S)
css_url = re.findall(pattern_css, response.text)
css_response = requests.get('http:' + css_url[0])
with open('F:\data\python\dzdp\G7lZQSVUguP43EIT\G7lZQSVUguP43EIT-CSS数据.css', 'w', encoding='utf-8') as f:
    f.write(css_response.text)
"""
4.获取svg内容
"""
pattern_svg = re.compile(r'svgmtsi\[class\^="wu"\].*?background-image: url\((.*?)\)', re.S)
svg_url = re.findall(pattern_svg, css_response.text)
svg_response = requests.get('http:' + svg_url[0])
with open('F:\data\python\dzdp\G7lZQSVUguP43EIT\G7lZQSVUguP43EIT-SVG数据.svg', 'w', encoding='utf-8') as f:
    f.write(svg_response.text)
"""
5.
"""