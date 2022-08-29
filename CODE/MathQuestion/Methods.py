import random
import time

def Dict(s):
    if s == '计算题':
        return 0
    return 1

def Gao_fill(n, m):
    for i in range(1, n + 1):
        print('(', i, ')', end='    ')
        a = random.randint(0, 100)
        # 根据m的数，使个位数为m
        if 0 <= m < 10:
            b = 10 - a % 10 + 10 * random.randint(0, 9) + m
        else:
            b = random.randint(0, 100)
        print(a, '+', b, '= ( )', end=',     ')
        if a != 0 and b != 0 and a % b == 0:
            print(a, '/', b, '= ( )', end=',     ')
        a, b = random.randint(0, 10), random.randint(0, 10)
        print(a, 'x', b, '= ( )')


def Gap_fill(n):

    return n