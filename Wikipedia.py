import requests

# Wikipedia API URL
url = "https://en.wikipedia.org/w/api.php"

# 参数
params = {
    "action": "query",
    "format": "json",
    "titles": "Python_(programming_language)",  # 替换为您要获取的页面标题
    "prop": "extracts",
    "explaintext": True
}

# 发送请求
response = requests.get(url, params=params)
data = response.json()

# 提取页面内容
page_id = list(data["query"]["pages"].keys())[0]
page_title = data["query"]["pages"][page_id]["title"]
page_content = data["query"]["pages"][page_id]["extract"]

print("Title:", page_title)
print("Content:", page_content)
