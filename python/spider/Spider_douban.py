import requests
from lxml import etree
import time
from pyquery import PyQuery
import re

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print("发生异常", e)
    return None
def parse_html(html):
    doc = PyQuery(html)
    items = doc.find(".grid_view li").items()
    detail_urls = []
    for item in items:
        detail_urls.append(item.find(".item .info .hd a").attr("href"))
    return detail_urls

def parse_detail_html(html):
    doc = PyQuery(html)
    moive = {
        "title": doc.find("#content h1").text(),
        "poster": doc.find("#mainpic .nbgnbg img").attr("src"),
        "director": doc.find("#info > span:nth-child(1) > span.attrs").text(),
        "scriptwriter": doc.find("#info > span:nth-child(3) > span.attrs").text(),
        "protagonist": doc.find("#info > span.actor > span.attrs").text(),
        "genre": re.findall('.*?<span class="pl">类型:</span>(.*?)<br>.*?', html),
        "country": re.findall('.*<span class="pl">制片国家/地区:</span>(.*?)<br>.*', html),
        "language": re.findall('.*<span class="pl">语言:</span>(.*)<br>.*?', html),
        "releaseDate": re.findall('.*<span class="pl">上映日期:</span>(.*?)<br>.*', html),
        "mins": re.findall('.*<span class="pl">片长:</span>(.*?)<br>.*', html),
        "alis": re.findall('.*<span class="pl">又名:</span>(.*?)<br>.*', html),
        "imdb": re.findall('<a href="(.*?)".*', re.findall('.*<span class="pl">IMDb链接:</span>(.*?)<br>.*', html)[0])[0],

    }
    print(moive)
    return moive

def save_movie_mongo(movie):

    return
if __name__ == "__main__":

    # 1获取网页HTML
    url = "https://movie.douban.com/top250?start=25&filter=";
    # for page in range(0, 250, 25):
    #     html = get_html(url)
    #     time.sleep(3)
    html = get_html(url)
    # 2.获取当前页电影详情集合
    urls = parse_html(html)
    print(urls)
    for url in urls:
        # 获取详情页
        detailHtml = get_html(url)
        # 3.解析出代码
        if detailHtml is None:
            print("网页获取失败")
        moive = parse_detail_html(detailHtml)
        # 4.保存电影
        # save_movie_mongo(moive)
        time.sleep(3)