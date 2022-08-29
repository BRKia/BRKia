from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

list = ["河北", "山西", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "海南", "四川", "贵州",
        "云南", "陕西", "甘肃", "青海", "台湾", "内蒙古", "广西", "西藏", "宁夏", "新疆", "北京", "天津", "上海", "重庆", "香港", "澳门"]
option = webdriver.EdgeOptions()
option.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'  # 这里添加edge的启动文件=>chrome的话添加chrome.exe的绝对路径
driver = webdriver.Edge(r'D:\爬虫\msedgedriver.exe', options=option)  # 这里添加的是driver的绝对路径
driver.get("https://www.baidu.com/")

for city in list:
    driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys(city + '疫情实时数据', Keys.ENTER)
    time.sleep(1)
    if city == '香港' or city == '台湾' or city == '澳门':
        person = driver.find_element(By.XPATH, '//*[@id="1"]/div/div[2]/a/div[2]/div[3]/div[2]').text
    else:
        person = driver.find_element(By.XPATH, '//*[@id="1"]/div/div[2]/a/div[2]/div[6]/div[2]').text
    print(city, '确诊人数：', person)
    driver.find_element(By.XPATH, '//*[@id="kw"]').clear()
    time.sleep(5)
