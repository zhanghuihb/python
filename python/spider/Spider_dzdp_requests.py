from pyquery import PyQuery
import re
import requests
import time
from fontTools.ttLib import TTFont
import os
import json
import module.mongo_database as md

from proxypool.storages.redis_db import RedisClient


class SpiderDZDP():

    def __init__(self):
        self.entry_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
            'Host': 'www.dianping.com',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': 'http://www.dianping.com/shop/F4nE08K09Ptc47y4',
            'Accept': 'cy=1; cityid=1; cye=shanghai; cy=1; cye=shanghai; _lxsdk_cuid=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _lxsdk=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _hc.v=0267b309-3904-cc87-7f6f-06a52aa7e104.1605662001; aburl=1; s_ViewType=10; fspop=test; ua=dpuser_0671354772; ctu=9094b28b3618ed0de6c888c89606527ac522f7d11957b989ed480f33132407ab; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1606217747,1606293404,1606353741,1606438349; _dp.ac.v=22055be9-2aa0-46cf-9ec5-8f2d27e0824f; dper=0e0250c1188016d13ee6653a92fc7bc9c75fbaec87dea78633993444ff266aeb560fd48208f0b1a5dca2ce80747c63305ba563bd8ebaa0cad181517e5745a465ecc444caf26d2f48d83cf4f29c66026d5c7919d37062560b6381af2f7794b76f; ll=7fd06e815b796be3df069dec7836c3df; uamo=13917041591; dplet=b822d6c27e3a988986ba9b0d52df8f17; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1606471872; _lxsdk_s=176091b63a7-2f7-057-9b0%7C%7C704',
        }
        self.css_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
            'Content-Type': 'text/css'
        }
        self.font_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
            'Content-Type': 'application/font-woff'
        }
        self.goods_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
            'Connection': 'keep-alive',
            'Cookie': 'cy=1; cye=shanghai; _lxsdk_cuid=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _lxsdk=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _hc.v=0267b309-3904-cc87-7f6f-06a52aa7e104.1605662001; aburl=1; s_ViewType=10; fspop=test; ua=dpuser_0671354772; ctu=9094b28b3618ed0de6c888c89606527ac522f7d11957b989ed480f33132407ab; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1606217747,1606293404,1606353741,1606438349; _dp.ac.v=22055be9-2aa0-46cf-9ec5-8f2d27e0824f; dper=0e0250c1188016d13ee6653a92fc7bc9c75fbaec87dea78633993444ff266aeb560fd48208f0b1a5dca2ce80747c63305ba563bd8ebaa0cad181517e5745a465ecc444caf26d2f48d83cf4f29c66026d5c7919d37062560b6381af2f7794b76f; ll=7fd06e815b796be3df069dec7836c3df; uamo=13917041591; dplet=f3f77a0b9a3f39eeb1878caac8757856; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1606460678; _lxsdk_s=176083f7def-8da-80c-d4b%7C%7C403'
        }

        # 字体库
        self.basefont_char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '店', '中', '美', '家', '馆', '小', '车', '大',
                              '市',
                              '公', '酒',
                              '行', '国', '品', '发', '电', '金', '心', '业', '商', '司', '超', '生', '装', '园', '场', '食', '有', '新',
                              '限',
                              '天', '面',
                              '工', '服', '海', '华', '水', '房', '饰', '城', '乐', '汽', '香', '部', '利', '子', '老', '艺', '花', '专',
                              '东',
                              '肉', '菜',
                              '学', '福', '饭', '人', '百', '餐', '茶', '务', '通', '味', '所', '山', '区', '门', '药', '银', '农', '龙',
                              '停',
                              '尚', '安',
                              '广', '鑫', '一', '容', '动', '南', '具', '源', '兴', '鲜', '记', '时', '机', '烤', '文', '康', '信', '果',
                              '阳',
                              '理', '锅',
                              '宝', '达', '地', '儿', '衣', '特', '产', '西', '批', '坊', '州', '牛', '佳', '化', '五', '米', '修', '爱',
                              '北',
                              '养', '卖',
                              '建', '材', '三', '会', '鸡', '室', '红', '站', '德', '王', '光', '名', '丽', '油', '院', '堂', '烧', '江',
                              '社',
                              '合', '星',
                              '货', '型', '村', '自', '科', '快', '便', '日', '民', '营', '和', '活', '童', '明', '器', '烟', '育', '宾',
                              '精',
                              '屋', '经',
                              '居', '庄', '石', '顺', '林', '尔', '县', '手', '厅', '销', '用', '好', '客', '火', '雅', '盛', '体', '旅',
                              '之',
                              '鞋', '辣',
                              '作', '粉', '包', '楼', '校', '鱼', '平', '彩', '上', '吧', '保', '永', '万', '物', '教', '吃', '设', '医',
                              '正',
                              '造', '丰',
                              '健', '点', '汤', '网', '庆', '技', '斯', '洗', '料', '配', '汇', '木', '缘', '加', '麻', '联', '卫', '川',
                              '泰',
                              '色', '世',
                              '方', '寓', '风', '幼', '羊', '烫', '来', '高', '厂', '兰', '阿', '贝', '皮', '全', '女', '拉', '成', '云',
                              '维',
                              '贸', '道',
                              '术', '运', '都', '口', '博', '河', '瑞', '宏', '京', '际', '路', '祥', '青', '镇', '厨', '培', '力', '惠',
                              '连',
                              '马', '鸿',
                              '钢', '训', '影', '甲', '助', '窗', '布', '富', '牌', '头', '四', '多', '妆', '吉', '苑', '沙', '恒', '隆',
                              '春',
                              '干', '饼',
                              '氏', '里', '二', '管', '诚', '制', '售', '嘉', '长', '轩', '杂', '副', '清', '计', '黄', '讯', '太', '鸭',
                              '号',
                              '街', '交',
                              '与', '叉', '附', '近', '层', '旁', '对', '巷', '栋', '环', '省', '桥', '湖', '段', '乡', '厦', '府', '铺',
                              '内',
                              '侧', '元',
                              '购', '前', '幢', '滨', '处', '向', '座', '下', '県', '凤', '港', '开', '关', '景', '泉', '塘', '放', '昌',
                              '线',
                              '湾', '政',
                              '步', '宁', '解', '白', '田', '町', '溪', '十', '八', '古', '双', '胜', '本', '单', '同', '九', '迎', '第',
                              '台',
                              '玉', '锦',
                              '底', '后', '七', '斜', '期', '武', '岭', '松', '角', '纪', '朝', '峰', '六', '振', '珠', '局', '岗', '洲',
                              '横',
                              '边', '济',
                              '井', '办', '汉', '代', '临', '弄', '团', '外', '塔', '杨', '铁', '浦', '字', '年', '岛', '陵', '原', '梅',
                              '进',
                              '荣', '友',
                              '虹', '央', '桂', '沿', '事', '津', '凯', '莲', '丁', '秀', '柳', '集', '紫', '旗', '张', '谷', '的', '是',
                              '不',
                              '了', '很',
                              '还', '个', '也', '这', '我', '就', '在', '以', '可', '到', '错', '没', '去', '过', '感', '次', '要', '比',
                              '觉',
                              '看', '得',
                              '说', '常', '真', '们', '但', '最', '喜', '哈', '么', '别', '位', '能', '较', '境', '非', '为', '欢', '然',
                              '他',
                              '挺', '着',
                              '价', '那', '意', '种', '想', '出', '员', '两', '推', '做', '排', '实', '分', '间', '甜', '度', '起', '满',
                              '给',
                              '热', '完',
                              '格', '荐', '喝', '等', '其', '再', '几', '只', '现', '朋', '候', '样', '直', '而', '买', '于', '般', '豆',
                              '量',
                              '选', '奶',
                              '打', '每', '评', '少', '算', '又', '因', '情', '找', '些', '份', '置', '适', '什', '蛋', '师', '气', '你',
                              '姐',
                              '棒', '试',
                              '总', '定', '啊', '足', '级', '整', '带', '虾', '如', '态', '且', '尝', '主', '话', '强', '当', '更', '板',
                              '知',
                              '己', '无',
                              '酸', '让', '入', '啦', '式', '笑', '赞', '片', '酱', '差', '像', '提', '队', '走', '嫩', '才', '刚', '午',
                              '接',
                              '重', '串',
                              '回', '晚', '微', '周', '值', '费', '性', '桌', '拍', '跟', '块', '调', '糕']

        # 当前爬取的店铺SHOP_ID
        self.current_shopId = 'F4nE08K09Ptc47y4'

        # 店铺名称提取正则表达式
        self.shop_name_re = '.*?<h1 class="shop-name"> (.*?)<a class="qr-contrainer".*?</h1>'
        # 星际评分正则
        self.star_wrapper_re = '.*?<div class="star-wrapper">.*?<div class="mid-score.*?">(.*?)</div>'
        # 评价提取正则
        self.review_count_re = '.*?<span id="reviewCount" class="item"> (.*?)</span>'
        # 平均消费正则
        self.avg_price_re = '.*?<span id="avgPriceTitle" class="item">人均: (.*?)</span>'
        # 口味正则
        self.taste_score_re = '.*<span class="item">口味: (.*?)</span>'
        # 技师正则
        self.technician_score_re = '.*<span class="item">技师: (.*?)</span>'
        # 环境正则
        self.environment_score_re = '.*<span class="item">环境: (.*?)</span>'
        # 服务正则
        self.service_score_re = '.*<span class="item">服务: (.*?)</span>'
        # 地址正则
        self.address_re = '.*?id="address">(.*?)</span>'
        # 电话正则
        self.mobile_re = '.*?<span class="info-name">电话：</span>(.*?)</p>'
        # 营业时间正则
        self.business_hour_re = '.*?<span class="info-name">营业时间：</span>.*?<span class="item">(.*?)</span>'

    def index_page(self, page):
        """
        抓取页面
        :param page:
        :return:
        """
        print('正在爬取第 %s 页' % page)
        try:
            entry_link = "http://www.dianping.com/shanghai/ch10/p" + str(page)
            response = requests.get(entry_link, headers=self.entry_headers)
            if (response.status_code == 200):
                doc = PyQuery(response.text)
                items = doc("#shop-all-list ul li").items()
                for item in items:
                    time.sleep(1)
                    redirect_url = item.find(".txt .tit a").attr("href")
                    # 当前店铺ID
                    self.current_shopId = item.find(".txt .tit a").attr("data-shopid")
                    # 解析当前店铺信息
                    self.parse_shop_info(redirect_url, True)
            else:
                # 请求不到，可以更换更换代理IP，重试
                print("请求不到，可以更换更换代理IP，重试")
        except Exception as e:
            print("超时了", e)
            # self.index_page(page)

    def parse_shop_info(self, redirect_url, retry_sign):
        """
        获取当前页面跳转详情页集合
        :param redirect_url 店铺页面URL
        :param retry_sign 重试标记，为True时代表需要重试，为False时代表不需要重试，失败记录直接保存数据库
        :return:
        """
        time.sleep(2)
        single_shop_response = requests.get(redirect_url, headers=self.entry_headers)
        if single_shop_response.status_code == 200:
            # 获取字体库
            if self.get_dictionary(single_shop_response.text):
                # 获取店铺信息
                if self.get_shop_info(single_shop_response.text):
                    return
        else:
            if retry_sign:
                # 请求不到，可以更换更换代理IP，重试;更换3次代理后，仍然失败，记录url，放入爬取失败列表
                print("请求不到，可以更换更换代理IP，重试")
                self.parse_shop_info(redirect_url, False)

        if not retry_sign:
            # 访问失败，保存失败记录到数据库
            record = {
                "type": 3,  # 失败类型 type: 1-保存商品信息失败 2-访问评论页面失败 3-爬取店铺信息失败
                "url": redirect_url,
                "status": 0,  # 重试状态 status: 0-未重试 1-重试成功 n-具体重试失败次数，比如2，代表重试失败1次，3代表重试失败2次
                "createTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "retryTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            }
            md.save_fail_record(record)

    def get_shop_info(self, html):
        # print(html)
        shopInfo = {
            "shopId": self.current_shopId,
            "shopName": self.fetch_info(["spider_dzdp_address"], re.findall(self.shop_name_re, html)),
            "starWrapper": self.fetch_info(["spider_dzdp_address"], re.findall(self.star_wrapper_re, html)),
            "reviewCount": self.fetch_info(["spider_dzdp_num"], re.findall(self.review_count_re, html)),
            "avgPriceTitle": self.fetch_info(["spider_dzdp_num"], re.findall(self.avg_price_re, html)),
            "tasteScore": self.fetch_info(["spider_dzdp_num"], e.findall(self.pattern(self.taste_score_re, re.S), html)),
            "technicianScore": self.fetch_info(["spider_dzdp_num"], re.findall(self.technician_score_re, html)),
            "environmentScore": self.fetch_info(["spider_dzdp_num"], re.findall(self.environment_score_re, html)),
            "serviceScore": self.fetch_info(["spider_dzdp_num"], re.findall(self.service_score_re, html)),
            "address": self.fetch_info(["spider_dzdp_address", "spider_dzdp_num"], re.findall(self.address_re, html)),
            "mobile": self.fetch_info(["spider_dzdp_num"], re.findall(self.mobile_re, html)),
            "businessHour": self.fetch_info(["spider_dzdp_shopdesc", "spider_dzdp_hours"], re.findall(self.business_hour_re, html))
        }
        print(shopInfo)
        # 保存店铺到数据库
        md.save_to_mongo(shopInfo, "dzdp-shop")

    def get_goods_info(self):
        """
        推荐菜
        :param html:
        :return:
        """
        # 直接通过get请求获取菜品列表
        goods_url = "http://www.dianping.com/ajax/json/shopDynamic/shopTabs?shopId=%s" % self.current_shopId
        goods_response = requests.get(goods_url, headers=self.goods_headers)
        if goods_response.status_code == 200:
            goods_json_str = goods_response.text
            goods_json = json.loads(goods_json_str)
            dishes = goods_json["dishesWithPicVO"]
            if not dishes is None or len(dishes) > 0:
                for dish in dishes:
                    goodsInfo = {
                        "goodsId": dish["menuId"],
                        "shopId": self.current_shopId,
                        "goodsName": self.fetch_info(["spider_dzdp_dishname"], dish["dishTagName"]),
                        "picture": dish["defaultPicURL"],
                        "finalPrice": dish["finalPrice"],
                        "shopPrice": dish["shopPrice"]
                    }

                    # 保存数据到mongo
                    md.save_to_mongo(goodsInfo, "dzdp-goods")
        else:
            print("获取推荐菜品失败")
            # 放入失败队列（字体编码也要单独存一份）
            # 保存
            record = {
                "type": 1,  # 失败类型 type: 1-保存商品信息失败
                "url": goods_url,
                "status": 0,  # 重试状态 status: 0-未重试 1-重试成功 n-具体重试失败次数，比如2，代表重试失败1次，3代表重试失败2次
                "createTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "retryTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            }
            md.save_fail_record(record)
            # 失败记录保存成功后，保存需要用到的字体库
            dictStr = RedisClient().getRedis("spider_dzdp_dishname")
            if not dictStr is None:
                RedisClient().setRedis('spider_dzdp_dishname_record["_id"]', dictStr)

    def get_comment_info(self):
        """
        爬取评论数据
        :param html:
        :return:
        """
        # 只爬取前20页评论
        for reviewPage in range(1, 2):
            review_url = "http://www.dianping.com/shop/%s/review_all/p%s" % (self.current_shopId, reviewPage)
            review_response = requests.get(review_url, self.entry_headers)
            if review_response.status_code == 200:
                html = review_response.text
                doc = PyQuery(html)
                items = doc(".review-list-main .reviews-wrapper .reviews-items ul li").items()
                for item in items:
                    time.sleep(1)
                    user_id = item.find(".dper-photo-aside").attr("data-user-id")
                    print(user_id)
            else:
                # 访问失败，更换代理重试一次，再次失败，保存失败记录到数据库
                record = {
                    "type": 2,  # 失败类型 type: 1-保存商品信息失败 2-访问评论页面失败
                    "url": review_url,
                    "status": 0,  # 重试状态 status: 0-未重试 1-重试成功 n-具体重试失败次数，比如2，代表重试失败1次，3代表重试失败2次
                    "createTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    "retryTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                }
                md.save_fail_record(record)
            time.sleep(2)

        return

    def get_dictionary(self, html):
        time.sleep(1)
        # 拿到含有字体的css_url
        pattern = re.compile('.*href="(//s3plus.*.css)"> <link.*', re.S)
        css_url = re.findall(pattern, html)
        # 拿到字体的url
        if len(css_url) == 0:
            print("没有获取到字体链接")
            return False
        time.sleep(1)
        woff_html_response = requests.get('http:' + css_url[0], headers=self.css_headers)
        if woff_html_response.status_code == 200:
            woff_url = ['http:' + url for url in re.findall(",url\(\"(.*?)\"\);}", woff_html_response.text)]
            # 拿到字体的名字
            woff_names = re.findall('font-family: "PingFangSC-Regular-(.*?)";', woff_html_response.text)
            # 将字体名字和url一一对应起来
            woff_name_url = {}
            for i in range(len(woff_names)):
                if woff_names[i] != 'reviewTag':  # 这样处理的原因是本例中用不到reviewTag这个字体文件，并且它是重复的，所以去掉它。
                    woff_name_url[woff_names[i]] = woff_url[i]
            # 字体key列表放入缓存
            for key in woff_name_url.keys():
                redisKey = "spider_dzdp_%s" % key
                # 下载字体
                response = requests.get(woff_name_url[key], headers=self.font_headers)
                with open('%s.woff' % key, 'wb') as f:
                    f.write(response.content)
                    f.close()
                # 获取字体健列表
                font = TTFont('%s.woff' % key)
                font_keys = font.getGlyphOrder()
                # uni替换成\u
                font_keys_replace = []
                for num in range(2, len(font_keys)):
                    font_keys_replace.append(font_keys[num])
                # 放入redis
                RedisClient().setRedis(redisKey, ','.join(font_keys[2:]), 60 * 60 * 24)
                # 删除字体文件
                os.remove('%s.woff' % key)
                time.sleep(1)

                return True
        else:
            print("获取字体失败 status_code=%s" % woff_html_response.status_code)

        return False

    def fetch_info(self, spider_dzdps, re_str):
        # print(re_str)
        return_str = ''
        if re_str is None or len(re_str) == 0:
            print("待替换文本不存在")
            return return_str
        return_str = re_str[0]
        # 不同字体名称有不同的标签，需要区分
        # 1.店铺名称
        need_decode_dict = {}
        woff_dict = {}
        for spider_dzdp in spider_dzdps:
            # 从缓存获取字典
            dictStr = RedisClient().getRedis(spider_dzdp)
            # 转换成列表
            if not dictStr is None:
                dictList = dictStr.split(",")
                # 放入字典
                woff_dict[spider_dzdp] = dictList

            if "spider_dzdp_address" == spider_dzdp:
                # 找出需要替换的加密字体
                pattern = re.compile('.*?<e class="address">(.*?)</e>.*?', re.S)
                need_decode_dict[spider_dzdp] = re.findall(pattern, return_str)
                # print(need_decode)
            elif "spider_dzdp_num" == spider_dzdp:
                # 找出需要替换的加密字体
                pattern = re.compile('.*?<d class="num">(.*?)</d>.*?', re.S)
                need_decode_dict[spider_dzdp] = re.findall(pattern, return_str)
            elif "spider_dzdp_shopdesc" == spider_dzdp:
                # 找出需要替换的加密字体
                pattern = re.compile('.*?<svgmtsi class="shopdesc">(.*?)</svgmtsi>.*?', re.S)
                need_decode_dict[spider_dzdp] = re.findall(pattern, return_str)
            elif "spider_dzdp_hours" == spider_dzdp:
                # 找出需要替换的加密字体
                pattern = re.compile('.*?<svgmtsi class="hours">(.*?)</svgmtsi>.*?', re.S)
                need_decode_dict[spider_dzdp] = re.findall(pattern, return_str)
            elif "spider_dzdp_dishname" == spider_dzdp:
                # 找出需要替换的加密字体
                pattern = re.compile('.*?<c class="dishname">(.*?)</c>.*?', re.S)
                need_decode_dict[spider_dzdp] = re.findall(pattern, return_str)

        # 标签需要最后统一替换，否则，如果传入多个spider_dzdp，可能使用相同的标签，提前替换的话会导致后面re.findall时筛选不出加密字体
        # 加密标签替换成空字符串
        return_str = return_str.replace('<e class="address">', '').replace('</e>', '')
        # 加密标签替换成空字符串
        return_str = return_str.replace('<d class="num">', '').replace('</d>', '')
        # 加密标签替换成空字符串
        return_str = return_str.replace('<svgmtsi class="shopdesc">', '').replace('</svgmtsi>', '')
        # 加密标签替换成空字符串
        return_str = return_str.replace('<svgmtsi class="hours">', '').replace('</svgmtsi>', '')
        # 加密标签替换成空字符串
        return_str = return_str.replace('<c class="dishname">', '').replace('</c>', '')

        # 利用字体库，替换加密字体
        for spider_dzdp_two in need_decode_dict.keys():
            # 获取需要解密的内容
            replaceBeforeList = need_decode_dict[spider_dzdp_two]
            if replaceBeforeList is None or len(replaceBeforeList) == 0:
                print("%s 没有可解密的加密字体" % spider_dzdp_two)
                continue
            for replaceBefore in replaceBeforeList:
                # 格式跟数据库格式不一致，替换成一致
                replaceAfter = replaceBefore.split(";")[0].replace("&#x", "uni")
                # 获取加密字体库的下标位置
                index_position = woff_dict[spider_dzdp_two].index(replaceAfter)
                # 替换解密字体
                return_str = return_str.replace(replaceBefore, self.basefont_char[index_position])

        return return_str

    def test(self, html):
        self.get_shop_info(html)
        # self.get_goods_info()
        # self.get_comment_info()


if __name__ == '__main__':
    testHtml = '<!DOCTYPE html> <html> <head> <title>【本一日式SPA·MASSAGE(花木路店)】电话,地址,价格,营业时间(图) - 上海休闲娱乐 - 大众点评网</title> <link rel="icon" type="image/x-icon" href="//www.dpfile.com/app/pc-common/dp_favicon.a4af753914321c8e82e402e2b4be01d7.ico"> <link rel="shortcut icon" type="image/x-icon" href="//www.dpfile.com/app/pc-common/dp_favicon.a4af753914321c8e82e402e2b4be01d7.ico" > <link rel="apple-touch-icon" href="//www.dpfile.com/s/res/app-touch-icon.89213f53ed66e1693e4b6aeedd355349.png"> <link rel="apple-touch-icon" sizes="76x76" href="//www.dpfile.com/s/res/app-touch-icon-76x76.6399ce382f3e0584a6b07599cbeb3bcb.png"> <link rel="apple-touch-icon" sizes="120x120" href="//www.dpfile.com/s/res/app-touch-icon-120x120.067844b8518f076b154dcf793a46a0a5.png"> <link rel="apple-touch-icon" sizes="152x152" href="//www.dpfile.com/s/res/app-touch-icon-152x152.ee6d0c24fc2de0f9a62b6cc9e6720393.png"> <link rel="canonical" href="http://www.dianping.com/shop/G19NvNJMMSqkNCHk"/> <link rel="alternate" media="only screen and (max-width: 640px)" href="//m.dianping.com/shop/G19NvNJMMSqkNCHk" > <meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=0, viewport-fit=cover" /> <meta charset="UTF-8"/> <meta http-equiv="X-UA-Compatible" content="IE=edge"/> <meta name="Keywords" content="本一日式SPA·MASSAGE(花木路店), 本一日式SPA·MASSAGE(花木路店)点评, 本一日式SPA·MASSAGE(花木路店)团购"/> <meta name="Description" content="为您提供本一日式SPA·MASSAGE(花木路店)的人均消费、品牌简介、店铺图片、折扣优惠、用户口碑、娱乐中心会所信息、夜生活指南、KTV茶馆酒吧电玩推荐等信息，本一日式SPA·MASSAGE(花木路店)好不好，浦东新区按摩/足疗选择本一日式SPA·MASSAGE(花木路店)怎么样？快来看看大家如何点评吧！"/> <meta name="location" content="province=上海;city=上海;"> <meta itemprop="name" content="本一日式SPA·MASSAGE"> <meta itemprop="description" content="本一日式SPA·MASSAGE"> <meta itemprop="image" content="https://p0.meituan.net/dpmerchantpic/ee2edf4e948e3bf4ccf75bd8e973a332346644.jpg%40300w_225h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"> <meta name="robots" content="noarchive"> <meta content="no-transform" http-equiv="Cache-Control"/> <meta content="no-siteapp" http-equiv="Cache-Control"/> <meta http-equiv="mobile-agent" content="format=html5; url=http://m.dianping.com/shop/G19NvNJMMSqkNCHk"> <script> document.documentElement.className = location.hash ? "J_H" : ""; var G_rtop = +new Date, _gaq = [ ["_setAccount", "UA-464026-1"], ["_addOrganic", "soso", "w"], ["_addOrganic", "sogou", "query"], ["_addOrganic", "yodao", "q"], ["_addOrganic", "bing", "q"], ["_addOrganic", "360", "q"], ["_addOrganic", "gougou", "search"], ["_setDomainName", ""] , ["_setAllowHash", false] ], dpga = function (key) { _gaq.push(["_trackPageview", key || ""]) }, pageTracker = {_trackPageview: dpga}, _hip = [ ["_setPageId", 12], ["_setCityId", ], ["_setShopType", ], ["_setPVInitData", {p_render:+(new Date)-G_rtop}] ]; </script> <link rel="stylesheet" type="text/css" href="//www.dpfile.com/app/pc-common/index.min.a77ed6b2d125089a497ce8978cecc46b.css"> <script type="text/javascript" src="//www.dpfile.com/app/pc-common/index.min.e26712257c2ebe0b1a13619dcc6f54a5.js"></script> <script type="text/javascript"> window._DP_HeaderData = { "cityId": "1", "cityChName": "上海", "cityEnName": "shanghai", "pageType": "channel", "userId": "0", "userName":"", "channelId": "30", } </script> <link rel="stylesheet" type="text/css" href="//s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/96cf1bb6e0355af9779ea02090bab8d2.css"> <link rel="stylesheet" href="//www.dpfile.com/app/app-pc-main/static/main-shop.min.639818b259a07012e6bae15460111569.css" type="text/css" /> <meta name="lx:category" content="dianping_nova"> <meta name="lx:appnm" content="dp_pc"> <meta name="lx:cid" content="dp12"> <meta name="lx:autopv" content="off"/> <link rel="dns-prefetch" href="//analytics.meituan.net"/> <link rel="dns-prefetch" href="//wreport.meituan.net"/> <link rel="dns-prefetch" href="//report.meituan.net"/> <script type="text/javascript"> !(function (win, doc, ns) { var cacheFunName = "_MeiTuanALogObject"; win[cacheFunName] = ns; if (!win[ns]) { var _LX = function () { _LX.q.push(arguments); return _LX; }; _LX.q = _LX.q || []; _LX.l = +new Date(); win[ns] = _LX; } })(window, document, "LXAnalytics"); ;(function () { var environment = { cityid: "1" }; var valLab = { cat0_id: "30", cat1_id: "141", poi_id: "G19NvNJMMSqkNCHk", shopuuid: "G19NvNJMMSqkNCHk" }; var cid = "dp12"; var _LXAnalytics = window.LXAnalytics; LXAnalytics = function LXAnalytics() { var METHOD = {PV: "pageView",MC: "moduleClick",MV: "moduleView"}; try { var checkUuid = function checkUuid(valLab) { var _valLab = valLab; var custom = _valLab&&_valLab.custom; var poi_id = _valLab && (_valLab.shopid || _valLab.shopId || _valLab.poi_id); if (poi_id) _valLab = Object.assign({}, valLab, {shopuuid: poi_id}); if (custom) _valLab.custom = checkUuid(custom); return _valLab || null; }; var args = Array.prototype.slice.call(arguments); var method = args[0]; var valLab = args[1]; var environment = args[2]; var cid = args[3]; if (method === METHOD.PV) { var _valLab = checkUuid(valLab); var _environment = environment || null; _LXAnalytics(method, _valLab, _environment, cid); } else if (method === METHOD.MC || method === METHOD.MV) { var _valBid = valLab; var _valLab2 = environment?checkUuid(environment):null; var options = cid || {}; _LXAnalytics(method, _valBid, _valLab2, options); } else { _LXAnalytics.apply(null, args); } } catch (e) { console.log("LXAnalytics hooks error", e); } }; Object.keys(_LXAnalytics).forEach(function (key) { LXAnalytics[key] = _LXAnalytics[key]; }); LXAnalytics("pageView", valLab, environment, cid); })(); </script> <script src="//analytics.meituan.net/analytics.js" type="text/javascript" charset="utf-8"></script> <script type="text/javascript">(function(){var c="www.dianping.com"===window.location.host||"w.51ping.com"===window.location.host,f="m.dianping.com"===window.location.host||"m.51ping.com"===window.location.host,a="iPhone;Android;Windows Phone;SymbianOS;iPad;iPod".split(";"),g=window.location.pathname,b=window.location.search,h=window.screen.width,e=-1!==location.href.indexOf("51ping")?"test":"prod",k="test"===e?"//w.51ping.com":"//www.dianping.com";e="test"===e?"//m.51ping.com":"//m.dianping.com";var d=!1;if(c){for(c=0;c<a.length;c++)if(d= a[c],-1!=navigator.userAgent.indexOf(d)&&640>=h){d=!0;break}else d=!1;d&&(a="source=pc_jump",b=b?b+"&"+a:b+"?"+a,a=setTimeout,location.href=e+(g+b),a(void 0,500))}f&&640<h&&(a="source=m_jump",f=setTimeout,location.href=k+(g+(b?b+"&"+a:b+"?"+a)),f(void 0,500))})();</script> <script> var rohrdata = ""; var Rohr_Opt = new Object; Rohr_Opt.Flag = 100041; Rohr_Opt.LogVal = "rohrdata"; </script> <script src="//www.dpfile.com/app/rohr/rohr.min.js"></script> <script type="text/javascript"> "use strict";!function(){var a=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"_Owl_",i=window,t={page:!0,resource:!0,js:!0};i[a]||(i[a]={isRunning:!1,isReady:!1,preTasks:[],config:t,dataSet:[],use:function(a,t){this.isReady&&i.Owl&&i.Owl[a](t),this.preTasks.push({api:a,data:[t]})},add:function(a){this.dataSet.push(a)},run:function(a){var t=this;if(!this.isRunning){this.isRunning=!0;var e=a||this.config;if(!1!==e.js){var n=i.onerror;i.onerror=function(){this.isReady||this.add({type:"jsError",data:arguments}),n&&n.apply(i,arguments)}.bind(this)}var r=i.addEventListener||i.attachEvent;!1!==e.page&&r("load",function(){if(!t.isReady){var a=i.performance&&i.performance.timing;t.add({type:"pageTime",data:[a]})}}),!1!==e.resource&&(r("error",function(a){t.isReady||t.add({type:"resError",data:[a]})},!0),r("load",function(a){t.isReady||t.add({type:"resTime",data:[a]})}))}}})}(); _Owl_.run({ page: true, js: true, resource: true }) </script> </head> <body id="top"> <div class="header-container"> <div id="top-nav" class="top-nav"> <div class="top-nav-container clearfix"> <div class="group J-city-select"> <!--城市选择--> <a target="_blank" class="city J-city"><span class="map-icon"></span><span class="J-current-city">上海</span><span class="J-city-change">[更换]</span></a> <div class="city-list J-city-list Hide"> <div class="group clearfix"> <h3 class="title">国内城市</h3> <div> <a href="//www.dianping.com/shanghai" class="city-item">上海</a> <a href="//www.dianping.com/beijing" class="city-item">北京</a> <a href="//www.dianping.com/guangzhou" class="city-item">广州</a> <a href="//www.dianping.com/shenzhen" class="city-item">深圳</a> <a href="//www.dianping.com/tianjin" class="city-item">天津</a> <a href="//www.dianping.com/hangzhou" class="city-item">杭州</a> <a href="//www.dianping.com/nanjing" class="city-item">南京</a> <a href="//www.dianping.com/suzhou" class="city-item">苏州</a> <a href="//www.dianping.com/chengdu" class="city-item">成都</a> <a href="//www.dianping.com/wuhan" class="city-item">武汉</a> <a href="//www.dianping.com/chongqing" class="city-item">重庆</a> <a href="//www.dianping.com/xian" class="city-item">西安</a> </div> </div> <div class="group clearfix"> <h3 class="title">国外城市</h3> <div> <a href="//www.dianping.com/tokyo" class="city-item">东京</a> <a href="//www.dianping.com/seoul" class="city-item">首尔</a> <a href="//www.dianping.com/bangkok" class="city-item">曼谷</a> <a href="//www.dianping.com/paris" class="city-item">巴黎</a> </div> </div> <a class="all" href="//www.dianping.com/citylist">更多城市 &gt;</a> </div> </div> <div class="group quick-menu "> <span class="login-container J-login-container"> <a rel="nofollow" class="item " href="http://account.dianping.com/login" data-click-name="login">你好，请登录</a> <a rel="nofollow" class="item login" href="https://account.dianping.com/reg" data-click-name="reg">免费注册</a> </span> <span class="seprate">|</span> <a rel="nofollow" href="https://www.dianping.com/member/myinfo" class="item J-my-center-trigger">个人中心<i class="icon i-arrow"></i></a> <span class="seprate">|</span> <a target="_blank" class="item J-shop-serve-trigger">商户服务<i class="icon i-arrow"></i></a> <span class="seprate">|</span> <a target="_blank" class="item J-help-trigger">帮助中心<i class="icon i-arrow"></i></a> </div> <div class="panel my-center J-my-center-target Hide"> </div> <div class="panel my-center J-shop-serve-target Hide"> <a rel="nofollow" target="_blank" href="https://e.dianping.com/" data-click-name="shop-center">商户中心</a> <a rel="nofollow" target="_blank" href="https://e.dianping.com/claimcpc/page/index?source=dp" data-click-name="shop-coop">商户合作</a> <a rel="nofollow" target="_blank" href="https://daili.meituan.com/?comeFrom=dpwebMenu" data-click-name="daili">招募餐饮代理</a> <a rel="nofollow" target="_blank" href="https://daili.meituan.com/dz-zhaoshang" data-click-name="apollo">招募非餐饮代理</a> <a rel="nofollow" target="_blank" href="http://b.meituan.com/canyin/PC">餐饮商户中心</a> </div> <div class="panel my-center J-help-target Hide"> <a rel="nofollow" target="_blank" href="https://rules-center.meituan.com?from=dianpingPC" data-click-name="useragreement">平台规则</a> <a rel="nofollow" target="_blank" href="http://kf.dianping.com" data-click-name="kf">联系客服</a> </div> </div> </div> <div id="logo-input" class="logo-input life-conf"> <div class="logo-input-container clearfix"> <a title="大众点评网" href="/" class="logo logo-life"></a> <div class="search-box"> <div class="search-bar "> <span class="search-container clearfix"> <i class="i-search"></i> <span> <input id="J-search-input" class="J-search-input" x-webkit-speech="" x-webkit-grammar="builtin:translate" data-s-pattern="https://www.dianping.com/search/keyword/{0}/{1}_" data-s-epattern="https://www.dianping.com/shanghai/{0}" data-s-cateid="0" data-s-cityid="1" type="text" placeholder="搜索商户名、地址、菜名、外卖等" autocomplete="off" /> </span> <span class="search-bnt-panel"> <a target="_blank" class="search-btn search-channel-bnt J-search-btn" id="J-channel-bnt" data-s-chanid="30">频道搜索</a> <a target="_blank" class="search-btn search-all-bnt J-search-btn platform-btn" id="J-all-btn" data-s-chanid="0">全站搜索</a> </span> </span> <p class="hot-search J-hot-search"> </p> </div> </div> </div> </div> <div id="cate-channel" class="cate-container channel-cate-container life-conf"> <div class="nav-header"> <div class="navbar"> <span class="cate-item all-cate J-all-cate">全部休闲娱乐分类 <i class="primary-more"></i> </span> <a target="_blank" class="cate-item other-cate " href="http://s.dianping.com/event/shanghai" data-click-title="row-nav" data-click-name="免费试">免费试</a> <i class = "hot-icon"></i> <a target="_blank" class="cate-item other-cate " href="http://s.dianping.com/shanghai/group?utm_source=dp_pc_life" data-click-title="row-nav" data-click-name="社区论坛">社区论坛</a> </div> </div> <div class="gradient"></div> <div id="cate-index" class="cate-index"> <div class="navwrap"> <div id="nav" > <div class="cate-nav J-cate-nav Hidden"> <ul class="first-cate J-primary-menu"> <li class="first-item"> <div class="primary-container"> <span class="span-container"> <a target="_blank" class="index-title">足疗洗浴</a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g141" data-category="life.zuliao" data-click-title="second" data-click-name="g141"><span>足疗按摩</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g140" data-category="life.zuliao" data-click-title="second" data-click-name="g140"><span>洗浴/汗蒸</span></a> </span> </div> <div class="sec-cate Hide" data-category="cate.life.zuliao" > <div class="groups"> <div class="group"> <div class="sec-title"> <span class="channel-title" href="">足疗洗浴</span> </div> <div class="sec-items"> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g141" data-category="life.zuliao" data-click-name="g141">足疗按摩</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g140" data-category="life.zuliao" data-click-name="g140">洗浴/汗蒸</a> </div> </div> </div> </div> </li> <li class="first-item"> <div class="primary-container"> <span class="span-container"> <a target="_blank" class="index-title">玩乐</a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch15/g135" data-category="life.wanle" data-click-title="second" data-click-name="g135"><span>KTV</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g133" data-category="life.wanle" data-click-title="second" data-click-name="g133"><span>酒吧</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g2754" data-category="life.wanle" data-click-title="second" data-click-name="g2754"><span>密室逃脱</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g20040" data-category="life.wanle" data-click-title="second" data-click-name="g20040"><span>轰趴馆</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g20041" data-category="life.wanle" data-click-title="second" data-click-name="g20041"><span>私人影院</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g137" data-category="life.wanle" data-click-title="second" data-click-name="g137"><span>游乐游艺</span></a> </span> </div> <div class="sec-cate Hide" data-category="cate.life.wanle" > <div class="groups"> <div class="group"> <div class="sec-title"> <span class="channel-title" href="">玩乐High</span> </div> <div class="sec-items"> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch15/g135" data-category="life.wanle" data-click-name="g135">KTV</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g133" data-category="life.wanle" data-click-name="g133">酒吧</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g2754" data-category="life.wanle" data-click-name="g2754">密室逃脱</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g20040" data-category="life.wanle" data-click-name="g20040">轰趴馆</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g20041" data-category="life.wanle" data-click-name="g20041">私人影院</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g137" data-category="life.wanle" data-click-name="g137">游乐游艺</a> </div> </div> </div> </div> </li> <li class="first-item"> <div class="primary-container"> <span class="span-container"> <a target="_blank" class="index-title">休闲活动</a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g134" data-category="life.xiuxianhd" data-click-title="second" data-click-name="g134"><span>茶馆</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g20042" data-category="life.xiuxianhd" data-click-title="second" data-click-name="g20042"><span>网吧网咖</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g144" data-category="life.xiuxianhd" data-click-title="second" data-click-name="g144"><span>DIY手工坊</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g20038" data-category="life.xiuxianhd" data-click-title="second" data-click-name="g20038"><span>采摘/农家乐</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g142" data-category="life.xiuxianhd" data-click-title="second" data-click-name="g142"><span>文化艺术</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g6694" data-category="life.xiuxianhd" data-click-title="second" data-click-name="g6694"><span>桌游</span></a> </span> </div> <div class="sec-cate Hide" data-category="cate.life.xiuxianhd" > <div class="groups"> <div class="group"> <div class="sec-title"> <span class="channel-title" href="">休闲活动</span> </div> <div class="sec-items"> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g134" data-category="life.xiuxianhd" data-click-name="g134">茶馆</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g20042" data-category="life.xiuxianhd" data-click-name="g20042">网吧网咖</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g144" data-category="life.xiuxianhd" data-click-name="g144">DIY手工坊</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g20038" data-category="life.xiuxianhd" data-click-name="g20038">采摘/农家乐</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g142" data-category="life.xiuxianhd" data-click-name="g142">文化艺术</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g6694" data-category="life.xiuxianhd" data-click-name="g6694">桌游</a> </div> </div> </div> </div> </li> <li class="first-item"> <div class="primary-container"> <span class="span-container"> <a target="_blank" class="index-title">其他休闲娱乐</a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g33857" data-category="life.qitaxxyl" data-click-title="second" data-click-name="g33857"><span>VR</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g34089" data-category="life.qitaxxyl" data-click-title="second" data-click-name="g34089"><span>团建拓展</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g32732" data-category="life.qitaxxyl" data-click-title="second" data-click-name="g32732"><span>棋牌室</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g156" data-category="life.qitaxxyl" data-click-title="second" data-click-name="g156"><span>桌球馆</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/shanghai/ch30/g156" data-category="life.qitaxxyl" data-click-title="second" data-click-name="g156"><span>更多</span></a> </span> </div> <div class="sec-cate Hide" data-category="cate.life.qitaxxyl" > <div class="groups"> <div class="group"> <div class="sec-title"> <span class="channel-title" href="">其他休闲娱乐</span> </div> <div class="sec-items"> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g33857" data-category="life.qitaxxyl" data-click-name="g33857">VR</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g20039" data-category="life.qitaxxyl" data-click-name="g20039">真人CS</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g32732" data-category="life.qitaxxyl" data-click-name="g32732">棋牌室</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g156" data-category="life.qitaxxyl" data-click-name="g156">桌球馆</a> <a target="_blank" class="second-item" href="http://www.dianping.com/shanghai/ch30/g156" data-category="life.qitaxxyl" data-click-name="g156">更多休闲娱乐</a> </div> </div> </div> </div> </li> </ul> </div> </div> </div> </div> </div> </div> <div id="body" class="body shop-body"> <div class="body-content clearfix"> <div class="breadcrumb"> <a href="//www.dianping.com/shanghai/ch30" itemprop="url"> 上海休闲娱乐 </a> &gt; <a href="//www.dianping.com/shanghai/ch30/g141" itemprop="url"> 按摩/足疗 </a> &gt; <a href="//www.dianping.com/shanghai/ch30/r5" itemprop="url"> 浦东新区 </a> &gt; <a href="//www.dianping.com/shanghai/ch30/r803" itemprop="url"> 世纪公园 </a> &gt; <span>本一日式SPA·MASSAGE(花木路店)</span> </div> <div class="main"> <div id="basic-info" class="basic-info default nug_shop_ab_pv-a"> <s class="cover J_cover"></s> <h1 class="shop-name"> <e class="address">&#xe591;</e><e class="address">&#xf388;</e><e class="address">&#xed7d;</e><e class="address">&#xf330;</e>SPA·MASSAGE(<e class="address">&#xe821;</e><e class="address">&#xe383;</e><e class="address">&#xeb8b;</e><e class="address">&#xee0a;</e>) <a class="qr-contrainer" href="//www.dianping.com/events/m/index.htm" data-click-name="手机买单" rel="nofollow" onclick="_hip.push(["mv", { module: "shopinfo_hoverQR", action: "click"}])"> <div class="phone-qr"> <span class="arrow"></span> 手机扫码&nbsp;优惠买单 </div> <div class="qr-code"> <div id="qrcode" class="code"> <div class="code-img"></div> </div> </div> </a> <a class="branch J-branch" data-click-name="其他分店信息">其它3家分店<i class="icon i-arrow" ></i></a> </h1> <div class="brief-info"> <span title="50" class="mid-rank-stars mid-str50"></span> <span id="reviewCount" class="item"> 1<d class="num">&#xf295;</d><d class="num">&#xf6ca;</d> 条评价 </span> <div class="star-from-desc J-star-from-desc Hide">星级来自业内综合评估<i class="icon"></i></div> <span id="avgPriceTitle" class="item">人均: <d class="num">&#xeb09;</d><d class="num">&#xe5cd;</d>1 元</span> <span id="comment_score"> <span class="item">技师: <d class="num">&#xeb09;</d>.<d class="num">&#xf789;</d> </span> <span class="item">环境: <d class="num">&#xeb09;</d>.<d class="num">&#xf440;</d> </span> <span class="item">服务: <d class="num">&#xeb09;</d>.<d class="num">&#xf440;</d> </span> </span> </div> <div class="expand-info address" itemprop="street-address"> <span class="info-name">地址：</span> <div id="J_map-show" class="map_address" > <span class="item" itemprop="street-address" id="address"> <e class="address">&#xe821;</e><e class="address">&#xe383;</e><e class="address">&#xeb8b;</e>1<d class="num">&#xe5cd;</d><d class="num">&#xf295;</d><d class="num">&#xf295;</d><e class="address">&#xe709;</e> </span> <div class="addressIcon"></div> </div> </div> <p class="expand-info tel"> <span class="info-name">电话：</span> <d class="num">&#xf098;</d><d class="num">&#xf440;</d>1-<d class="num">&#xf295;</d><d class="num">&#xec53;</d><d class="num">&#xf789;</d><d class="num">&#xf098;</d><d class="num">&#xf295;</d>1** &nbsp; 1<d class="num">&#xf789;</d>1<d class="num">&#xf31f;</d><d class="num">&#xf440;</d><d class="num">&#xf295;</d><d class="num">&#xf295;</d><d class="num">&#xe5cd;</d><d class="num">&#xf295;</d>** </p> <div class="promosearch-wrapper"></div> <a class="J-unfold unfold" data-click-name="更多信息">更多信息<i class="icon"></i></a> <div class="other J-other Hide"> <p class="info info-indent"> <span class="info-name">营业时间：</span> <span class="item"> <svgmtsi class="shopdesc">&#xf531;</svgmtsi><svgmtsi class="shopdesc">&#xf388;</svgmtsi>至<svgmtsi class="shopdesc">&#xf531;</svgmtsi><svgmtsi class="shopdesc">&#xed7d;</svgmtsi> 1<svgmtsi class="hours">&#xf8a9;</svgmtsi>:<svgmtsi class="hours">&#xe3c8;</svgmtsi><svgmtsi class="hours">&#xe3c8;</svgmtsi>-<svgmtsi class="hours">&#xf8a9;</svgmtsi><svgmtsi class="hours">&#xf15a;</svgmtsi>:<svgmtsi class="hours">&#xe3c8;</svgmtsi><svgmtsi class="hours">&#xe3c8;</svgmtsi> </span> <a class="item-gray" href="//www.dianping.com/shop/G19NvNJMMSqkNCHk/edit" target="_blank" rel="nofollow" data-click-name="修改/添加营业时间"> 修改 </a> </p> <div id="license-wrappper"></div> <p class="info J-feature Hide"></p> <p id="park" class="info info-indent J-park Hide"></p> <div id="tips-wrapper"></div> </div> <div class="action"> <a class="write left-action" href="//www.dianping.com/shop/G19NvNJMMSqkNCHk/review" target="_blank" rel="nofollow" data-click-name="写评价"> <i class="icon"></i><span id="dpReviewBtn" >写评价</span></a> <div id="booking-wrapper" data-click-name="订座"></div> <span class="right-action"> <a class="share J-weixin" rel="nofollow" title="微信分享" data-click-name="微信分享"><i class="icon"></i></a> <a id="fav" class="favorite J-favorite" rel="nofollow" title="收藏" data-click-name="收藏"><i class="icon"></i></a> <a class="report" title="报错" href="/shop/G19NvNJMMSqkNCHk/edit" rel="nofollow" target="_blank" data-click-name="报错"><i class="icon"></i></a> <a class="action-more J-action-more" ><i class="icon"></i></a> <div class="shop-action-more-list J-action-more-list Hide"> <a href="/upload/shop/G19NvNJMMSqkNCHk" rel="nofollow" target="_blank" data-click-name="添加图片">添加图片</a> <i class="arrow"></i> </div> </span> </div> <div id="tuiguangAd-wrapper"> </div> </div> <div id="shop-branchs" class="shop-branchs Hide" rel="nofollow"> <div class="item"> <h3 class="name"> <a href="//www.dianping.com/shop/G7BzjydFNY0y0Toa" data-click-name="查看商户分店"> 黄浦店 </a> </h3> <p class="address"> <span class="sml-rank-stars sml-str50"></span> 斜土东路36号 </p> </div> <div class="item"> <h3 class="name"> <a href="//www.dianping.com/shop/H2CJRrbS64KBXrbn" data-click-name="查看商户分店"> 长寿路店 </a> </h3> <p class="address"> <span class="sml-rank-stars sml-str50"></span> 长寿路700号古井假日酒店3楼 </p> </div> <div class="item"> <h3 class="name"> <a href="//www.dianping.com/shop/E3AjmHEhu1MGZecy" data-click-name="查看商户分店"> 静安店 </a> </h3> <p class="address"> <span class="sml-rank-stars sml-str50"></span> 延安中路1007号二楼 </p> </div> <a class="add-shop" rel="nofollow"><i class="icon"></i></a> <a class="more-shop" target="_blank" href="//www.dianping.com/brands/bG19NvNJMMSqkNCHk" data-click-name="查看全部分店">查看全部3家分店</a> </div> <div id="shop-score" class="shop-score Hide"> </div> <div id="shop-hours" class="shop-hours Hide"> <h3 class="title">修改时间</h3> <textarea></textarea> <p class="action"> <a class="J-cancel">取消</a> <a class="btn J-confirm">保存修改</a> </p> </div> <div id="stop-info" class="stop-info J-park-more Hide"> </div> <div id="promoinfo-wrapper"></div> <div id="joybooking-wrapper"></div> <div id="shoptabs-wrapper"></div> <div id="myreview-wrapper"></div> <div id="friends-comment" class="mod comment friends-comment"> <div id="friends-comment-head"></div> <ul class="comment-list J-list" id="friend-reviewlist-wrapper"></ul> <div id="friends-comment-tail"></div> <div id="qqfriends-comment-head"></div> <div class="qq-friends" id="qq-friends-wrapper"> <h3 class="names" id="qq-friends-names"></h3> <div class="avatars clearfix" id="qq-friends-avatars"></div> </div> </div> <div id="comment" class="mod comment" data-render="1"> <h2 class="mod-title J-tab" id="defaultcomment-wrapper"></h2> <div id="summaryfilter-wrapper"></div> <div id="attributefilter-wrapper"></div> <ul class="comment-list J-list" id="reviewlist-wrapper"></ul> <div id="morelink-wrapper"></div> </div> <div id="addreview-wrapper"></div> <div id="relatedeal-wrapper"></div> <div class="mod shop-owner"> <h2 class="mod-title"> <a class="item current">App专享优惠</a> </h2> </div> </div> <div id="aside" class="aside"> <div id="aside-photos" class="photos-container"></div> <div id="aside-bottom"></div> </div> </div> </div> <div class="footer-container"> <div id="channel-footer" class="channel-footer"> <p class="links"> <a target="_blank" href="https://about.meituan.com" rel="nofollow">关于我们</a>| <a target="_blank" href="https://dpapp-appeal.meituan.com/#/shopCreditRegulationPC" rel="nofollow">商户诚信公约</a>| <a target="_blank" href="https://rules-center.meituan.com/?from=dianpingPC" rel="nofollow">规则中心</a>| <a target="_blank" href="https://about.meituan.com/news/report" rel="nofollow">媒体报道</a>| <a target="_blank" href="https://e.dianping.com/claimcpc/page/index?source=dp" rel="nofollow">商户入驻</a>| <a target="_blank" href="//www.dianping.com/business/" rel="nofollow">推广服务</a>| <a target="_blank" href="https://join.dianping.com/" rel="nofollow">人才招聘</a>| <span class="links-container"> <a class="ext-links" href="javascript:void(0);" rel="nofollow">最新咨询</a>| </span> <a target="_blank" rel="nofollow" href="https://about.meituan.com/contact?source=dp" rel="nofollow">联系我们</a>| <a target="_blank" href="http://www.dianping.com/app/download">应用下载</a> </p> <div class="ext-container Hide"> <div class="link-items Hide"> <a target="_blank" href="//www.dianping.com/discovery/"><span>资讯评论精选</span></a> </div> </div> <p class="rights"> <span style="margin-right:10px;">©2003-2020 dianping.com, All Rights Reserved.</span> <span>本站发布的所有内容，未经许可，不得转载，详见 <a rel="nofollow" class="G" href="https://rules-center.meituan.com/rules-detail/69">《知识产权声明》</a>。 </span> </p> </div> <script> var _hmt = _hmt || []; (function() { var hm = document.createElement("script"); hm.src = "https://hm.baidu.com/hm.js?602b80cf8079ae6591966cc70a3940e7"; var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(hm, s); })(); </script> <script> (function(){var h=navigator.userAgent;var i=navigator.appName;var b=i.indexOf("Microsoft Internet Explorer")!==-1;if(!b){return false}var d=/MSIE (\d+).0/g;var e=d.exec(h);if(e&&e.length&&e[1]<9){var j="<div class="browser-overlay"></div><div id="browser-ie-con" class="browser-ie-con"><div id="browser-close" class="close">×</div><div class="browser-download chrome"><a href="//www.google.cn/chrome/browser/desktop/index.html?utm_dp" target="_black" title="chrome"></a></div><div class="browser-download firefox"><a href="//www.firefox.com.cn/download/?utm_dp" target="_black" title="firefox"></a></div></div>";var f=document.createElement("div");f.id="browser-update-ie";f.className="browser-update-ie";f.innerHTML=j;document.body.appendChild(f);var a=document.documentElement.clientWidth||document.body.clientWidth;var c=document.getElementById("browser-ie-con").offsetWidth;var g=(a-c)/2;document.getElementById("browser-ie-con").style.left=g+"px";document.getElementById("browser-close").attachEvent("onclick",function(){document.getElementById("browser-update-ie").style.display="none"},false)}})(); </script> </div> <script> window.shop_config={ userId: 0, shopId: "G19NvNJMMSqkNCHk", shopCityId: 1, shopName: "<e class="address">&#xe591;</e><e class="address">&#xf388;</e><e class="address">&#xed7d;</e><e class="address">&#xf330;</e>SPA·MASSAGE", address: "<e class="address">&#xe821;</e><e class="address">&#xe383;</e><e class="address">&#xeb8b;</e>1<d class="num">&#xe5cd;</d><d class="num">&#xf295;</d><d class="num">&#xf295;</d><e class="address">&#xe709;</e>", publicTransit: "", cityId: "1", cityCnName: "上海", cityName: "上海", cityEnName: "shanghai", isOverseasCity: 0, power:5, shopPower:50, voteTotal:0, district:0, shopType:30, mainRegionId:803, categoryURLName:"life", shopGroupId: "G19NvNJMMSqkNCHk", loadUserDomain:"//www.dianping.com", map:{ power:5, manaScore:"0" }, mainCategoryId:141, defaultPic:"https://p0.meituan.net/dpmerchantpic/ee2edf4e948e3bf4ccf75bd8e973a332346644.jpg%40300w_225h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20", textCssVersion:"eovvulq7p2", shopEvtId:"G19NvNJMMSqkNCHk" } </script> <script src="//www.dpfile.com/app/app-pc-main/static/common.min.afe724462da9ff529198b050b4795387.js" type="text/javascript"></script><script src="//www.dpfile.com/app/app-pc-main/static/main-shop.min.2d62b833d420684083957ec33c835812.js" type="text/javascript"></script> <script crossorigin="anonymous" src="//www.dpfile.com/app/owl/static/owl.min.57e7d73af5de4934d3f7cae341d504fa.js"></script> <script> Owl.start({ project: "app-pc-main-shop", pageUrl: "main-shop" }) </script> </body> </html>'
    spider = SpiderDZDP()
    try:
        # for page in range(50):
        #     index_page(page)
        #     time.sleep(10)
        spider.index_page(1)
        # spider.test(testHtml)
    except Exception as e:
        print("出错了", e)
    finally:
        print("关闭浏览器")
        # spider.browser.close()
