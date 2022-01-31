from urllib import parse

result = parse.urlsplit("https://www.baidu.com/index.html;user?id=5#comment")
print(result)

print(result.netloc,result[1])
unresult = parse.urlunsplit(result)
print(unresult)