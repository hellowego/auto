#!/usr/bin/env python
#-*- coding: UTF-8 -*- 


import tornado.web
from models.account_models import AutoUser

class BaseHandler(tornado.web.RequestHandler):
	"""
	do some your base things
	"""
	def get_current_user(self):
		user_id = self.get_secure_cookie("current_user")
		print "user_id ", user_id
		if not user_id: return None
		#return True
		user = AutoUser.queryByUserId(user_id)
		print "user_name " , user.name
		return user
		
	def get_current_user_id(self):
		user_id = self.get_secure_cookie("current_user")
		print "user_id ", user_id
		if not user_id: 
			return None
		else:
			return user_id