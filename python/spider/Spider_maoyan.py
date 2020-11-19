import requests
import re
import json

def get_one_page(url):
    '''通过http请求抓取单个页面html'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
        'Host': 'maoyan.com',

    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        return response.text
    return None
def parse_one_page(html):
    '''解析抓取到的页面'''
    movie_list = []
    regex_ = '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?movieId:(.*?)}">(.*?)</a>.*?star">(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'
    pattern = re.compile(regex_, re.S)
    items = re.findall(pattern, html)
    for item in items:
        movie={
            'index': item[0],
            'image': item[1],
            'movieId': item[2].strip(),
            'title': item[3],
            'actor': item[4].strip()[3:] if len(item[4].strip()) > 3 else '',
            'time': item[5].strip()[5:] if len(item[5].strip()) > 5 else '',
            'score': item[6].strip() + item[6].strip()
        }
        movie_list.append(movie)
    write_movie_to_file(movie_list)

def write_movie_to_file(content):
    '''写入文件'''
    with open('E:\data\python\maoyan_movies.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(content, indent=2, ensure_ascii=False))
    print("写入文件成功")
if __name__ == '__main__':
    try:
        html = get_one_page("https://maoyan.com/board/4")
        if(html != None):
            parse_one_page(html)
        print("请求页面数据为空")
    except Exception as e:
        print("出错了,原因是：", e)