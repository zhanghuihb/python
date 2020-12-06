import module.mongo_database as md
from python.spider.Spider_dzdp_comment_download import CommentDownload as d
from python.spider.Spider_dzdp_comment_parse import CommentParse as p
import time
import random

def download():
    """
    下载网页文件
    :return:
    """
    # 获取待爬取店铺列表
    pageSize = 10
    for shopPage in range(1, 76):
        query = {"status": 0}
        counts = md.query_count("dzdp-shop", query)
        shop_records = md.query_by_page("dzdp-shop", query, pageNum=shopPage, pageSize=pageSize)
        if counts <= (shopPage - 1) * pageSize:
            break
        for shop in shop_records:
            # 每个店铺爬取前30页
            try:
                for page in range(1, 31):
                    result = d.download(shop["shopId"], page)
                    if result is True:
                        print('爬取店铺【%s】 第【%s】页评论成功' % (shop["shopName"], str(page)))
                    else:
                        raise Exception('爬取店铺【%s】 第【%s】页评论出错了, 停止爬取' % (shop["shopName"], str(page)))

                    # 控制访问频率，10秒到30秒之间访问一次
                    time.sleep(10 + int(random.random() * 21))
            except Exception as e:
                print(e)
                break
            else:
                # 店铺爬取成功后，修改店铺状态：status = 1 待解析
                shop_obj = md.find_one("dzdp-shop", {"shopId": shop["shopId"]})
                if shop_obj:
                    shop_obj["status"] = 1
                    md.save(shop_obj, "dzdp-shop")
                print('店铺【%s】数据下载成功' % shop["shopName"])
            # 店铺分页查询控制访问频率，10秒到30秒之间访问一次
            time.sleep(10 + int(random.random() * 21))

def parse():
    """
        解析网页文件
        :return:
        """
    # 获取待爬取店铺列表
    pageSize = 10
    query = {"status": 1}
    counts = md.query_count("dzdp-shop", query)
    for shopPage in range(1, 76):
        shop_records = md.query_by_page("dzdp-shop", query, pageNum=shopPage, pageSize=pageSize)
        if counts <= (shopPage - 1) * pageSize:
            break;
        for shop in shop_records:
            # 创建目录
            try:
                # 每个店铺爬取前30页
                for page in range(1, 31):
                    result = p.parse(shop["shopId"], page)
                    if result is True:
                        print('解析店铺【%s】 第【%s】页评论成功' % (shop["shopName"], str(page)))
                    else:
                        raise Exception('解析店铺【%s】 第【%s】页评论出错了' % (shop["shopName"], str(page)))
            except Exception as e:
                print(e)
                break;
            else:
                print('店铺【%s】数据解析完成\n' % shop["shopName"])
                # 店铺爬取成功后，修改店铺状态：status = 2 已解析
                shop_obj = md.find_one("dzdp-shop", {"shopId": shop["shopId"]})
                if shop_obj:
                    shop_obj["status"] = 2
                    md.save(shop_obj, "dzdp-shop")
if __name__ == '__main__':
    # 下载网页文件
    # download()
    # 解析网页文件
    parse()