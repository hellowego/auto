#!/usr/bin/env python
#-*- coding: UTF-8 -*- 


import tornado.web
import sys
sys.path.append("..")
from util import Util

class AnswerModule(tornado.web.UIModule):
	def render(self, answer, user):
		return self.render_string("modules/answer.html", answer=answer, user=user)

		
		
class FollowListModule(tornado.web.UIModule):
	def render(self, uid, url_token, username):
		avatarUrl = Util.get_avatar_url(uid)
		return self.render_string("modules/followList.html", uid=uid, url_token=url_token, avatarUrl=avatarUrl, username=username)
		
		

class LinkModule(tornado.web.UIModule):
	def render(self, link, get_time_format):
		return self.render_string("modules/linkList.html", link = link, get_time_format = get_time_format)
		