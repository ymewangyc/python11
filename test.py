# -*- coding: utf-8 -*-
from MysqlHelper import MysqlHelper

mh = MysqlHelper('10.100.1.142', 'test', '123456', 'testDB', 'utf8')
# mh = MysqlHelper('localhost', 'test', '123456', 'testDB', 'utf8')
sql = "select * from user where name=%s"
print(mh.find(sql, '小明'))
print(mh.find(sql, '张三'))


# mh = MysqlHelper('localhost', 'root', '123456', 'test', 'utf8')
# mh = MysqlHelper('10.100.1.142', 'test', '123456', 'testDB', 'utf8')
'''
# z添加数据
sql = "insert into user(name,password) values(%s,%s)"
mh.cud(sql, ('李四', '123456'))
mh.cud(sql, ('赵六', '123456'))
mh.cud(sql, ('哈哈哈', '123456'))
mh.cud(sql, ('顺丰', '123456'))
mh.cud(sql, ('132sd', '123456'))
mh.cud(sql, ('sdf5', '123456'))
'''

'''
# 删除数据
# delsql = "delete from user where NAME=%s "
delsql = "delete from user where id>%s "
mh.cud(delsql,('10'))
'''

# 更新数据
upsql = "update user set name=%s where name=%s "
mh.cud(upsql,('new132','132sd'))