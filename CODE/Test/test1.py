from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


# option = webdriver.EdgeOptions() option.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'  # 这里添加edge的启动文件=>chrome的话添加chrome.exe的绝对路径
# driver = webdriver.Edge(r'D:\编程\Python\Project\爬虫\msedgedriver.exe', options=option)  # 这里添加的是driver的绝对路径

s = Service(r'D:\编程\Python\Project\爬虫\msedgedriver.exe')
driver = webdriver.Edge(service=s)
driver.get("https://www.51test.net/show/10053782.html")

ulList = driver.find_elements(By.TAG_NAME, 'p')
for li in ulList:
    print(li.text)
