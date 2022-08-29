import Sample_course01.crawl_init as crawl
from selenium.webdriver.common.by import By
import xlwt
import time

start = time.time()
# 创建表格
book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建一个文件，设置编码格式，且不压缩
sheet = book.add_sheet('股票行情', cell_overwrite_ok=True)  # 在文件中添加一个表

### 爬取数据
url = 'https://xueqiu.com/hq#exchange=CN&plate=1_3_2&firstName=1&secondName=1_3&type=sha&order=desc&order_by=amount'
driver = crawl.init(url)
table = driver.find_element(By.XPATH, "//*[@id='stockList']/div[1]/table")
####### 拿到起始行
thead = table.find_element(By.TAG_NAME, 'thead')
cols = thead.find_elements(By.CLASS_NAME, 'sortable')
for i in range(0, len(cols)):
    sheet.write(0, i, cols[i].text)  # 0行 i列
print('起始行输入完成')
####### 拿到数据
stockList = []

# 换页
ul = driver.find_element(By.XPATH, "//*[@id='pageList']/div/ul")
for i in range(2, 56):
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    trs = tbody.find_elements(By.TAG_NAME, 'tr')
    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, 'td')
        tdData = []  # 一条股票的数据
        for td in tds:
            if td.text != '关注':
                # print(td.text, end=' ')
                tdData.append(td.text)
        stockList.append(tdData)
    xpath = "//*[@id='pageList']/div/ul/li[" + str(i) + "]/a"
    ul.find_element(By.XPATH, xpath).click()
    print('第', (i - 1), '页数据爬取完成！')
print('全部数据爬取成功！')
# print(stockList)
for i in range(0, len(stockList)):  # n组数据
    data = stockList[i]
    for j in range(0, len(cols)):  # 每组数据有8列
        sheet.write(i + 1, j, data[j])
savePath = 'C:/Users/12267/Desktop/股票.xlsx'
book.save(savePath)
end = time.time()
driver.close()
print('数据导入成功！')
print('用时', round(end - start, 4), '秒')
