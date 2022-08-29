from lxml import html
import requests

url = 'https://desk.zol.com.cn/meinv/'
resp = requests.get(url)
resp.encoding = 'gbk'
print(resp.text)
resp.close()