import urllib.request,http.cookiejar
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
cookie = http.cookiejar.LWPCookieJar()

cookie.load("cookie.txt",ignore_expires=True,ignore_discard=True)

handler  = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

reponse = opener.open("https://www.baidu.com")

print(reponse.read().decode("utf-8"))