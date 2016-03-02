# -*-coding=utf8-*-
# your models module write here
import sys
from datetime import datetime
from users_models import Users
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
	def queryIsFollowed(cls, fansUid, friendUid):
		''' 查询是否关注 '''
		# 创建session对象:
		session = DBSession()
		count = session.query(cls).filter(cls.friend_uid==friendUid, cls.fans_uid==fansUid).count()
		return count

	@classmethod
	def countFollowing(cls, uid):
		''' 查询关注人数 '''
		# 创建session对象:
		session = DBSession()
		following = session.query(cls).filter(cls.fans_uid==uid).count()
		return following

	@classmethod
	def countFollower(cls, uid):
		''' 查询被关注人数 '''
		# 创建session对象:
		session = DBSession()
		follower = session.query(cls).filter(cls.friend_uid==uid).count()
		return follower
	

	@classmethod
	def follow(cls, fansUid, friendUid):
		''' 
		添加关注
		同时更新用户表的粉丝数和关注数
		'''
		ret = cls(fans_uid = fansUid, friend_uid = friendUid)
		session = DBSession()
		session.add(ret)
		session.commit()
		session.close()


		# 更新uid为fansUid的关注人数和粉丝数
		following = cls.countFollowing(fansUid)
		follower = cls.countFollower(fansUid)
		Users.updateFollowCount(fansUid, follower, following)

		# 更新uid为friendUid的关注人数和粉丝数
		following = cls.countFollowing(friendUid)
		follower = cls.countFollower(friendUid)
		Users.updateFollowCount(friendUid, follower, following)
		return True




	@classmethod
	def unfollow(cls, fansUid, friendUid):
		''' 取消关注 '''
		# 创建session对象:
		session = DBSession()
		ret = session.query(cls).filter(cls.friend_uid==friendUid, cls.fans_uid==fansUid).delete()
		session.commit()
		session.close()


		# 更新uid为fansUid的关注人数和粉丝数
		following = cls.countFollowing(fansUid)
		follower = cls.countFollower(fansUid)
		Users.updateFollowCount(fansUid, follower, following)

		# 更新uid为friendUid的关注人数和粉丝数
		following = cls.countFollowing(friendUid)
		follower = cls.countFollower(friendUid)
		Users.updateFollowCount(friendUid, follower, following)
		return True

	@classmethod
	def followingList(cls, uid):
		''' 获取用户关注名单，uid, url_token, '''
		# 创建session对象:
		session = DBSession()
		ret = session.query(Users.uid, Users.user_name, Users.url_token).filter(cls.fans_uid == uid, Users.uid == cls.friend_uid).all()		
		return ret
		
	@classmethod
	def followerList(cls, uid):
		''' 获取用户粉丝名单，uid, url_token, '''
		# 创建session对象:
		session = DBSession()
		ret = session.query(Users.uid, Users.user_name, Users.url_token).filter(cls.friend_uid == uid, Users.uid == cls.fans_uid).all()		
		return ret


if __name__ == "__main__":
	print 'hi'
	# User_follow.follow(1,2)
	# User_follow.follow(1,3)
	# User_follow.follow(2,3)

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
	
	# 查询是否关注
	count = User_follow.queryIsFollowed(1,4)
	print count
	for fan in fans:
		print fan.follow_id, fan.fans_uid
		
	# 获取用户关注名单，uid
	print u'获取用户关注名单，uid'
	ret = User_follow.followingList(1)
	for uid, url_token in ret:
		print uid, url_token
		
	# 获取用户关注名单，uid
	print u'获取用户粉丝名单，uid'
	ret = User_follow.followerList(11)
	for uid, url_token in ret:
		print uid, url_token

	print 'hello'


