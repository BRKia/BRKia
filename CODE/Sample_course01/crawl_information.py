from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

option = webdriver.EdgeOptions()
option.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'  # 这里添加edge的启动文件=>chrome的话添加chrome.exe的绝对路径
driver = webdriver.Edge(r'D:\爬虫\msedgedriver.exe', options=option)  # 这里添加的是driver的绝对路径
driver.get("http://www.lagou.com/")
# 找到关闭弹窗
driver.find_element(by=By.XPATH, value='//*[@id="cboxClose"]').click()  # 点击搜索
time.sleep(1)
# 找到搜索输入框
driver.find_element(by=By.XPATH, value='//*[@id="search_input"]').send_keys('python', Keys.ENTER)
alist = driver.find_elements(by=By.CLASS_NAME, value='p-top__1F7CL')  # 拿到a标签
for a in alist:
    # a.find_element(By.TAG_NAME, 'h3').click()  # 找href点击
    a.find_element(By.TAG_NAME, 'a').click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[-1])  # 点击新建的子页面
    detail = driver.find_element(By.XPATH, '//*[@id="job_detail"]/dd[1]/p').text  # 找到子页面关于岗位的要求
    work_address = driver.find_element(By.XPATH, '//*[@id="job_detail"]/dd[3]/div[1]/a[1]').text
    print(work_address, ',职位诱惑：', detail)
    # 关闭窗口
    driver.close()
    driver.switch_to.window(driver.window_handles[0])  # 调回初始的总窗口
    time.sleep(5)


