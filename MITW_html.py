import re
from lxml import html

file_path = "C:\\CYLab_Hsuan\\MITW_WebCrawler\\台灣醫學資訊聯測松(MI-TW)-網站.html"
with open(file_path, "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

# 使用lxml解析HTML内容
tree = html.fromstring(html_content)

# # 使用XPath提取内容 ##全部 純HTML##
# elements = tree.xpath("//html")  # 这里假设您希望提取整个HTML标签内容
#
# for element in elements:
#     print(html.tostring(element, encoding="unicode"))

# # 使用XPath提取内容并去除html标签
elements = tree.xpath("//html/body/*")  # 这里假设内容在<body>标签内
# 将内容转换为字符串并打印
for element in elements:
    content = html.tostring(element, encoding="unicode")
    print(content)

    #<div id="doc" class="markdown-body container-fluid comment-enabled" data-hard-breaks="true">
# 使用XPath选择要移除的内容
content_to_remove_xpath = "//div[@id='doc' and contains(@class, 'markdown-body') and contains(@class, 'container-fluid') and contains(@class, 'comment-enabled') and @data-hard-breaks='true']\
                          | //div[@class='title-tags-preview']\
                          | //button[contains(@class, 'text-gray-500')]"
# content_to_remove_xpath = "//div[@class='title-tags-preview']"

# 替换为要移除的内容的XPath
elements_to_remove = tree.xpath(content_to_remove_xpath)

# 移除选择的内容
for element in elements_to_remove:
    parent = element.getparent()
    parent.remove(element)

# 获取更新后的HTML内容并打印
updated_html_content = html.tostring(tree, encoding="unicode")
print(updated_html_content)



## 移除HTML标签并打印内容 ##拿掉html 純文字##
# for element in elements:
#     extracted_text = element.text_content()  # 获取标签内的纯文本内容
#     print(extracted_text)

# # 将HTML内容写入文件
# with open("extracted_html.html", "w", encoding="utf-8") as extracted_file:
#     for element in elements:
#         extracted_file.write(html.tostring(element, encoding="unicode"))
#
# print("HTML内容已提取并保存为 extracted_html.html")



# print("HTML内容已提取并保存为 extracted_html.html")