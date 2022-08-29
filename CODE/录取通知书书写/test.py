import pandas as pd
from docxtpl import DocxTemplate, InlineImage
import docxtpl
import sys
from docx.shared import Mm


df = pd.read_excel('C:/Users/12267/Desktop/数据源.xlsx')
# print(df)

for i in range(len(df)):
    context = dict(df.iloc[i])
    # print(context)
    fileName = context['姓名']
    fileNum = context['编号']
    # 生成模板文件
    tpl = DocxTemplate('模板.docx')
    # 要插入的图片路径
    image_path = './file/' + str(fileNum) + '_' + fileName + '.png'
    # 创建图片对象
    insert_image = docxtpl.InlineImage(tpl, image_path, width=Mm(30), height=Mm(30))
    # context字典对象中添加项目, key为img
    context['img'] = insert_image
    # 渲染模板文件生成新文件
    tpl.render(context)

    tpl.save('./file/' + str(fileNum) + '_' + fileName + '.docx')
    print(str(fileNum) + '_' + fileName + '.docx')


