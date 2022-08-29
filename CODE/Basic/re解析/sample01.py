import requests
import re
import csv

#  拿到页面源代码 -> 提取有效信息
#  request -> re

url = 'https://movie.douban.com/top250?start=0&filter='
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
resp = requests.get(url, headers=headers)
# print(resp.content)
pageContent = resp.text
#  解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<rank>.*?)</span>'
                 r'.*?<span>(?P<comment>.*?)人评价</span>', re.S)
# result = obj.findall(pageContent)
result = obj.finditer(pageContent)
for i in result:
    print(i.group('name'), end=' ')
    print(i.group('rank'), end=' ')
    print(i.group('comment'), end=' ')
    print(i.group('year').strip())
resp.close()
