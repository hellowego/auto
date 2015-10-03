#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
from baseHandler import BaseHandler
from tornado import gen
sys.path.append("..")
from models.account_models import AutoUser




class RegisterHandler(BaseHandler):
	def get(self):
		self.render("register.html")

	@gen.coroutine
	def post(self):
		user_name = self.get_argument("user_name")
		email = self.get_argument("email")
		password = self.get_argument("password")
		print user_name
		print email
		print password
		result = check(cls,user_name, email, password)
		result = {"errno" : -1, "err" : "用户名为空"}
		

		self.write(result)

	def check(cls, username, email, password):
		# not null check
		if not user_name :
			result = {"errno" : -1, "err" : "用户名为空"}
			return result
		if not email :
			result = {"errno" : -1, "err" : "邮箱为空"}
			return result
		if not password :
			result = {"errno" : -1, "err" : "密码为空"}
			return result

		bl = AutoUser.checkUsername(user_name)
		if bl :
			result = {"errno" : -1, "err" : "用户名已被注册"}
			return result

		bl = AutoUser.checkEmail(email)
		if bl :
			result = {"errno" : -1, "err" : "邮箱已被注册"}
			return result





class CheckUsernameHandler(BaseHandler):

	@gen.coroutine
	def post(self):
		user_name = self.get_argument("username")
		bl = AutoUser.checkUsername(user_name)

		if bl :
			result = {"errno" : -1, "err" : "用户名已被注册"}
		else :
			result = {"errno" : 1, "err" : ""}

		self.write(result)


class CheckEmailHandler(BaseHandler):

	@gen.coroutine
	def post(self):
		email = self.get_argument("email")
		bl = AutoUser.checkEmail(email)
		if bl :
			result = {"errno" : -1, "err" : "邮箱已被注册"}
		else :
			result = {"errno" : 1, "err" : ""}

		# return result

		self.write(result)    


if __name__ == "__main__":
	print 'hi'
	# u = AutoUser.queryUser("hello1", '1');
	# if u :
	# 	print u.name;
	# 	print u.hashed_password;
	# else:
	# 	print 'wrong username or password'
	u = AutoUser.checkEmail("hellowego@gmail.com");
	if u:
		print 'register'
	else:
		print 'not register'