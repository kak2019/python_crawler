import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen("https://www.baidu.com")
#print(response.read().decode("utf-8"))

# print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))