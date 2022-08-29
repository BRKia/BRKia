from selenium import webdriver


def init(url):
    driver = webdriver.Edge(r'D:\编程\Python\Project\爬虫\msedgedriver.exe')
    driver.get(url)
    return driver
