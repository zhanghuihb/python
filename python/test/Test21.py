import re
import requests
from selenium import webdriver

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'Cookie': 'cy=1; cye=shanghai; _lxsdk_cuid=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _lxsdk=175d8e9c66fc8-0d6334719e6d83-7b10374c-1fa400-175d8e9c66fc8; _hc.v=0267b309-3904-cc87-7f6f-06a52aa7e104.1605662001; aburl=1; s_ViewType=10; fspop=test; ua=dpuser_0671354772; ctu=9094b28b3618ed0de6c888c89606527ac522f7d11957b989ed480f33132407ab; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1606217747,1606293404,1606353741,1606438349; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1606440469; _lxsdk_s=17607503d2f-54b-c4d-f85%7C%7C17'
}

url = "http://www.dianping.com/shop/H5xqIFZBWP0Zt3nd"

chrome_options = webdriver.ChromeOptions()
# 更换头部
# chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get(url)
html = browser.page_source
# html = requests.get(url, headers=headers).text
print(html)
shop_names = re.findall('.*?<h1 class="shop-name">(.*?)<a class="qr-contrainer".*?</h1>', html)
print(shop_names)
font_keys = re.findall('.*?<e class="address">(.*?)</e>.*?', shop_names[0])
print(font_keys)
for font in font_keys:
    print(font.split(";")[0].replace("&#x", "uni"))

browser.close()