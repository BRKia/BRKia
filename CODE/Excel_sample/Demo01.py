import xlwt

book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建一个文件，设置编码格式，且不压缩
sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 在文件中添加一个表
col = ('电影详情链接', '图片链接', '影片中文名', '影片外国名', '评分', '评价数', '概况', '相关信息')  # 写明列数据
for i in range(0, 8):
    sheet.write(0, i, col[i])  # 0行 i列， 写入col[i]
datalist = [['www', 'www图片', '西游记', 'Journey to the West', '100分', '0人', '很好', '超级棒'],
            ['www2', 'www图片2', '西游记2', 'Journey to the West 2', '1000分', '1人', '很棒', '一级棒']]
for i in range(0, 2):  # 2组数据
    data = datalist[i]
    for j in range(0, 8):  # 每组数据有8列
        sheet.write(i + 1, j, data[j])
savePath = 'C:/Users/12267/Desktop/excel表格.xlsx'
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
