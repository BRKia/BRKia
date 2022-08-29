# coding=utf-8
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import crawl_init
import csv

information = []
ips = []
xpath = By.XPATH
cname = By.CLASS_NAME
driver = crawl_init.init('https://www.89ip.cn/')
count = 0
with open("ip.csv", "w", encoding="gbk", newline="") as f:
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f, dialect='excel', delimiter=',', quotechar='\"')
    while True:
        try:
            element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="layui-laypage-1"]/a[8]'))  # 直到出现
            )
            csv_writer.writerow(driver.find_element(cname, 'layui-table').find_element(By.TAG_NAME, 'tbody').text)
            element.click()
        finally:
            count += 1
            print(count, '次数据写入成功')
        if count > 100:
            break
f.close()

