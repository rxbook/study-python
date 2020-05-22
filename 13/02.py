#coding=utf-8
import MySQLdb


conn= MySQLdb.connect(
    host='localhost',
    port = 3306,
    user='root',
    passwd='',
    db ='rxpython',
)

cur = conn.cursor()

#插入一条数据
sqli = "insert into student values(%s,%s,%s,%s)"
cur.execute(sqli,('3','renxing','wwwwww','7'))

cur.close()
conn.commit()
conn.close()
