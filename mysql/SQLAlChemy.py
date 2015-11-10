#coding=utf-8
__author__ = 'jql'


# 导入:
from sqlalchemy import Column, String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    userid = Column(Integer,primary_key=True)
    username = Column(String(20))

# 初始化数据库连接:   '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqldb://root:123456@127.0.0.1:3306/own')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.userid=='5').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.username
# 关闭Session:
session.close()