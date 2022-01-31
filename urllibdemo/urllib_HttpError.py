import ssl
from urllib import request,error

ssl._create_default_https_context = ssl._create_unverified_context
try:
    response = request.urlopen("https://cuiqingcai.com/404")
except error.HTTPError as e:
    print(e.reason,e.code,e.headers)