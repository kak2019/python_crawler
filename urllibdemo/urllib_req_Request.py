from urllib import request, parse
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Host" : "www.httpbin.org"
}
dict = {"name":"flynt"}
data = bytes(parse.urlencode(dict),encoding="utf-8")
req = request.Request(url=url,data=data,headers=headers,method="POST")
response = request.urlopen(req)
print(response.read().decode("utf-8"))
