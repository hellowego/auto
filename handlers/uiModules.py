#!/usr/bin/env python
#-*- coding: UTF-8 -*- 


import tornado.web

class AnswerModule(tornado.web.UIModule):
	def render(self, answer):
		return self.render_string("modules/answer.html", answer=answer)
