from urllib.parse import urlencode

params = {
    'name':'flynt',
    'age': "24"
}
base_url = "https://www.baidu.com"

url = base_url+urlencode(params)
print(url)