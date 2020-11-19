import requests
import re
import json
import time

def get_one_page(url):
    '''通过http请求抓取单个页面html'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
        'Host': 'maoyan.com',
        'Cookie': '__mta=149197705.1605773125898.1605782589305.1605782590275.34; uuid_n_v=v1; uuid=02FBD6D02A3E11EB97145540D12763BA6C013251484E48AB8823E321AB33C35C; _csrf=381e571f4ae205fbfe1fcd708e07e1d1d7986d35745d887de56d9d41979cc70f; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1605773126; _lx_utm=utm_source=Baidu&utm_medium=organic; _lxsdk_cuid=175df8968d625-063014ffc317bd-7b10374c-1fa400-175df8968d7c8; _lxsdk=02FBD6D02A3E11EB97145540D12763BA6C013251484E48AB8823E321AB33C35C; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1605782590; _lxsdk_s=175dfe76bec-314-84e-19d||58',
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
            'score': item[6].strip() + item[7].strip()
        }
        movie_list.append(movie)
    write_movie_to_file(movie_list)

def write_movie_to_file(content):
    '''写入文件'''
    with open('E:\data\python\maoyan_movies.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, indent=2, ensure_ascii=False))
    print("写入文件成功")
if __name__ == '__main__':
    try:
        for i in range(10):
            html = get_one_page("https://maoyan.com/board/4?offset=" + str(i * 10))
            if (html != None):
                parse_one_page(html)
            else:
                print("第%d请求页面数据为空" % i)
            time.sleep(1)
    except Exception as e:
        print("出错了,原因是：", e)