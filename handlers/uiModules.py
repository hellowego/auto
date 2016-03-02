#!/usr/bin/env python
#-*- coding: UTF-8 -*- 


import tornado.web

class AnswerModule(tornado.web.UIModule):
	def render(self, answer, user):
		return self.render_string("modules/answer.html", answer=answer, user=user)

		
		
class FollowListModule(tornado.web.UIModule):
	def render(self, uid, url_token):
		return self.render_string("modules/followList.html", uid=uid, url_token=url_token)
		
		