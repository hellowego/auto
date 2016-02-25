# -*-coding=utf8-*-
# your models module write here
import sys
import bcrypt
import concurrent.futures
import torndb
import tornado.escape
from datetime import datetime
from tornado import gen
sys.path.append("..")
from db.dbSession import BaseModel, DBSession
from sqlalchemy import Column, String, Integer

from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

executor = concurrent.futures.ThreadPoolExecutor(2)

class Users(BaseModel):
	"""
	user model
	"""
	__tablename__ = 'users'

	uid = Column(Integer, primary_key=True, nullable=False)
	user_name = Column(String(255), nullable=False)
	email = Column(String(255), nullable=False)
	mobile = Column(String(16), nullable=True)
	password = Column(String(64), nullable=False)
	salt = Column(String(16), nullable=True)
	avatar_file = Column(String(128), nullable=True)
	sex = Column(TINYINT, nullable=True) 
	birthday = Column(Integer, nullable=True)  
	province = Column(String(64), nullable=True)
	city = Column(String(64), nullable=True)
	job_id = Column(Integer, nullable=True, default = 0) 
	reg_time = Column(DATETIME, nullable=True, default = datetime.now) 
	reg_ip = Column(BIGINT, nullable=False)
	last_login = Column(Integer, nullable=True, default = 0) 
	last_ip = Column(BIGINT, nullable=False)
	online_time = Column(Integer, nullable=True, default = 0) 
	last_active = Column(Integer, nullable=True, default = 0) 
	notification_unread = Column(Integer, nullable=True, default = 0) 
	inbox_unread = Column(Integer, nullable=True, default = 0) 
	inbox_recv = Column(TINYINT, nullable=True, default = 0) 	
	fans_count = Column(Integer, nullable=True, default = 0) 
	friend_count = Column(Integer, nullable=True, default = 0) 
	invite_count = Column(Integer, nullable=True, default = 0) 
	article_count = Column(Integer, nullable=True, default = 0) 
	question_count = Column(Integer, nullable=True, default = 0) 
	answer_count = Column(Integer, nullable=True, default = 0) 
	topic_focus_count = Column(Integer, nullable=True, default = 0) 
	invitation_available = Column(Integer, nullable=True, default = 0)	
	group_id = Column(Integer, nullable=True, default = 0) 
	reputation_group = Column(Integer, nullable=True, default = 0)	
	forbidden = Column(TINYINT, nullable=True, default = 0) 
	valid_email = Column(TINYINT, nullable=True, default = 0) 
	is_first_login = Column(TINYINT, nullable=True, default = 1) 	
	agree_count = Column(Integer, nullable=True, default = 0)
	thanks_count = Column(Integer, nullable=True, default = 0)
	views_count = Column(Integer, nullable=True, default = 0)
	reputation = Column(Integer, nullable=True, default = 0)
	reputation_update_time = Column(DATETIME, nullable=True, default = datetime.now)	
	weibo_visit = Column(TINYINT, nullable=True, default = 0) 	
	credit = Column(Integer, nullable=True, default = 0) 
	draft_count = Column(Integer, nullable=True, default = 0)
	common_email = Column(String(255), nullable=True)
	url_token = Column(String(32), nullable=True)
	url_token_update = Column(Integer, nullable=True, default = 0)
	verified = Column(String(32), nullable=True)	
	default_timezone = Column(String(32), nullable=True)
	email_settings = Column(String(255), nullable=True)
	weixin_settings = Column(String(255), nullable=True)	
	recent_topics = Column(TEXT, nullable=True) 
	

	@classmethod
	def queryUser(cls, username, password):
		# 创建session对象:
		session = DBSession()
		u = session.query(cls).filter(cls.user_name==username).first()

		if not u:
			return False

		hashed_password = bcrypt.hashpw(password, tornado.escape.utf8(u.hashed_password))

		if u.password == hashed_password:
			return u
		else:
			print 'wrong  password'
			return False

	@classmethod
	def queryAllUsers(cls):
		# 创建session对象:
		session = DBSession()
		u = session.query(cls).all()
		return u

	@classmethod
	def queryByUserId(cls, userid):
		session = DBSession()
		u = session.query(cls).filter(cls.uid==userid).first()
		if not u:
			return None
		else:
			return u

	@classmethod
	def queryByUsername(cls, username):
		""" 按用户名查询用户 """
		session = DBSession()
		u = session.query(cls).filter(cls.user_name==username).first()
		if not u:
			return None
		else:
			return u
			
	@classmethod
	def checkUsername(cls, username):
		'''
		检查用户名是否已经被注册
		'''
		session = DBSession()
		u = session.query(cls).filter(cls.user_name==username).first()

		if not u:
			return False
		else:
			return u

		print 'hi'

	@classmethod
	def checkEmail(cls, email):
		'''
		检查邮箱是否已经被注册
		'''
		session = DBSession()
		u = session.query(cls).filter(cls.email==email).first()

		if not u:
			return False
		else:
			return u

		print 'hi'

	@classmethod
	def checkPassword(cls, password, hashed_password_db):
		'''
		判断用户输入的密码是否正确
		'''
		hashed_password = bcrypt.hashpw(tornado.escape.utf8(password), tornado.escape.utf8(hashed_password_db))
		if hashed_password == hashed_password_db :
			return True
		else:
			return False


	@classmethod
	def checkUserLogin(cls, usernameOrEmail, password):
		'''
		用户登录时判断
		'''
		bl = False
		u = AutoUser.checkUsername(usernameOrEmail)
		if not u:
			u = AutoUser.checkEmail(usernameOrEmail)
			if not u:
				return False
		# print 'hi'	
		bl = AutoUser.checkPassword(password, u.hashed_password)
		return u
		


	@classmethod
	def addUser(cls, username, email, password):
		hashed_password = bcrypt.hashpw(tornado.escape.utf8(password), bcrypt.gensalt())
		print hashed_password
		ret = cls(user_name = username, email = email, password = hashed_password)
		session = DBSession()
		session.add(ret)
		session.commit()
		session.close()
		return True

	@classmethod
	def updateFollowCount(cls, uid, fans_count, friend_count):
		session = DBSession()
		session.query(cls).filter(cls.uid == uid).update({cls.fans_count:fans_count, cls.friend_count:friend_count})
		session.commit()
		session.close()

		

if __name__ == "__main__":
	print 'hi'
	# u = AutoUser.queryUser("hello1", '1');
	# if u :
	# 	print u.name;
	# 	print u.hashed_password;
	# else:
	# 	print 'wrong username or password'
	# u = AutoUser.checkEmail("hellowego@gmail.com");
	# u = Users.addUser('hi', 'aa1@a.com', '1')
	u = Users.addUser('hello', 'hellowego@gmail.com', '1')
	u = Users.queryByUserId(2)
	if u:
		print 'register'
	else:
		print 'not register'


