# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

 #SELECT DISTINCT CONCAT('User: ''',user,'''@''',host,''';') AS query FROM mysql.user;
 #show grants for 'TestLogin22'@'%';   
 ##delete from mysql.user where user=''; #新建用户需要登录，必须删除匿名用户，必须设置root密码

# change root password to yours:
conn = mysql.connector.connect(user='TestLogin', password='a123159147', database='test')
#conn = mysql.connector.connect(user='root', password='liaoyibiao1987', database='test')
cursor = conn.cursor()
# 创建user表:
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (name) values (%s)', ('Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()