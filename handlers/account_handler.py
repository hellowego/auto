#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
from baseHandler import BaseHandler
from tornado import gen
sys.path.append("..")
from models.account_models import AutoUser
from models.question_models import Question



class RegisterHandler(BaseHandler):
	def get(self):
		self.render("account/register.html")

	@gen.coroutine
	def post(self):
		username = self.get_argument("user_name")
		email = self.get_argument("email")
		password = self.get_argument("password")
		print username
		print email
		print password

		result = self.check( username, email, password)
		# result = {"errno" : -1, "err" : "用户名为空"}
		# rsm = {"url":"/home/first_login-TRUE"}
		rsm = {"url":"/"}
		result = {"rsm" : rsm, "errno" : 1, "err" : ""}
		bl = AutoUser.addUser(username, email, password)
		self.write(result)

	
	def check(self, username, email, password):
		# not null check
		if not username :
			result = {"errno" : -1, "err" : "用户名为空"}
			return result
		if not email :
			result = {"errno" : -1, "err" : "邮箱为空"}
			return result
		if not password :
			result = {"errno" : -1, "err" : "密码为空"}
			return result

		bl = AutoUser.checkUsername(username)
		if bl :
			result = {"errno" : -1, "err" : "用户名已被注册"}
			return result

		bl = self.validateEmail(email)

		if not bl:
			result = {"errno" : -1, "err" : "邮箱格式不正确"}
			return result

		bl = AutoUser.checkEmail(email)
		if bl :
			result = {"errno" : -1, "err" : "邮箱已被注册"}
			return result

		result = {"errno" : 1, "err" : "注册成功"}
		return result

		

	@classmethod
	def validateEmail(cls, email):
		if len(email) > 7:
			if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
				return True
		return False


class LoginHandler(BaseHandler):
	"""docstring for LoginHandler"""
	def get(self):
		self.render("account/login.html")

	def post(self):
		username = self.get_argument("user_name")
		password = self.get_argument("password")
		print username
		print password
		u = AutoUser.checkUserLogin(username, password)
		if u :
			print 'right'
			rsm = {"url":"/explore"}
			result = {"rsm" : rsm, "errno" : 1, "err" : ""}
			self.set_secure_cookie("current_user", str(u.id))
			print "current_user" ," ", str(u.id)

		else :
			print 'wrong'
			result = {"errno" : -1, "err" : "用户名或者密码错误"}

		self.write(result)

class LogoutHandler(BaseHandler):
	def get(self):
		self.clear_cookie("current_user")
		q = Question.queryAllQuestions()
		self.redirect("/explore")


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


class SettingHandler(BaseHandler):
	""" 账户设置 """

	def get(self):
		self.render("account/setting.html")

if __name__ == "__main__":
	print 'hi'
	# u = AutoUser.queryUser("hello1", '1');
	# if u :
	# 	print u.name;
	# 	print u.hashed_password;
	# else:
	# 	print 'wrong username or password'
	# u = AutoUser.checkEmail("hellowego@gmail.com");
	# if u:
	#	print 'register'
	#else:
	#	print 'not register'
	bl = RegisterHandler.check( 'hi', "hello@gmail.com", '111')
	print bl