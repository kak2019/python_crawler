import socket
import urllib.request
import ssl


try:
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen("https://www.httpbin.org/get",timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("Time Out")