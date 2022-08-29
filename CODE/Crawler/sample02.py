import requests

url = 'https://www.sogou.com/sie?query=周杰伦'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'
}
resp = requests.get(url, headers=headers)
print(resp.text)
resp.close()
