import pymysql
import csv
import cryptography

host = 'localhost'
port = 3306
user = 'root'
password = '123456'
db = 'brk'
charset = 'utf8'
conn = pymysql.Connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
print('连接成功！')
try:
    cursor = conn.cursor()
    sql = 'select * from emp'
    cursor.execute(sql)
    result = cursor.fetchall()
    with open("file.csv", "w", encoding="utf-8", newline="") as f:  # 打开一个csv文件，准备将数据库查询得到的文件导入。w表示只写入数据
        csv_writer = csv.writer(f)
        for data in result:
            csv_writer.writerow(data)
except Exception:
    print('查询失败！')
conn.close()
f.close()
print('数据导入成功!')
