import requests
from bs4 import BeautifulSoup # 从bs4这个库中导入BeautifulSoup
from selenium import webdriver

entry_link = "http://www.dianping.com/shanghai/ch10"
entry_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
           'Host': 'www.dianping.com',
           'Referer': 'http://www.dianping.com/shanghai/ch10',
           'Cookie': 'fspop=test; cy=1; cye=shanghai; _lxsdk_cuid=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _lxsdk=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _hc.v=0267b309-3904-cc87-7f6f-06a52aa7e104.1605662001; aburl=1; s_ViewType=10; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1605662008,1605662152,1605663061,1605748733; _lx_utm=utm_source%3Ddp_pc_event; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1605769464; _lxsdk_s=175df1a4171-acc-7b0-99e%7C%7C117'}
response = requests.get(entry_link, headers=entry_headers, timeout=5)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
# print(response.status_code)
# print(response.cookies)
# print(soup.find('div',class_='tit').a.text.strip())
# shopNameDivs = soup.find_all('div',class_='tit')
# shop_list = []
# for shopNameDiv in shopNameDivs:
#     shopName = shopNameDiv.a.text.strip()
#     shop_list.append(shopName)
# print(shop_list)

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
browser = driver.get('http://www.dianping.com/shop/G7lZQSVUguP43EIT')
comment = driver.find_element_by_css_selector('h1.shop-name')
print(comment)
