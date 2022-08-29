from lxml import html
import requests

url = 'https://desk.zol.com.cn/meinv/'
domain = 'https://desk.zol.com.cn'
resp = requests.get(url)
resp.encoding = 'gbk'
# print(resp.text)
etree = html.etree
et = etree.HTML(resp.text)
result = et.xpath("//ul[@class='pic-list2  clearfix']/li/a/@href")[1:]
for item in result:
    url = domain + item
    print(url)
resp.close()