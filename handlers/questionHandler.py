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
from models.answer_models import Answer
import traceback
class QuestionModule(tornado.web.UIModule):
	def render(self, question):
		return self.render_string("modules/question.html", question=question)
		


class QuestionHandler(BaseHandler):
	'''
	具体的一个问题页面
	'''
	def get(self, questionId):
		question = Question.queryById(questionId)
		answers = ''
		self.render("question/question_detail.html", question=question, questionId=questionId, answers=answers)


class AnswerAddHandler(BaseHandler):
	'''
	问题回复
	'''
	def post(self):
		# try:
			# print 'begin'
			# answerContent = self.get_argument("answer_content")
			# print 'end'
		# except :
			# print traceback.print_exc()
			# print 'error'
		# print 'hi'	
		
		answerContent = self.get_argument("answer_content")
		questionId = self.get_argument("question_id")
		print 'answerContent:', answerContent
		# questionId = 1
		userId = self.get_current_user_id()
		print 'userId' , userId
		# user = self.get_current_user()
		Answer.addAnswer(questionId, answerContent, userId)
		
		result = {"errno" : 1, "err" : ""}
		self.write(result)




class AnswerQuestionHandler(BaseHandler):
	def post(self):
		answerContent = self.get_argument("answer_Content")
		questionId = 1
		userId = self.get_current_user_id()
		# userid is false need login 




	
		