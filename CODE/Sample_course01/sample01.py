from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt


def crawl_data(href):
    option = webdriver.EdgeOptions()
    option.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'  # 这里添加edge的启动文件=>chrome的话添加chrome.exe的绝对路径
    driver = webdriver.Edge(r'D:\爬虫\msedgedriver.exe', options=option)  # 这里添加的是driver的绝对路径
    driver.get(href)
    driver.find_element(By.XPATH, '//*[@id="link173"]').click()
    text = driver.find_element(By.XPATH, '//*[@id="tablelist"]').text
    text = text.split('\n', 2)[-1]
    with open("file.csv", "w", encoding="utf-8") as f:  # 2. 基于文件对象构建 csv写入对象
        f.write(text)
        print("写入数据成功")  # 5. 关闭文件
        f.close()


if __name__ == '__main__':
    # crawl_data("https://datachart.500.com/ssq/history/history.shtml")
    data = pd.read_csv('file.csv', header=None, index_col=0)
    red_ball = data.loc[:, 1:6]
    blue_ball = data.loc[:, 7]
    red_ball_count = pd.value_counts(red_ball.values.flatten())
    blue_ball_count = pd.value_counts(blue_ball)
    plt.pie(red_ball_count,labels=red_ball_count.index, radius=1, wedgeprops={'width': 0.3})
    plt.pie(blue_ball_count, labels=blue_ball_count.index, radius=0.5, wedgeprops={'width': 0.2})
    plt.show()
