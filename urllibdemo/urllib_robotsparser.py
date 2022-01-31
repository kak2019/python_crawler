from urllib.robotparser import RobotFileParser
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
rp = RobotFileParser()

rp.set_url("https://baidu.com/robots.txt")
rp.read()
print(rp.can_fetch("Baiduspider",'https://baidu.com'))