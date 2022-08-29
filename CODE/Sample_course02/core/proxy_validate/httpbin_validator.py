import requests
import time
import json
from Sample_course02 import settings
from Sample_course02.domain import Proxy
from Sample_course02.utils import http
from Sample_course02.utils.log import logger

def check_proxy(proxy):
    '''
    检测代理协议类型，匿名程度
    :param proxy:
    :return:
    '''
    proxies = {
        'http': "http://{}:{}".format(proxy.ip, proxy.port),
        'https': "https://{}:{}".format(proxy.ip, proxy.port)
    }

    http, http_nick_type, http_speed = _check_proxy(proxies)
    https, http_nick_types, http_speeds = _check_proxy(proxies, False)
    if http and https:
        # 如果二者都可以请求成功
        proxy.protocol = 2
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    elif http:
        proxy.protocol = 0
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    elif https:
        proxy.protocol = 1
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    else:
        proxy.protocol = -1
        proxy.nick_type = -1
        proxy.speed = -1

    logger.debug(proxy)
    return proxy

def _check_proxy(proxies, isHttp=True):
    nick_type = -1  # 匿名程度
    speed = -1  # 响应速度
    if isHttp:
        # 此处为测定http
        test_url = 'http://httpbin.org/get'
    else:
        test_url = 'https://httpbin.org/get'
    try:
        start = time.time()  # 获取开启的时间
        r = requests.get(url=test_url, headers=http.get_request_headers(), timeout=settings.TIMEOUT, proxies=proxies)
        if r.ok:
            speed = round(time.time() - start, 2)  # 计算响应时间
            content = json.load(r.text)  # 把响应内容转换为字典
            headers = content['headers']  # 获取请求头
            ip = content['origin']  # 获取origin，请求来源的IP地址
            proxy_connection = headers.get('Proxy-Connection', None)  # 获取请求头中'Proxy-Connection',如果有，说明匿名代理

            if ',' in ip:
                # 如果origin中有','分割，则两个IP是透明代理IP
                nick_type = 2  # 透明
            elif proxy_connection:
                # 如果headers中包含proxy-connection则是匿名代理IP
                nick_type = 1
            else:
                nick_type = 0  # 此时为高匿代理IP

            return True, nick_type, speed
        else:
            return False, nick_type, speed
    except Exception as e:
        logger.exception(e)
        return False, nick_type, speed

if __name__ == '__main__':
    proxy = Proxy('39.175.75.15', port='30001')
    print(check_proxy(proxy))






