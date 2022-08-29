from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import crawl_init


driver = crawl_init.init("https://i.51job.com/userset/user_discover.php?lang=c")
driver.find_element(By.XPATH, '//*[@id="NormalLoginBtn"]/span[3]/a').click()
driver.find_element(By.XPATH, '//*[@id="loginname"]').send_keys('13015883037')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('021231BRK')
driver.find_element(By.XPATH, '//*[@id="isread_em"]').click()
time.sleep(1)
driver.maximize_window()  # 全屏最大化
driver.find_element(By.XPATH, '//*[@id="login_btn_withPwd"]').click()  # 点击登录
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='topIndex']/div/p/a[2]"))  # 直到出现搜索按钮才点击
    )
    element.click()
finally:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="keywordInput"]'))  # 直到出现搜索按钮才点击
        )
        element.send_keys('Java', Keys.ENTER)
    finally:
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]"))
                # 直到出现工作地点按钮才继续
            )
            element.click()
        finally:
            ttags = driver.find_elements(By.CLASS_NAME, 'ttag')
            # print(ttags.text.index())
            for ttag in ttags:
                ttag.click()  # 删除所有城市，取全国
            driver.find_element(By.XPATH, '//*[@id="popop"]/div/div[3]/span').click()  # 点击确定
            time.sleep(10)
            try:
                element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "j_joblist")))
                element.find_element(By.CLASS_NAME, 'e').find_element(By.CLASS_NAME, 'e_icons ick').click()
            # for job in jobs:
            #     job.find_element
            #     break
            #     time.sleep(1)
            #     text = job.find_element(By.CLASS_NAME, 'sal').text()
            #     print(text)
            finally:
                print('end')
            #     # text = job.find_element(By.CLASS_NAME, 'el').find_element(By.By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[1]/a/p[2]').find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[1]/a/p[2]/span[1]')
            #     time.sleep(1)
            #     text = job.find_element(By.CLASS_NAME, 'sal').text
            #     print(text)
