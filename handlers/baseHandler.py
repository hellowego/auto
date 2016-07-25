#!/usr/bin/env python
#-*- coding: UTF-8 -*- 


import tornado.web
from models.account_models import AutoUser
from models.users_models import Users
import uuid

class BaseHandler(tornado.web.RequestHandler):
	"""
	do some your base things
	"""
	def get_current_user(self):
		user_id = self.get_secure_cookie("current_user")
		print "user_id ", user_id
		if not user_id: return None
		#return True
		# user = AutoUser.queryByUserId(user_id)
		user = Users.queryByUserId(user_id)
		print "user_name " , user.user_name
		return user
		
	def get_current_user_id(self):
		user_id = self.get_secure_cookie("current_user")
		print "user_id ", user_id
		if not user_id: 
			return None
		else:
			return user_id


	def get_session_id(self):
		session_id = self.get_secure_cookie("session_id")
		if not session_id:
			session_id = str(uuid.uuid1())
			self.set_secure_cookie("session_id", session_id)
			return session_id
		else:
			return session_id


	def set_session_id(self):
		self.get_session_id()
		