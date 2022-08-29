import requests
import pprint

url = 'https://fanyi.baidu.com/sug'
num = int(input('你要搜索的单词数： '))
for i in range(num):
    s = input('输入你要翻译的英文:')
    data = {
        'kw': s
    }
    #  post请求，发送的数据必须放在字典中，通过data参数进行传递
    resp = requests.post(url, data=data)
    pprint.pprint(resp.json())  # 将服务器返回的内容直接处理成json -> dict
    resp.close()
