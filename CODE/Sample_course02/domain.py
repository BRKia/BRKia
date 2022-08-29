from Sample_course02.settings import MAX_SCORE


# 封装ip
class Proxy(object):

    def __init__(self, ip, port, protocol=-1, nick_type=-1, speed=-1, area=None, score=MAX_SCORE, disable_domain=[]):
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.nick_type = nick_type
        self.speed = speed
        self.area = area
        self.score = score
        self.disable_domain = disable_domain

    def __str__(self):
        return str(self.__dict__)  # 返回数据字符串
