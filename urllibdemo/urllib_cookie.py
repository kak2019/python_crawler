import urllib.request,http.cookiejar
import ssl


ssl._create_default_https_context = ssl._create_unverified_context



cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

response = opener.open("https://www.baidu.com")
for item in cookie:
    print(item.name + "=" + item.value)

