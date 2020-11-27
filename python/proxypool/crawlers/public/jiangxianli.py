from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler


BASE_URL = 'https://ip.jiangxianli.com/?page={}&country=中国'
MAX_PAGE = 4


class JiangXianLiCrawler(BaseCrawler):
    """
    JiangXianLi crawler, https://ip.jiangxianli.com/
    """
    urls = [BASE_URL.format(page) for page in range(1, MAX_PAGE + 1)]
    
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('.layui-table tbody tr').items()
        for tr in trs:
            host = tr.find('td:nth-child(1)').text()
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = JiangXianLiCrawler()
    for proxy in crawler.crawl():
        print(proxy)
