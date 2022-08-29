import time

import Sample_course01.crawl_init as crawl
from selenium.webdriver.common.by import By

url = 'https://xueqiu.com/hq#exchange=CN&plate=1_3_2&firstName=1&secondName=1_3&type=sha&order=desc&order_by=amount'
driver = crawl.init(url)
ul = driver.find_element(By.XPATH, "//*[@id='pageList']/div/ul")
# ul.find_element(By.XPATH, '//*[@id="pageList"]/div/ul/li[9]/a').click()
# //*[@id="pageList"]/div/ul/li[2]/a
# //*[@id="pageList"]/div/ul/li[4]/a
# //*[@id="pageList"]/div/ul/li[5]/a
# //*[@id="pageList"]/div/ul/li[6]/a
for i in range(1, 56):
    xpath = "//*[@id='pageList']/div/ul/li[" + str(i) + "]/a"
    ul.find_element(By.XPATH, xpath).click()