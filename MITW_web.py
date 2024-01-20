import json
import requests
from lxml import html


#发送HTTP请求获取HackMD页面内容
url = "https://hackmd.io/riEKAy8wSEKe6YlDpnwTeQ?" ##MI-TW
response = requests.get(url)
print(response)
if response=="200":
    print(response)
    html_content = response.content
    # print(f"{html_content}\n")







