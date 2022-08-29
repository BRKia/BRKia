from lxml import html
import requests
import re
import json
import time

url = 'https://desk.zol.com.cn'
domain = 'https://desk.zol.com.cn'
resp = requests.get(url)
resp.encoding = 'gbk'
# print(resp.text)
etree = html.etree
et = etree.HTML(resp.text)
child = et.xpath("//dd[@class='brand-sel-box clearfix']/a/@href")
child = child[1:]
# print(child)
# 拿到总页面
for item in child:
    url1 = domain + item
    # print(url1)
    resp1 = requests.get(url1)
    resp1.encoding = 'gbk'
    # print(resp1.text)
    etree = html.etree
    et1 = etree.HTML(resp1.text)
    child_photo = et.xpath("//li/a[@class='pic']/@href")
    # print(child_photo)
    # 拿到小分区页面
    for item1 in child_photo:
        url2 = url + item1
        # print(url2)
        time.sleep(1)
        resp_child = requests.get(url2)
        resp_child.encoding = 'gbk'
        # print(resp_child_child.text)
        etree = html.etree
        et = etree.HTML(resp_child.text)
        obj = re.compile(r"var deskPicArr.*?=(?P<deskPicArr>.*?);", re.S)
        result = obj.search(resp_child.text)
        deskPicStr = result.group('deskPicArr')  # 从正则.*?提取的内容为字符串
        deskPic = json.loads(deskPicStr)  # 把类似字典的字符串变成字典
        text = et.xpath("//div[@class='wrapper photo-tit clearfix']/h3/a/text()")
        text = text[0]
        # print(text, ':')
        # 拿到照片页面
        for item1 in deskPic['list']:
            oriSize = item1.get('oriSize')  # 拿到图片大小
            imgsrc = item1.get('imgsrc')
            # print(oriSize, imgsrc)
            imgsrc = imgsrc.replace('##SIZE##', oriSize)  # 字符串替换
            # print(imgsrc)
            resp_child_child_img = requests.get(imgsrc)  # 拿对应的超链接对网络请求
            name = imgsrc.split('/')[-1]
            with open(f'img_examine/{text}{name}', mode='wb') as f:
                f.write(resp_child_child_img.content)
        print(text, '下载完成!')
        resp_child.close()
        f.close()
    resp1.close()
resp.close()
