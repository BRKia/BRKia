import time
import requests
from lxml import html
import re
import json
from concurrent.futures import ThreadPoolExecutor

domain = 'https://desk.zol.com.cn/'


def get_href(url):
    # 该函数负责获取详情页href值
    etree = html.etree
    resp = requests.get(url)
    resp.encoding = 'gbk'
    et = etree.HTML(resp.text)
    hrefs = et.xpath("//ul[@class='pic-list2  clearfix']/li/a/@href")
    resp.close()
    new_href = []
    for href in hrefs[1:]:
        new_href.append(domain + href)
    return new_href


def get_img_srcs(href):
    """
    访问每个详情页，拿到图片对应的下载路径
    """
    resp = requests.get(href)
    resp.encoding = 'gbk'
    obj = re.compile(r"var deskPicArr.*?=(?P<desk_str>.*?);", re.S)
    result = obj.search(resp.text).group('desk_str')
    desk = json.loads(result)
    img_list = []
    for item in desk['list']:
        oriSize = item.get('oriSize')
        img_src = item.get('imgsrc')
        img_src = img_src.replace('##SIZE##', oriSize)
        img_list.append(img_src)
    resp.close()
    return img_list


def download(img_src):
    name = img_src.split('/')[-1]
    print(f'开始下载{name}')
    resp = requests.get(img_src)
    with open(f'img/{name}', mode='wb') as f:
        f.write(resp.content)
    f.close()


def main():
    for i in range(1, 10):
        url = 'https://desk.zol.com.cn/pc/'
        if i != 1:
            url = url + f'{i}.html'
            # print(url)
        hrefs = get_href(url)
        imgs = []
        print('抓取到详情页的href')
        for href in hrefs:
            img_src = get_img_srcs(href)  # 访问每个详情页，拿到图片对应的下载路径
            for img in img_src:
                imgs.append(img)
        with ThreadPoolExecutor(20) as t:
            for img in imgs:  # 拿到图片的下载地址
                t.submit(download, img)
        print('第', i, '页all over')
        time.sleep(2)


if __name__ == '__main__':
    main()
