from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


def search():
    return input('请输入你想检索的内容')


search_text = search()
option = webdriver.EdgeOptions()
option.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'  # 这里添加edge的启动文件=>chrome的话添加chrome.exe的绝对路径
driver = webdriver.Edge(r'D:\爬虫\msedgedriver.exe', options=option)  # 这里添加的是driver的绝对路径
driver.get("https://w.hqu.edu.cn")
driver.find_element(By.XPATH, '//*[@id="qrCodeLoginA"]/span[2]').click()  # 打开今日校园扫码界面
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="rsList"]/div[2]/div/ul/li[4]/a/h3').click()  # 打开知网界面
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/input[2]').click()
# childs = driver.find_element(By.XPATH, '//*[@id="gridTable"]/table/tbody/tr[1]/td[2]/a')
# for child in childs:
#     print(child)



