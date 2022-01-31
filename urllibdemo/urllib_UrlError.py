from urllib import request,error
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
try:
    response = request.urlopen("https://cuiqingcai.com/404")
except error.URLError as e:
    print(e.reason)
