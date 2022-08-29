import xlwt
import random

book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建一个文件，设置编码格式，且不压缩
sheet = book.add_sheet('个人信息', cell_overwrite_ok=True)  # 在文件中添加一个表
col = ('编号', '姓名', '语文', '数学', '英语')  # 写明列数据
for i in range(len(col)):
    sheet.write(0, i, col[i])  # 0行 i列， 写入col[i]
for i in range(1, 49):  # 48条数据
    sheet.write(i, 0, i)  # 编号
    # 导入名字
    name = ''
    for j in range(3):
        a = int(random.randint(20102, 40880))
        name += chr(a)
    sheet.write(i, 1, name)
    # 导入成绩
    for j in range(2, 5):
        sheet.write(i, j, int(random.randint(70, 150)))
savePath = 'C:/Users/12267/Desktop/数据源.xlsx'
book.save(savePath)


'''
import random


classes = []
for k in range(5):
    s = []
    for i in range(10):
        name = ''
        for j in range(3):
            a = int(random.randint(65, 90))
            name += chr(a)
        s.append(name)
    classes.append([k + 1, s])
print(classes)


'''