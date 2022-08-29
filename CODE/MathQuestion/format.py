from random import randint
import random


def get_expression():  # 算式的生成
    a = randint(0, 100)
    b = randint(0, 100)  # 随机生成1~100之间的整数
    sign = random.choice(['+', '-', 'x'])  # 随机进行＋，－, *运算
    if sign == '+':
        ans = a + b
    elif sign == 'x':
        if a * b > 100:
            a = int(a / 2)
            b = int(b / 2)
        ans = a * b
    else:
        ans = a - b
    if ans < 0 or ans > 100:  # 如果结果不在0-100之间 则重新生成a b
        get_expression()
    else:
        a = '{: <2d}'.format(a)
        b = '{: <3d}'.format(b)
        ans = '{: <3d}'.format(ans)
        # a,b,ans格式化，统一为2个宽度 使输出更整齐，美观
        # 存放 带没有（ex1）答案  和 有答案（ex2） 的算式
        ex1 = str(a) + str(sign) + str(b) + '='
        ex2 = str(a) + str(sign) + str(b) + '=' + str(ans)
        global expression
        expression = list()
        expression.append(ex1)
        expression.append(ex2)
    return expression  # 得到的两个算式以列表的形式返回


def save_expression(n):  # 得到指定数量的算式
    expression_Noans = list()  # 不带有答案
    expression_withans = list()  # 带有答案
    for i in range(0, n):  # 调用n次生成函数，得到n个满足条件的算式
        get_expression()
        expression_Noans.append(expression[0])
        expression_withans.append(expression[1])
    return [expression_Noans, expression_withans]  # 返回的expression_Noans,expression_withans列表中各有n个算式


def show_expression(n=int(eval(input('请输入出题数量:')))):  # 算式的输出和打印
    fp1 = open(r'C:\math.txt', 'a+')  # ’a+’表示如果没有这个文件则生成，有则在内容中继续填充
    fp2 = open(r'C:\key.txt', 'w+')
    if fp1.read != '':
        fp1.truncate(0)
        # print('fp1已清空')
    # if fp2.read() != '':
    #     fp2.truncate(0)
    #     print('fp2已清空')

    # expression_Noans=save_expression(n)[0]
    # expression_withans=save_expression(n)[1]
    # 如果这么写，就相当于重新调用了get_expression()函数，答案会不一致
    lis = save_expression(n)
    expression_Noans = lis[0]
    expression_withans = lis[1]
    show_number = 0  # 用于记录每行输出的题量 控制排版
    print(n, '道计算题:')  # 在频幕上输出
    print(n, '道计算题:', file=fp1)  # 打印至文本文档中
    for i in range(0, len(expression_Noans)):
        print(expression_Noans[i], end='     ')
        print(expression_Noans[i], end='     ', file=fp1)
        show_number += 1
        if show_number % 2 == 0:  # 每行输出两个题
            print('\n')  # 在频幕上输出
            print('\n', file=fp1)  # 打印至文本文档中
    show_number = 0  # 用于记录每行输出的题量 控制排版
    print()  # 换一行输出
    print(n, '道计算题(带答案):')  # 在频幕上输出
    print(n, '道计算题(带答案):', file=fp2)  # 打印至文本文档中
    for i in range(0, len(expression_withans)):
        print(expression_withans[i], end='      ')
        print(expression_withans[i], end='      ', file=fp2)
        show_number += 1
        if show_number % 2 == 0:
            print('\n')
            print('\n', file=fp2)


show_expression()


