import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.umei.cc/meinvtupian/meinvxiezhen/'
resp = requests.get(url)
resp.encoding = 'utf-8'
m = 1
main_page = BeautifulSoup(resp.text, 'html.parser')
alist = main_page.find("ul", attrs={"class": "pic-list after"}).find_all("a")
slide_list = main_page.find("div", attrs={"class": "swiper-wrapper after"}).find_all("a")
# print(alist)
# f = open(f"tu_{m}.jpg", mode='wb')

for a in alist[1:]:
    domain = 'https://www.umei.cc'
    href = domain + a.get('href')
    print('图片组:', href)
    resp_child = requests.get(href)
    resp_child.encoding = 'utf-8'
    child_page = BeautifulSoup(resp_child.text, 'html.parser')
    child_page = child_page.find('div', attrs={'class': 'content-box'}).find_all('a')
    # print(child_page)
    for a1 in child_page:
        print(domain + a1.get('href'))
        resp_child.close()
        break
    break
    # content = requests.get(img.get('data-src')).content
    # f.write(content)
    # print('第', m, '张图片下载完成')
    # m += 1
    # time.sleep(5)
    # child_page =

# print('滑窗内容为:')
# for img in slide_list:
#     print(img.get('data-src'))
# print(alist)
resp.close()
