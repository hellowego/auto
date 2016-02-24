# -*-coding=utf8-*-
# your models module write here
import sys
from datetime import datetime
sys.path.append("..")
from db.dbSession import BaseModel, DBSession
from sqlalchemy import Column, String, Integer

from sqlalchemy.dialects.mysql import \
		BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
		DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
		LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
		NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
		TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


class User_follow(BaseModel):
	"""
	user_follow model
	"""
	__tablename__ = 'user_follow'

	follow_id = Column(Integer, primary_key=True, nullable=False)
	fans_uid = Column(Integer, nullable=False) 
	friend_uid = Column(Integer, nullable=False) 
	add_time = Column(DATETIME, nullable=True, default = datetime.now) 
	

	@classmethod
	def queryByFansUid(cls, fansUid):
		# 创建session对象:
		session = DBSession()
		follows = session.query(cls).filter(cls.fans_uid==fansUid).all()
		return follows

		
	

	@classmethod
	def queryByFriendUidId(cls, friendUid):
		# 创建session对象:
		session = DBSession()
		fans = session.query(cls).filter(cls.friend_uid==friendUid).all()
		return fans

	

	@classmethod
	def addFans(cls, fansUid, friendUid):
		
		ret = cls(fans_uid = fansUid, friend_uid = friendUid)
		session = DBSession()
		session.add(ret)
		session.commit()
		session.close()
		return True

if __name__ == "__main__":
	print 'hi'
	User_follow.addFans(1,2)
	User_follow.addFans(1,3)
	User_follow.addFans(2,3)

	follows = User_follow.queryByFansUid(1)
	# 查询1关注了谁
	for follow in follows:
		print follow.follow_id, follow.friend_uid

	# 查询谁关注了3
	fans = User_follow.queryByFriendUidId(3)
	for fan in fans:
		print fan.follow_id, fan.fans_uid

	# 查询谁关注了1
	fans = User_follow.queryByFriendUidId(1)
	for fan in fans:
		print fan.follow_id, fan.fans_uid

	print 'hello'


