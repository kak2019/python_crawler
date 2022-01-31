from urllib.parse import parse_qs,parse_qsl

from urllib.parse import urlencode

params = {
    'name':'flynt',
    'age': "24"
}
base_url = "https://www.baidu.com"

url = base_url+urlencode(params)
print(url)

print(parse_qs(url))
print(parse_qsl(url))