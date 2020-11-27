from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pyquery import PyQuery
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import module.mongo_database as md
import re
import requests
import time
from fontTools.ttLib import TTFont
import os

from proxypool.storages.redis_db import RedisClient


class SpiderDZDP():

    def __init__(self):
        self.entry_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
                    'Host': 'www.dianping.com',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                    'Referer': 'http://www.dianping.com/',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    }

        # 无界面模式
        self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_argument('--headless')
        # fire_options = webdriver.FirefoxOptions()
        # fire_options.add_argument('--headless')

        # 代理
        # self.chrome_options.add_argument('--proxy-server=http://%s' % str(RedisClient.random()))

        # self.browser = webdriver.Chrome()
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        # browser = webdriver.Firefox()
        # browser = webdriver.Firefox(firefox_options=fire_options)


        self.wait = WebDriverWait(self.browser, 20)

        self.cookies = [
{
    "domain": ".dianping.com",
    "expirationDate": 1637198001,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_hc.v",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "0267b309-3904-cc87-7f6f-06a52aa7e104.1605662001",
    "id": 1
},
{
    "domain": ".dianping.com",
    "expirationDate": 1606958540,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_lx_utm",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "utm_source%3DBaidu%26utm_medium%3Dorganic",
    "id": 2
},
{
    "domain": ".dianping.com",
    "expirationDate": 1700270000,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_lxsdk",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8",
    "id": 3
},
{
    "domain": ".dianping.com",
    "expirationDate": 1700270000,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_lxsdk_cuid",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8",
    "id": 4
},
{
    "domain": ".dianping.com",
    "expirationDate": 1606379475,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_lxsdk_s",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "176038aa782-e4e-203-0d6%7C%7C260",
    "id": 5
},
{
    "domain": ".dianping.com",
    "expirationDate": 1637198063.948732,
    "hostOnly": False,
    "httpOnly": False,
    "name": "aburl",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 6
},
{
    "domain": ".dianping.com",
    "expirationDate": 1637830044.338862,
    "hostOnly": False,
    "httpOnly": False,
    "name": "ctu",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "9094b28b3618ed0de6c888c89606527ac522f7d11957b989ed480f33132407ab",
    "id": 7
},
{
    "domain": ".dianping.com",
    "expirationDate": 1609032215.236423,
    "hostOnly": False,
    "httpOnly": False,
    "name": "cy",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 8
},
{
    "domain": ".dianping.com",
    "expirationDate": 1609032215.236543,
    "hostOnly": False,
    "httpOnly": False,
    "name": "cye",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "shanghai",
    "id": 9
},
{
    "domain": ".dianping.com",
    "expirationDate": 1606398788.102691,
    "hostOnly": False,
    "httpOnly": True,
    "name": "dper",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "0e0250c1188016d13ee6653a92fc7bc9b3b408b0aa7146a1eff3a94d6f7e8e2401d0f01202f4d046f203e6cbdcd579df76afff23a46140b6610798b1f4fdd0d8aaae353fc156a936665b9ee145c9b2ea806e96e6d6ce16c8899508135040656f",
    "id": 10
},
{
    "domain": ".dianping.com",
    "expirationDate": 1606398788.10262,
    "hostOnly": False,
    "httpOnly": True,
    "name": "dplet",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "a13ef22a730ce62ff67dfd1c0967b6a9",
    "id": 11
},
{
    "domain": ".dianping.com",
    "expirationDate": 1606898202.128948,
    "hostOnly": False,
    "httpOnly": False,
    "name": "fspop",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "test",
    "id": 12
},
{
    "domain": ".dianping.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "Hm_lpvt_602b80cf8079ae6591966cc70a3940e7",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "1606377675",
    "id": 13
},
{
    "domain": ".dianping.com",
    "expirationDate": 1637913675,
    "hostOnly": False,
    "httpOnly": False,
    "name": "Hm_lvt_602b80cf8079ae6591966cc70a3940e7",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1606215775,1606217747,1606293404,1606353741",
    "id": 14
},
{
    "domain": ".dianping.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "ll",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "7fd06e815b796be3df069dec7836c3df",
    "id": 15
},
{
    "domain": ".dianping.com",
    "expirationDate": 1669445640.371538,
    "hostOnly": False,
    "httpOnly": False,
    "name": "s_ViewType",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "10",
    "id": 16
},
{
    "domain": ".dianping.com",
    "expirationDate": 1637889815.033459,
    "hostOnly": False,
    "httpOnly": False,
    "name": "ua",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "dpuser_0671354772",
    "id": 17
}
]

        # 字体库
        self.basefont_char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '店', '中', '美', '家', '馆', '小', '车', '大', '市',
                         '公', '酒',
                         '行', '国', '品', '发', '电', '金', '心', '业', '商', '司', '超', '生', '装', '园', '场', '食', '有', '新', '限',
                         '天', '面',
                         '工', '服', '海', '华', '水', '房', '饰', '城', '乐', '汽', '香', '部', '利', '子', '老', '艺', '花', '专', '东',
                         '肉', '菜',
                         '学', '福', '饭', '人', '百', '餐', '茶', '务', '通', '味', '所', '山', '区', '门', '药', '银', '农', '龙', '停',
                         '尚', '安',
                         '广', '鑫', '一', '容', '动', '南', '具', '源', '兴', '鲜', '记', '时', '机', '烤', '文', '康', '信', '果', '阳',
                         '理', '锅',
                         '宝', '达', '地', '儿', '衣', '特', '产', '西', '批', '坊', '州', '牛', '佳', '化', '五', '米', '修', '爱', '北',
                         '养', '卖',
                         '建', '材', '三', '会', '鸡', '室', '红', '站', '德', '王', '光', '名', '丽', '油', '院', '堂', '烧', '江', '社',
                         '合', '星',
                         '货', '型', '村', '自', '科', '快', '便', '日', '民', '营', '和', '活', '童', '明', '器', '烟', '育', '宾', '精',
                         '屋', '经',
                         '居', '庄', '石', '顺', '林', '尔', '县', '手', '厅', '销', '用', '好', '客', '火', '雅', '盛', '体', '旅', '之',
                         '鞋', '辣',
                         '作', '粉', '包', '楼', '校', '鱼', '平', '彩', '上', '吧', '保', '永', '万', '物', '教', '吃', '设', '医', '正',
                         '造', '丰',
                         '健', '点', '汤', '网', '庆', '技', '斯', '洗', '料', '配', '汇', '木', '缘', '加', '麻', '联', '卫', '川', '泰',
                         '色', '世',
                         '方', '寓', '风', '幼', '羊', '烫', '来', '高', '厂', '兰', '阿', '贝', '皮', '全', '女', '拉', '成', '云', '维',
                         '贸', '道',
                         '术', '运', '都', '口', '博', '河', '瑞', '宏', '京', '际', '路', '祥', '青', '镇', '厨', '培', '力', '惠', '连',
                         '马', '鸿',
                         '钢', '训', '影', '甲', '助', '窗', '布', '富', '牌', '头', '四', '多', '妆', '吉', '苑', '沙', '恒', '隆', '春',
                         '干', '饼',
                         '氏', '里', '二', '管', '诚', '制', '售', '嘉', '长', '轩', '杂', '副', '清', '计', '黄', '讯', '太', '鸭', '号',
                         '街', '交',
                         '与', '叉', '附', '近', '层', '旁', '对', '巷', '栋', '环', '省', '桥', '湖', '段', '乡', '厦', '府', '铺', '内',
                         '侧', '元',
                         '购', '前', '幢', '滨', '处', '向', '座', '下', '県', '凤', '港', '开', '关', '景', '泉', '塘', '放', '昌', '线',
                         '湾', '政',
                         '步', '宁', '解', '白', '田', '町', '溪', '十', '八', '古', '双', '胜', '本', '单', '同', '九', '迎', '第', '台',
                         '玉', '锦',
                         '底', '后', '七', '斜', '期', '武', '岭', '松', '角', '纪', '朝', '峰', '六', '振', '珠', '局', '岗', '洲', '横',
                         '边', '济',
                         '井', '办', '汉', '代', '临', '弄', '团', '外', '塔', '杨', '铁', '浦', '字', '年', '岛', '陵', '原', '梅', '进',
                         '荣', '友',
                         '虹', '央', '桂', '沿', '事', '津', '凯', '莲', '丁', '秀', '柳', '集', '紫', '旗', '张', '谷', '的', '是', '不',
                         '了', '很',
                         '还', '个', '也', '这', '我', '就', '在', '以', '可', '到', '错', '没', '去', '过', '感', '次', '要', '比', '觉',
                         '看', '得',
                         '说', '常', '真', '们', '但', '最', '喜', '哈', '么', '别', '位', '能', '较', '境', '非', '为', '欢', '然', '他',
                         '挺', '着',
                         '价', '那', '意', '种', '想', '出', '员', '两', '推', '做', '排', '实', '分', '间', '甜', '度', '起', '满', '给',
                         '热', '完',
                         '格', '荐', '喝', '等', '其', '再', '几', '只', '现', '朋', '候', '样', '直', '而', '买', '于', '般', '豆', '量',
                         '选', '奶',
                         '打', '每', '评', '少', '算', '又', '因', '情', '找', '些', '份', '置', '适', '什', '蛋', '师', '气', '你', '姐',
                         '棒', '试',
                         '总', '定', '啊', '足', '级', '整', '带', '虾', '如', '态', '且', '尝', '主', '话', '强', '当', '更', '板', '知',
                         '己', '无',
                         '酸', '让', '入', '啦', '式', '笑', '赞', '片', '酱', '差', '像', '提', '队', '走', '嫩', '才', '刚', '午', '接',
                         '重', '串',
                         '回', '晚', '微', '周', '值', '费', '性', '桌', '拍', '跟', '块', '调', '糕']

        # 店铺名称提取正则表达式
        self.shop_name_re = '.*<h1 class="shop-name">(.*)<a class="qr-contrainer".*</h1>'

    def index_page(self, page):
        """
        抓取页面
        :param page:
        :return:
        """
        print('正在爬取第 %s 页' % page)
        try:
            # self.chrome_options.add_argument('--proxy-server=http://%s' % str(RedisClient().random()))
            # self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
            entry_link = "http://www.dianping.com/shanghai/ch30/p" + str(page)
            self.browser.get(entry_link)
            for cookie in self.cookies:
                self.browser.add_cookie(cookie)
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page .cur"), str(page)))
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#shop-all-list ul li")))
            self.get_shop_redirect_url()
        except Exception as e:
            print("超时了", e)
            # self.index_page(page)
    def get_shop_redirect_url(self):
        """
        获取当前页面跳转详情页集合
        :return:
        """
        html = self.browser.page_source
        doc = PyQuery(html)
        items = doc("#shop-all-list ul li").items()
        for item in items:
            redirect_url = item.find(".txt .tit a").attr("href")
            # self.chrome_options.add_argument('--proxy-server=http://%s' % str(RedisClient().random()))
            # self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
            self.browser.get(redirect_url)
            for cookie in self.cookies:
                self.browser.add_cookie(cookie)

            # 获取字体库
            self.get_dictionary(redirect_url)
            # 获取店铺信息
            self.get_shop_info()
            # 获取评论信息
            self.get_comment_info()
            time.sleep(10)
    def get_shop_info(self):
        html = self.browser.page_source
        doc = PyQuery(html)
        shopInfo = {
            "shopName": self.fetch_info("spider_dzdp_address", re.findall(self.shop_name_re, html)), #doc.find("#basic-info .shop-name").text().replace("\n", ""),
            # "starWrapper": doc.find("#basic-info .star-wrapper .mid-score").text().replace("\n", ""),
            # "reviewCount": doc.find("#reviewCount").text().replace("\n", ""),
            # "avgPriceTitle": doc.find("#avgPriceTitle").text().replace("\n", ""),
            # "address": doc.find("#address").text().replace("\n", "")
        }
        # 评分
        # "commentScoreTasete": doc.find("#comment_score ")
        print(shopInfo)
        return

    def get_comment_info(self):
        html = self.browser.page_source
        doc = PyQuery(html)

        return

    def get_dictionary(self, url):
        # self.chrome_options.add_argument('--proxy-server=http://%s' % str(RedisClient().random()))
        # self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.browser.get(url)
        for cookie in self.cookies:
            self.browser.add_cookie(cookie)
        html = self.browser.page_source
        # 拿到含有字体的css_url
        pattern = re.compile('.*href="(//s3plus.*.css)"> <link.*', re.S)
        css_url = re.findall(pattern, html)
        # 拿到字体的url
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36'
        }
        if len(css_url) == 0:
            print("没有获取到字体链接")
            return
        woff_html = requests.get('http:' + css_url[0], headers=headers)
        woff_url = ['http:' + url for url in re.findall(",url\(\"(.*?)\"\);}", woff_html.text)]
        # 拿到字体的名字
        woff_names = re.findall('font-family: "PingFangSC-Regular-(.*?)";', woff_html.text)
        # 将字体名字和url一一对应起来
        woff_name_url = {}
        for i in range(len(woff_names)):
            if woff_names[i] != 'reviewTag':  # 这样处理的原因是本例中用不到reviewTag这个字体文件，并且它是重复的，所以去掉它。
                woff_name_url[woff_names[i]] = woff_url[i]
        print(woff_name_url)
        # 字体key列表放入缓存
        for key in woff_name_url.keys():
            redisKey = "spider_dzdp_%s" % key
            # 下载字体
            response = requests.get(woff_name_url[key], headers=headers)
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
            RedisClient().setRedis(redisKey, ','.join(font_keys[2:]), 600)
            # 删除字体文件
            os.remove('%s.woff' % key)
            time.sleep(1)

    def fetch_info(self, woff_name_key, re_str):
        print(re_str)
        if re_str is None:
            print("待替换文本不存在")
            return re_str
        # 从缓存获取字典
        dictStr = RedisClient().getRedis(woff_name_key)
        # 转换成列表
        if dictStr is None:
            print("字体列表不存在")
            return re_str
        dictList = dictStr.split(",")
        # 不同字体名称有不同的标签，需要区分
        # 1.店铺名称
        if "spider_dzdp_address" == woff_name_key:
            # 找出需要替换的加密字体
            pattern = re.compile('.*?<e class="address">(.*?)</e>.*?', re.S)
            need_decode = re.findall(pattern, re_str[0])
            print(need_decode)
            if len(need_decode) == 0:
                print("没有可匹配的加密字体")
                return
            # 店铺名称加密标签替换成空字符串
            re_str = re_str[0].replace('<e class="address">', '').replace('</e>', '')
            # 利用字体库，替换加密字体
            for need in need_decode:
                # 格式跟数据库格式不一致，替换成一致
                need = 'uni'.join(need[2:])
                # 获取加密字体库的下标位置
                index_position = dictList.index(need)
                print(need,index_position)
                # 替换解密字体
                re_str = re_str.replace(need, self.basefont_char[index_position])

            return re_str

        return re_str
if __name__ == '__main__':
    spider = SpiderDZDP()
    try:
        # for page in range(50):
        #     index_page(page)
        #     time.sleep(10)
        spider.index_page(1)
    except Exception as e:
        print("出错了", e)
    finally:
        print("关闭浏览器")
        spider.browser.close()
