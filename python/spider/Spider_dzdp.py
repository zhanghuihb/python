from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pyquery import PyQuery
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import module.mongo_database as md
import time

entry_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
            'Host': 'www.dianping.com',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': 'http://www.dianping.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            }

# 无界面模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# fire_options = webdriver.FirefoxOptions()
# fire_options.add_argument('--headless')


# browser = webdriver.Chrome()
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Firefox()
# browser = webdriver.Firefox(firefox_options=fire_options)

wait = WebDriverWait(browser, 10)

cookies = [
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
        "expirationDate": 1606898203,
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
        "expirationDate": 1606295856,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_lxsdk_s",
        "path": "/",
        "sameSite": "Lax",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "175fe8c3788-282-f34-da3%7C%7C159",
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
        "expirationDate": 1608972444.590227,
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
        "expirationDate": 1608972444.59035,
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
        "expirationDate": 1606315644.338662,
        "hostOnly": False,
        "httpOnly": True,
        "name": "dper",
        "path": "/",
        "sameSite": "Lax",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "0e0250c1188016d13ee6653a92fc7bc994048a95c43a1122c6bbcd16d506c8f8a9a09369c3f0db6845afb3a7c3102501cc599165c951cb90ada7845097209fcd81f77f20489db8e94ff752594b2ec45d2adccf2125c5aa8c2e1c2f9ac2838d28",
        "id": 10
    },
    {
        "domain": ".dianping.com",
        "expirationDate": 1606315644.338522,
        "hostOnly": False,
        "httpOnly": True,
        "name": "dplet",
        "path": "/",
        "sameSite": "Lax",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "2473b0a6bd49a05fa6ea06ec40721f22",
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
        "value": "1606294057",
        "id": 13
    },
    {
        "domain": ".dianping.com",
        "expirationDate": 1637830056,
        "hostOnly": False,
        "httpOnly": False,
        "name": "Hm_lvt_602b80cf8079ae6591966cc70a3940e7",
        "path": "/",
        "sameSite": "Lax",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "1606179130,1606215775,1606217747,1606293404",
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
        "expirationDate": 1669366054.141891,
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
        "expirationDate": 1637830044.3388,
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
    },
    {
        "domain": ".dianping.com",
        "expirationDate": 1606315644.338925,
        "hostOnly": False,
        "httpOnly": False,
        "name": "uamo",
        "path": "/",
        "sameSite": "Lax",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "13917041591",
        "id": 18
    }
]

def index_page(page):
    """
    抓取页面
    :param page:
    :return:
    """
    print('正在爬取第 %s 页' % page)
    try:
        entry_link = "http://www.dianping.com/shanghai/ch30/p" + str(page)
        browser.get(entry_link)
        for cookie in cookies:
            browser.add_cookie(cookie)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page .cur"), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#shop-all-list ul li")))
        get_shop_redirect_url()
    except Exception as e:
        print("超时了", e)
        index_page(page)
def get_shop_redirect_url():
    """
    获取当前页面跳转详情页集合
    :return:
    """
    html = browser.page_source
    doc = PyQuery(html)
    items = doc("#shop-all-list ul li").items()
    print(items)
    for item in items:
        redirect_url = item.find(".txt .tit a").attr("href")
        print(redirect_url)
        browser.get(redirect_url)
        for cookie in cookies:
            browser.add_cookie(cookie)
        get_shop_info()
        get_comment_info()
        time.sleep(10)
def get_shop_info():
    html = browser.page_source
    # 替换加密字符
    dicts = getDictionary()
    for dictKey in dicts.keys():
        if dictKey in html:
            print("存在key和value",dictKey,dicts[dictKey])
            html  = html.replace(dictKey, dicts[dictKey])
    doc = PyQuery(html)
    shopInfo = {
        "shopName": doc.find("#basic-info .shop-name").text(),
        "starWrapper": doc.find("#basic-info .star-wrapper .mid-score").text(),
        "reviewCount": doc.find("#reviewCount").text(),
        "avgPriceTitle": doc.find("#avgPriceTitle").text(),
        "address": doc.find("#address").text()
    }
    # 评分
    # "commentScoreTasete": doc.find("#comment_score ")
    print("替换前",shopInfo)
    return

def get_comment_info():
    html = browser.page_source
    doc = PyQuery(html)

    return

def getDictionary():
    dictionary = {}
    dictionary['\&#xee17'] = "化"
    dictionary["\&#xf5d3"] = "学"
    dictionary["\&#xed95"] = "健"
    dictionary["\&#xe460"] = "泰"
    dictionary["\&#xee60"] = "机"
    dictionary["\&#xe377"] = "式"
    dictionary["\&#xf24c"] = "室"
    dictionary["\&#xf525"] = "南"
    dictionary["\&#xe698"] = "京"
    dictionary["\&#xf0bc"] = "西"
    dictionary["\&#xea6e"] = "路"
    dictionary["\&#xe310"] = "店"

    return dictionary
if __name__ == '__main__':
    try:
        # for page in range(50):
        #     index_page(page)
        #     time.sleep(10)
        index_page(1)
    except Exception as e:
        print("出错了", e)
    finally:
        print("关闭浏览器")
        browser.close()
