# -*-coding=utf8-*-
# your models module write here
import sys
sys.path.append("..")
from db.dbSession import BaseModel, DBSession
from sqlalchemy import Column, String, Integer

class AutoUser(BaseModel):
    """
    user model
    """
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)
    hashed_password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)



if __name__ == "__main__":
	# 创建session对象:
	session = DBSession()
	# 创建新User对象:
	new_user = AutoUser(id='6', name='Bob', hashed_password='ok', email = 'hi@hi.com')
	# 添加到session:
	session.add(new_user)
	# 提交即保存到数据库:
	session.commit()
	# 关闭session:
	session.close()

