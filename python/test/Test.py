import requests


headers = {
    'Cookie': 'cy=1; cye=shanghai; _lxsdk_cuid=17604c6746761-072f44f27fa8e6-c791e37-1fa400-17604c67468a6; _lxsdk=17604c6746761-072f44f27fa8e6-c791e37-1fa400-17604c67468a6; _hc.v=b4d5fcf5-4318-2deb-4d21-1bb0d1ad115b.1606397884; s_ViewType=10; fspop=test; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1606397884,1606564506,1607214930; lgtoken=07601ee17-4464-4a9a-a544-da6c1711ba26; dplet=d54bcfece85ba2538cb451e2d420fda6; dper=8bb62f838991f97ed3b646e60802177316409476d11fe91f50ca6389be5480d3b15eeab72f19b2df3f4b8ff154b98c841d19c66550e0b8dc0314bbb6574bd918ecb94f9df8bc32fb8ea9013478d342f58e2944b71c5474903e15038de9b9cc1f; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_7445491144; ctu=79ae6d5d7d147d898187b31ce77f66206c18e469f57d9c0a0de111522e35bb9a; uamo=17321437793; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1607215007; _lxsdk_s=1763579971e-08e-0e9-3ca%7C%7C254',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
    'Host': 'www.dianping.com',
    'Referer': 'http://www.dianping.com/shop/G7lZQSVUguP43EIT'
}

url = 'http://www.dianping.com/shop/l35tKdqLK2r6SbXm/review_all/p20'

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(requests.get(url, headers=headers).text)