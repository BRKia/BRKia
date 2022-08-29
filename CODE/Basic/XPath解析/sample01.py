from lxml import html

etree = html.etree
f = open('test.html', mode='r', encoding='utf-8')
pageSouce = f.read()
# print(pageSouce)
et = etree.HTML(pageSouce)
# print(et)
result = et.xpath("//nick[@class='joy']/text()")  # @href可拿到超链接 -> @后为属性值
print(result)
# result = html.etree.HTML(xml)
# print(result)



