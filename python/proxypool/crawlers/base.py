from retrying import retry
import requests
from loguru import logger
from proxypool.setting import GET_TIMEOUT


class BaseCrawler(object):
    urls = []
    
    @retry(stop_max_attempt_number=3, retry_on_result=lambda x: x is None, wait_fixed=2000)
    def fetch(self, url, **kwargs):
        try:
            kwargs.setdefault('timeout', GET_TIMEOUT)
            kwargs.setdefault('verify', False)
            response = requests.get(url, **kwargs)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                return response.text
        except requests.ConnectionError:
            return

    @retry(stop_max_attempt_number=3, retry_on_result=lambda x: x is None, wait_fixed=2000)
    def fetch_post(self, url,param, **kwargs):
        try:
            kwargs.setdefault('timeout', GET_TIMEOUT)
            kwargs.setdefault('verify', False)
            response = requests.post(url,data=param, **kwargs)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                return response.text
        except requests.ConnectionError:
            return


    @logger.catch
    def crawl(self):
        """
        crawl main method
        """
        if not self.urls is None:
            for url in self.urls:
                logger.info(f'fetching {url}')
                html = self.fetch(url)
                for proxy in self.parse(html):
                    logger.info(f'fetched proxy {proxy.string()} from {url}')
                    yield proxy

        if not self.post_urls is None:
            for post_url in self.post_urls:
                logger.info(f'fetching {post_url}')
                html = self.fetch_post(post_url[0], post_url[1])
                for proxy in self.parse(html):
                    logger.info(f'fetched proxy {proxy.string()} from {post_url}')
                    yield proxy