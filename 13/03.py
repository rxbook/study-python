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

#一次插入多条记录
sqli = "insert into student values(%s,%s,%s,%s)"
cur.executemany(sqli,[
    ('11','zhang','aaaaa','1001'),
    ('12','wang','bbbbb','1002'),
    ('13','li','ccccc','1003'),
    ('14','zhao','ddddd','1004'),
])


cur.close()
conn.commit()
conn.close()
