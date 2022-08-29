import requests as re
import pprint
import xlwt
import time
import random
import Sample_course01.crawl_init as crawl
from selenium.webdriver.common.by import By


# url_last = '&size=90&order=desc&order_by=amount&exchange=CN&market=CN&type=sha&_='
# url_type = ''
# url = url_pre + str(i) + url_last + random.choice(last)

def get_stockCount(code, headers, last_url):
    url = 'https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=90&order=desc&order_by=percent&exchange=CN&market=CN&ind_code=' + code + '&_=' + last_url
    response = re.get(url=url, headers=headers)
    json_data = response.json()
    # pprint.pprint(json_data)
    count = json_data['data']['count']
    count = count // 90 if count % 90 == 0 else count // 90 + 1
    # print(url)
    # print('该股票有',count, '页')
    return count


def re_getStockList(code, headers, last_url, count):
    # 需求：拿到一个股票代号 -> 网页链接
    # 求取：股票条数
    url_pre = 'https://xueqiu.com/service/v5/stock/screener/quote/list?page='
    url_media = '&size=90&order=desc&order_by=percent&exchange=CN&market=CN&'
    url_code = 'ind_code=' + code + '&_='
    stockList = []
    for i in range(1, count + 1):
        url = url_pre + str(i) + url_media + url_code + last_url
        # print('re_getStockList:', url)
        response = re.get(url=url, headers=headers)
        json_data = response.json()
        # pprint.pprint(json_data)
        # for j in range(0, 12):
        #     sheet.write()
        # 数据分析
        stocks = json_data['data']['list']
        for stock in stocks:
            data1 = stock['symbol']
            data2 = stock['name']
            data3 = stock['current']
            data4 = stock['chg']
            if data4:
                if float(data4) > 0:
                    data4 = '+' + str(data4)
                else:
                    data4 = str(data4)
            data5 = str(stock['percent']) + '%'
            data6 = str(stock['current_year_percent']) + '%'
            data7 = simplify(stock['volume'])
            data8 = simplify(stock['amount'])
            data9 = str(stock['turnover_rate']) + '%' if stock['turnover_rate'] else ''
            data10 = str(stock['pe_ttm']) if stock['pe_ttm'] else ''  # TTM
            data11 = stock['dividend_yield']
            if data11:
                data11 = str(data11) + '%'
            else:
                data11 = None
            data12 = simplify(stock['market_capital'])
            stockList.append([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12])
        if i % 10 == 0:
            print('前', i, '页数据爬取完成！')
    return stockList


def get_code(hq_url):
    driver = crawl.init(hq_url)
    basicSort = driver.find_element(By.XPATH, "//*[@id='center']/div/div[2]/div[1]/div[1]/div[2]/ul/li[3]/div")
    aList = basicSort.find_elements(By.TAG_NAME, 'a')
    codeList = []
    for a in aList:
        att = a.get_attribute('data-level2code')
        name = a.get_attribute('title')
        codeList.append([name, att])
    driver.close()
    return codeList


def simplify(n):
    if n:
        if n > 10000000:
            n = str(round(n / 10000000.0, 2)) + '亿'
        elif n > 10000:
            n = str(round(n / 10000.0, 2)) + '万'
        elif n > 1000:
            n = str(round(n / 1000.0, 2)) + '千'
        else:
            n = str(n) + '元'
    return n
