import requests

url = 'http://wapi.http.cnapi.cc/index/index/get_free_ip'
data = [{'page': page} for page in range(10)]

for d in data:
    r = requests.post(url, d)
    print(r)
    print(r.text)