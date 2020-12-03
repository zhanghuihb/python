from pyquery import PyQuery
import module.mongo_database as md
import requests
import time
import random
import module.timeUtil as timeUtil
import os


class SpiderDZDP():

    def __init__(self):
        self.entry_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
            'Host': 'www.dianping.com',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cookie': 'cy=1; cye=shanghai; _lxsdk_cuid=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _lxsdk=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _hc.v=0267b309-3904-cc87-7f6f-06a52aa7e104.1605662001; aburl=1; s_ViewType=10; fspop=test; ua=dpuser_0671354772; ctu=9094b28b3618ed0de6c888c89606527ac522f7d11957b989ed480f33132407ab; _dp.ac.v=22055be9-2aa0-46cf-9ec5-8f2d27e0824f; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1606438349,1606709351,1606789303,1606870537; dper=0e0250c1188016d13ee6653a92fc7bc940f79cecb87795dcd7e66b81249c236759781259652310f6c3a9674e5042e4a53256952c4c3600c460378a07ddb3fdec540be11571a327157fe0c976fbdfb5225b4df4b6b98a1db0402ec511ddf7ba41; ll=7fd06e815b796be3df069dec7836c3df; uamo=13917041591; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; dplet=f5c34d3a013e04ec29378b3ec6f1d9a4; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1606888618; _lxsdk_s=17621ffa74d-dd5-391-bc1%7C%7C64'
        }

    def index_page(self, page):
        """
        抓取页面
        :param page:
        :return:
        """
        print('正在爬取第 %s 页' % page)
        try:
            entry_link = "http://www.dianping.com/shanghai/ch10/p" + str(page)
            # 获取字体
            response = requests.get(entry_link, headers=self.entry_headers)
            if response.status_code == 200:
                doc = PyQuery(response.text)
                items = doc("#shop-all-list ul li").items()
                for item in items:
                    # 当前店铺ID
                    self.current_shopId = item.find(".txt .tit a").attr("data-shopid")

                    # 保存店铺网页
                    self.download_html(self.current_shopId, response.text)

                    # 保存当前店铺信息
                    shopInfo = {
                        "shopId": self.current_shopId,
                        "shopName": item.find(".txt .tit a").attr("title"),
                        "starWrapper": item.find(".comment .nebula_star").text(),
                        "url": item.find(".pic a img").attr("data-src")
                    }
                    md.save_to_mongo(shopInfo, "dzdp-shop")
            else:
                record = {
                    "type": 4,  # 失败类型 type: 1-保存商品信息失败 2-访问评论页面失败
                    "url": entry_link,
                    "status": 0,  # 重试状态 status: 0-未重试 1-重试成功 n-具体重试失败次数，比如2，代表重试失败1次，3代表重试失败2次
                    "createTime": timeUtil.fotmatCurrentTimeWithFormat("%Y-%m-%d %H:%M:%S"),
                    "retryTime": timeUtil.fotmatCurrentTimeWithFormat("%Y-%m-%d %H:%M:%S")
                }
                md.save_fail_record(record)
        except Exception as e:
            print("超时了", e)
            record = {
                "type": 4,  # 失败类型 type: 1-保存商品信息失败 2-访问评论页面失败 3-店铺详情页面失败 4-店铺列表页面失败
                "url": entry_link,
                "status": 0,  # 重试状态 status: 0-未重试 1-重试成功 n-具体重试失败次数，比如2，代表重试失败1次，3代表重试失败2次
                "createTime": timeUtil.fotmatCurrentTimeWithFormat("%Y-%m-%d %H:%M:%S"),
                "retryTime": timeUtil.fotmatCurrentTimeWithFormat("%Y-%m-%d %H:%M:%S")
            }
            md.save_fail_record(record)

    def download_html(self, shopId, html_text):
        path = 'F:\data\python\dzdp\shopList\%s' % shopId
        if not os.path.exists(path):
            os.makedirs(path)

        with open('%s\%s-网页数据.html' % (path, self.current_shopId), 'w', encoding='utf-8') as f:
            f.write(html_text)

if __name__ == '__main__':
    spider = SpiderDZDP()
    try:
        for page in range(10,51):
            spider.index_page(page)
            time.sleep(5 + int(random.random() * 10))
    except Exception as e:
        print("出错了", e)
