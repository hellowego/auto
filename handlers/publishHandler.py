#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
import datetime
import time
import tornado.web
from baseHandler import BaseHandler
from tornado import gen
sys.path.append("..")
from util import Util
from models.question_models import Question



class PublishQuestionHandler(BaseHandler):
	"""docstring for PublishQuestionHandler"""
	def post(self):
		print 'PublishQuestionHandler'
		question_content = self.get_argument('question_content')
		question_detail = self.get_argument('question_detail')
		print question_detail
		print question_content
		user = self.get_current_user()
		userId = self.get_current_user_id()
		if len(question_content) < 5 :
			self.write(Util.response(None, -1, u'问题标题字数不得少于 5 个字'))
			return
		else :
			Question.addQuestion(question_content, question_detail, userId)

		url = '/'
		rsm = {'url':'/question/2'}
		self.write(Util.response(rsm, 1, None))
