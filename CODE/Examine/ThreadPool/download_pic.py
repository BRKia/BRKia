import requests
import re
import json
from lxml import html
from concurrent.futures import ThreadPoolExecutor


def download(imgsrc):
    # print(imgsrc)
    name = imgsrc.split('/')[-1]
    print(f'准备开始下载{name}')
    resp_child_child_img = requests.get(imgsrc)  # 拿对应的超链接对网络请求
    with open(f'img/{name}', mode='wb') as f:
        f.write(resp_child_child_img.content)
    print(f'{name}下载完毕!')
    f.close()


def main():
    url2 = 'https://desk.zol.com.cn/bizhi/9922_119187_2.html'
    domain = 'https://desk.zol.com.cn'
    resp_child = requests.get(url2)
    resp_child.encoding = 'gbk'
    # etree = html.etree
    # # et = etree.HTML(resp_child.text)
    obj = re.compile(r"var deskPicArr.*?=(?P<deskPicArr>.*?);", re.S)
    result = obj.search(resp_child.text)
    deskPicStr = result.group('deskPicArr')  # 从正则.*?提取的内容为字符串
    # 把类似字典的字符串变成字典
    deskPic = json.loads(deskPicStr)
    # text = et.xpath("//div[@class='wrapper photo-tit clearfix']/h3/a/text()")
    # text = text[0]
    # print(text, ':')
    with ThreadPoolExecutor(10) as t:
        for item in deskPic['list']:
            oriSize = item.get('oriSize')  # 拿到图片大小
            imgsrc = item.get('imgsrc')
            # print(oriSize, imgsrc)
            imgsrc = imgsrc.replace('##SIZE##', oriSize)  # 字符串替换
            t.submit(download, imgsrc)
    print('下载完成!')
    resp_child.close()


if __name__ == '__main__':
    main()
