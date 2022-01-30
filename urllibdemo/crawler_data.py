import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

data = bytes(urllib.parse.urlencode({'name':'flynt'}),encoding="utf-8")
response = urllib.request.urlopen("https://www.httpbin.org/post",data=data)

print(response.read().decode("utf-8"))