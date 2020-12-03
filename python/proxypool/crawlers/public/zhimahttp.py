from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
import re
import json


BASE_URL = 'http://wapi.http.cnapi.cc/index/index/get_free_ip'
MAX_PAGE = 280


class ZhiMaHttpCrawler(BaseCrawler):
    """
    ZhiMaHttp crawler, http://wapi.http.cnapi.cc/index/index/get_free_ip
    """
    post_urls = [(BASE_URL, {'page': page}) for page in range(1, MAX_PAGE + 1)]
    
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        dict = json.loads(html)
        doc = pq(dict['ret_data']['html'])
        trs = doc('.tr').items()
        for tr in trs:
            host = tr.find('td:nth-child(1)').text().replace('FREE','')
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = ZhiMaHttpCrawler()
    for proxy in crawler.crawl():
        print(proxy)
