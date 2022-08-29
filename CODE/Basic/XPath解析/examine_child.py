import requests
import re
import json
from lxml import html

'''
观察到页面内的script标签内有图片分辨率和下载地址的信息，故此处考虑使用re来解析
1.访问详情子页面，提取var deskPicArr = ‘xxxx’
2.分析deskPicArr，提取两个内容，imgsrc，orisize
3.将orisize插入到imgsrc的##SIZE##中，拿到图片的下载地址
'''

url2 = 'https://desk.zol.com.cn/bizhi/9922_119187_2.html'
domain = 'https://desk.zol.com.cn'
resp_child = requests.get(url2)
resp_child.encoding = 'gbk'
# print(resp_child_child.text)
etree = html.etree
et = etree.HTML(resp_child.text)
obj = re.compile(r"var deskPicArr.*?=(?P<deskPicArr>.*?);", re.S)
result = obj.search(resp_child.text)
deskPicStr = result.group('deskPicArr')  # 从正则.*?提取的内容为字符串
# 把类似字典的字符串变成字典
deskPic = json.loads(deskPicStr)
text = et.xpath("//div[@class='wrapper photo-tit clearfix']/h3/a/text()")
text = text[0]
# print(text, ':')
for item in deskPic['list']:
    oriSize = item.get('oriSize')  # 拿到图片大小
    imgsrc = item.get('imgsrc')
    # print(oriSize, imgsrc)
    imgsrc = imgsrc.replace('##SIZE##', oriSize)  # 字符串替换
    # print(imgsrc)

    resp_child_child_img = requests.get(imgsrc)  # 拿对应的超链接对网络请求
    name = imgsrc.split('/')[-1]
    with open(f'img_examine/{text}{name}', mode='wb') as f:
        f.write(resp_child_child_img.content)
print('下载完成!')
resp_child.close()
f.close()
