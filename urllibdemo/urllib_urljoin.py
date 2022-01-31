from urllib.parse import urljoin

print(urljoin("https://www.baidu.com","FAQ.html"))
print(urljoin("https://www.baidu.com","https://cuiqingcai/FAQ.html"))
print(urljoin("https://www.baidu.com/about.html","https://cuiqingcai/FAQ.html"))
print(urljoin("https://www.baidu.com/about.html","https://cuiqingcai/FAQ.html?question=2"))
print(urljoin("https://www.baidu.com?wd=abc","https://cuiqingcai/FAQ.html/index.php"))
print(urljoin("https://www.baidu.com","?category=2#comment"))
print(urljoin("www.baidu.com","?category=2#comment"))
print(urljoin("https://www.baidu.com#comment","?category=2"))

