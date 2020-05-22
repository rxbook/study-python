#coding=utf-8
import MySQLdb

#Connect() 方法用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息。
#这只是连接到了数据库，要想操作数据库需要创建游标。
conn= MySQLdb.connect(
    host='localhost',
    port = 3306,
    user='root',
    passwd='',
    db ='rxpython',
)

#通过获取到的数据库连接conn下的cursor()方法来创建游标。
#通过游标cur 操作execute()方法可以写入纯sql语句。
#通过execute()方法中写如sql语句来对数据进行操作。
cur = conn.cursor()

#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

#cur.close() 关闭游标
cur.close()
#conn.commit()方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入。
conn.commit()
#Conn.close()关闭数据库连接
conn.close()
