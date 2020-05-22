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

############## [查询数据] ############## 
# 查询记录总数
aa = cur.execute("select * from student")
print aa

print '-----------------------'

#单条记录查询
print cur.fetchone()
print cur.fetchone()
print cur.fetchone()
cur.scroll(0,'absolute')
print cur.fetchone()

print '-----------------------'

#打印表中的所有数据
cur.scroll(0,'absolute')
info = cur.fetchmany(aa) #aa是记录总数
for i in info:
    print i





cur.close()
conn.commit()
conn.close()
