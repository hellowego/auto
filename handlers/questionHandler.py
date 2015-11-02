#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
import tornado.web
from baseHandler import BaseHandler
from tornado import gen
sys.path.append("..")
from models.account_models import AutoUser

class QuestionModule(tornado.web.UIModule):
	def render(self, question, answer):
		# question = 'hello'
		return self.render_string("modules/question.html", question=question, answer=answer)
		