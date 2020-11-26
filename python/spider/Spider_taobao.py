from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pyquery import PyQuery
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import module.mongo_database as md
import time

# 无界面模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# fire_options = webdriver.FirefoxOptions()
# fire_options.add_argument('--headless')

# cookie
cookies = [
{
    "domain": ".taobao.com",
    "expirationDate": 1637513814.260998,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_cc_",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "VFC%2FuZ9ajQ%3D%3D",
    "id": 1
},
{
    "domain": ".taobao.com",
    "expirationDate": 1606568305.426632,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_m_h5_tk",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "f566b4536bc0f652aded5631820d2e96_1605972143794",
    "id": 2
},
{
    "domain": ".taobao.com",
    "expirationDate": 1606568305.426711,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_m_h5_tk_enc",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "149741cea04a1145d19f3f24fed1f430",
    "id": 3
},
{
    "domain": ".taobao.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "_tb_token_",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": True,
    "storeId": "0",
    "value": "fb7fb36637568",
    "id": 4
},
{
    "domain": ".taobao.com",
    "expirationDate": 2236058305,
    "hostOnly": False,
    "httpOnly": False,
    "name": "cna",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "3HE1GLeUyygCAWVYVEBPoY2d",
    "id": 5
},
{
    "domain": ".taobao.com",
    "hostOnly": False,
    "httpOnly": True,
    "name": "cookie2",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": True,
    "storeId": "0",
    "value": "217e9a5b9186c50d95a1c31795293581",
    "id": 6
},
{
    "domain": ".taobao.com",
    "expirationDate": 1921309015.259912,
    "hostOnly": False,
    "httpOnly": True,
    "name": "enc",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "r%2BCVaCcxjy0xwVGMx%2BVanx5mGWvyqUG4FECgqeE%2BxYC0ml0LEXrVulCHN49A7aWddiFQDEdoLnPh5jzmgjKdkg%3D%3D",
    "id": 7
},
{
    "domain": ".taobao.com",
    "expirationDate": 1637513816.364702,
    "hostOnly": False,
    "httpOnly": False,
    "name": "hng",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "CN%7Czh-CN%7CCNY%7C156",
    "id": 8
},
{
    "domain": ".taobao.com",
    "expirationDate": 1621519544,
    "hostOnly": False,
    "httpOnly": False,
    "name": "isg",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "BCwsexReX0acwUtssp38AJnF_Qpe5dCPGMq_mYZtOFd6kcybrvWgHyIjsVkpAgjn",
    "id": 9
},
{
    "domain": ".taobao.com",
    "expirationDate": 1621519544,
    "hostOnly": False,
    "httpOnly": False,
    "name": "l",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "eBLpcFcnOkC5mgnoBOfanurza77OSIRYYuPzaNbMiOCP_yCB5xJdWZ71q4T6C3GVh6UvR37kyyKBBeYBqQAonxv92j-la_kmn",
    "id": 10
},
{
    "domain": ".taobao.com",
    "expirationDate": 1608569814.260818,
    "hostOnly": False,
    "httpOnly": False,
    "name": "lgc",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "%5Cu4F1A%5Cu80DC%5Cu7070%5Cu5C18",
    "id": 11
},
{
    "domain": ".taobao.com",
    "expirationDate": 1606051047.517163,
    "hostOnly": False,
    "httpOnly": False,
    "name": "lLtC1_",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 12
},
{
    "domain": ".taobao.com",
    "expirationDate": 1692364647.517049,
    "hostOnly": False,
    "httpOnly": False,
    "name": "miid",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "2073114195336874228",
    "id": 13
},
{
    "domain": ".taobao.com",
    "expirationDate": 1606582616.374686,
    "hostOnly": False,
    "httpOnly": False,
    "name": "mt",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "ci=5_1",
    "id": 14
},
{
    "domain": ".taobao.com",
    "expirationDate": 1637513814.260866,
    "hostOnly": False,
    "httpOnly": False,
    "name": "sgcookie",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "E1000yOhVlxQv5oWUnZJ6SDqVxBojU2QyWRwMnfb%2ByFlXDPefUW8B1ka8%2Ff0knIjWYs2E%2FxeYc1TztRoYQVZBbH%2FTA%3D%3D",
    "id": 15
},
{
    "domain": ".taobao.com",
    "expirationDate": 1613753814.260832,
    "hostOnly": False,
    "httpOnly": False,
    "name": "t",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "a600f5dec5ed04e7d4432a3f3235a5b1",
    "id": 16
},
{
    "domain": ".taobao.com",
    "expirationDate": 1621519544,
    "hostOnly": False,
    "httpOnly": False,
    "name": "tfstk",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "cCelBST0F7lSNBh01TM7XU_hDn6Owq9ESJyb3--KQuxe3KfcDIRZXZSmrz2pO",
    "id": 17
},
{
    "domain": ".taobao.com",
    "expirationDate": 1637053016,
    "hostOnly": False,
    "httpOnly": False,
    "name": "thw",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "cn",
    "id": 18
},
{
    "domain": ".taobao.com",
    "expirationDate": 1637513814.260966,
    "hostOnly": False,
    "httpOnly": False,
    "name": "tracknick",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "%5Cu4F1A%5Cu80DC%5Cu7070%5Cu5C18",
    "id": 19
},
{
    "domain": ".taobao.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "uc1",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": True,
    "storeId": "0",
    "value": "cookie14=Uoe0aDVuyXdMDw%3D%3D",
    "id": 20
},
{
    "domain": ".taobao.com",
    "expirationDate": 1608569814.260789,
    "hostOnly": False,
    "httpOnly": True,
    "name": "uc3",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "lg2=WqG3DMC9VAQiUQ%3D%3D&id2=VWhawy72R%2F2i&vt3=F8dCufwqQPNfcn0vBiE%3D&nk2=2DnRb0qZHgA%3D",
    "id": 21
},
{
    "domain": ".taobao.com",
    "expirationDate": 1608569814.26094,
    "hostOnly": False,
    "httpOnly": True,
    "name": "uc4",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "id4=0%40V8nS%2BZC2UcKcaD3ZFqCWAjEAk88%3D&nk4=0%402gzJ6tbJ985meckZ78aTvGy6Og%3D%3D",
    "id": 22
},
{
    "domain": ".taobao.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "v",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "0",
    "id": 23
},
{
    "domain": ".taobao.com",
    "expirationDate": 1606035409,
    "hostOnly": False,
    "httpOnly": False,
    "name": "xlly_s",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 24
},
{
    "domain": "s.taobao.com",
    "hostOnly": True,
    "httpOnly": False,
    "name": "alitrackid",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "www.taobao.com",
    "id": 25
},
{
    "domain": "s.taobao.com",
    "hostOnly": True,
    "httpOnly": True,
    "name": "JSESSIONID",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "680646C0FD12C3402630513E02891A29",
    "id": 26
},
{
    "domain": "s.taobao.com",
    "hostOnly": True,
    "httpOnly": False,
    "name": "lastalitrackid",
    "path": "/",
    "sameSite": "Lax",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "www.taobao.com",
    "id": 27
},
{
    "domain": "s.taobao.com",
    "expirationDate": 1605969097.087515,
    "hostOnly": True,
    "httpOnly": False,
    "name": "x5sec",
    "path": "/",
    "sameSite": "Lax",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "7b227365617263686170703b32223a223962666336346238313239303162376363623736636661623532613163623366434c713735503046454a54496e706e79716f75336c514561437a59334d5441324f5445324e447378227d",
    "id": 28
}
]

# browser = webdriver.Chrome()
# browser = webdriver.Firefox(firefox_options=fire_options)
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 10)
KEYWORD = 'IPAD'

def index_page(page):
    """
        抓取索引页
        ：:param page: 页码
    """
    print('正在爬取第 %s 页' % page)
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        # 用selenium切忌不要在打开网址之前就添加cookie，要不然就错 Message: invalid cookie domain
        for cookie in cookies:
            browser.add_cookie(cookie)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#mainsrp-pager li.item.active > span"), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".m-itemlist .items .item")))
        get_products()
    except TimeoutException as e:
        print("超时了", e)
        index_page(page)
def get_products():
    """提取商品数据"""
    html = browser.page_source
    doc = PyQuery(html)
    print(doc)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'productId': item.find('.title a').attr('data-nid'),
            'title': item.find('.title').text(),
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        md.save_to_mongo(product)
if __name__ == '__main__':
    try:
        for page in range(100):
            print(page)
            index_page(page)
            time.sleep(10)
    except Exception as e:
        print("出错了", e)
    finally:
        browser.close()