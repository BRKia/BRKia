import logging

# 日志的配置信息
LOG_LEVEL = logging.INFO
LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 默认时间格式
LOG_FILENAME = 'log.log'  # 默认日志名称
MAX_SCORE = 50
TEST_TIMEOUT = 10  # 测试代理IP的超时时间
MONGO_URLL = 'mongodb://127.0.0.1:27017'  # mongoDB数据库的URL