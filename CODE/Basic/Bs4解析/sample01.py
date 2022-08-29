from bs4 import BeautifulSoup
import requests

url = 'https://www.chinamoney.com.cn/chinese/tycdgg/20220520/2377428.html#cp=tycd'
resp = requests.get(url)
# print(resp.text)

page = BeautifulSoup(resp.text, 'html.parser')  # 制定html解析器
print(page)
# 从bs对象中查找数据

