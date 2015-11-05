#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
import tornado.web
from baseHandler import BaseHandler
from tornado import gen
sys.path.append("..")
from models.account_models import AutoUser
from models.question_models import Question

class QuestionModule(tornado.web.UIModule):
	def render(self, question):
		return self.render_string("modules/question.html", question=question)
		

class QuestionHandler(BaseHandler):
	def get(self, questionId):
		question = Question.queryById(questionId)
		self.render("question/question_detail.html", question=question)
