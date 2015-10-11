# -*-coding=utf8-*-
# your models module write here
import sys
import bcrypt
import concurrent.futures
import torndb
import tornado.escape
from tornado import gen
sys.path.append("..")
from db.dbSession import BaseModel, DBSession
from sqlalchemy import Column, String, Integer

executor = concurrent.futures.ThreadPoolExecutor(2)

class AutoUser(BaseModel):
	"""
	user model
	"""
	__tablename__ = 'authors'

	id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String(64), nullable=False)
	hashed_password = Column(String(64), nullable=False)
	email = Column(String(64), nullable=False)

	@classmethod
	def queryUser(cls, username, password):
		# 创建session对象:
		session = DBSession()
		u = session.query(cls).filter(cls.name==username).first()

		if not u:
			return False

		hashed_password = bcrypt.hashpw(password, tornado.escape.utf8(u.hashed_password))

		if u.hashed_password == hashed_password:
			return u
		else:
			print 'wrong  password'
			return False

	@classmethod
	def checkUsername(cls, username):
		'''
		检查用户名是否已经被注册
		'''
		session = DBSession()
		u = session.query(cls).filter(cls.name==username).first()

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
		return bl
		


	@classmethod
	def addUser(cls, username, email, password):
		hashed_password = bcrypt.hashpw(tornado.escape.utf8(password), bcrypt.gensalt())
		print hashed_password
		ret = cls(name = username, email = email, hashed_password = hashed_password)
		session = DBSession()
		session.add(ret)
		session.commit()
		session.close()
		return True

if __name__ == "__main__":
	print 'hi'
	# u = AutoUser.queryUser("hello1", '1');
	# if u :
	# 	print u.name;
	# 	print u.hashed_password;
	# else:
	# 	print 'wrong username or password'
	# u = AutoUser.checkEmail("hellowego@gmail.com");
	u = AutoUser.addUser('hi', 'aa1@a.com', '1')
	if u:
		print 'register'
	else:
		print 'not register'


