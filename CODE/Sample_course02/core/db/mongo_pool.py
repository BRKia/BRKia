from pymongo import MongoClient
from Sample_course02.settings import MONGO_URLL


class MongoPool(object):
    def __init__(self):
        self.client = MongoClient(MONGO_URLL)
        self.proxies = self.client['proxies_pool']['proxies']

    def __del__(self):
        # 关闭数据库的连接
        self.client.close()
