import random
import time

from Methods import Gao_fill

# start = time.time()
# print('开始出题')
# Gao_fill(10, 1)  # 100000题，答案以1结尾
# end = time.time()
# print('出题结束,用时', int(end - start) / 60, '分钟')

# with open(r'D:\编程\Python\Project\爬虫\MathQuestion\应用题错题.txt', 'r', encoding='utf-8') as infile:
#     data2 = []
#     for line in infile:
#         data_line = line.strip("\n").split()  # 去除首尾换行符，并按空格划分
#         # print(data_line)
#         data2.append(data_line)
# print(data2)

print(10 * random.randint(1, 5))
