#  定位2022必看片 -> 提取子页面链接地址
import requests
import re
import time

domain = 'https://dytt89.com/'
resp = requests.get(domain)
resp.encoding = 'gb2312'

obj1 = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)  # re.S表示全局搜索，不仅在本行内
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="'
                  r'(?P<download>.*?)">', re.S)

result = obj1.finditer(resp.text)
child_href_list = []
for i in result:
    ul = i.group('ul')

    #  提取子页面网址
    result2 = obj2.finditer(ul)
    for j in result2:
        child_href = domain + j.group('href').strip('/')
        child_href_list.append(child_href)
#  提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    time.sleep(0.5)
    print(result3.group('movie'), end='     ')
    print('下载地址:', result3.group('download'))
resp.close()
