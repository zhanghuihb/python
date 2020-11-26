import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

url = "http://www.dianping.com/shop/G7lZQSVUguP43EIT"

html = requests.get(url, headers=headers)
print(html.text)
shop_names = re.findall('.*?<h1 class="shop-name">(.*?)<a class="qr-contrainer".*?</h1>', html.text)
print(shop_names)
font_keys = re.findall('.*?<e class="address">(.*?)</e>.*?', shop_names[0])
print(font_keys)
for font in font_keys:
    print(font.split(";")[0].replace("&#x", "uni"))