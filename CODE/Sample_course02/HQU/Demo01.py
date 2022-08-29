from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from Sample_course01 import crawl_init

xpath = By.XPATH
driver = crawl_init.init("https://jwc.hqu.edu.cn/")
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/ul/li[1]/a').click()
print('打开新页面')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((xpath, '/html/body/div/div/div[2]/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[3]/span/input'))  # 直到出现搜索按钮才点击
    )
    print("找到搜索按钮")
    element.click()
    print("点击结束")
finally:
    # e1 = driver.find_element(By.TAG_NAME, "user_pwd")
    # e1.click()
    # e1.send_keys("20021231@202103638", Keys.ENTER)
    # driver.find_element(xpath, '//*[@id="user_id"]').send_keys('2134133001')
    driver.close()