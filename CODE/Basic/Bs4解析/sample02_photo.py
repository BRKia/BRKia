import requests
from bs4 import BeautifulSoup
url = 'http://www.netbian.com/weimei/'
resp = requests.get(url)
resp.encoding = 'gbk'
main_page = BeautifulSoup(resp.text, 'html.parser')
aList = main_page.find('div', class_='list').find_all('img')
for img in aList:
    # print(a.get('alt'), end=' ')
    # print(a.get('src'))
    # 下载图片
    src = img.get('src')
    img_resp = requests.get(src)
    img_name = src.split('/')[-1]
    with open("img/"+img_name, mode='wb') as f:
        f.write(img_resp.content)
print('all over!')
f.close()
resp.close()

# print(aList)
# print(resp.text)
