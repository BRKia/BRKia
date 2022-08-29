import urllib.request

url = 'http://www.baidu.com/'
resp = urllib.request.urlopen(url)
with open('myBaidu.html', mode='wb') as f:
    f.write(resp.read())
print('over')
resp.close()
f.close()
