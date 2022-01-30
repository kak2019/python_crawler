import urllib.request,http.cookiejar
import ssl


ssl._create_default_https_context = ssl._create_unverified_context




filename = "cookie.txt"

cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

response = opener.open("https://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)