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
from models.answerVote_models import AnswerVote
from models.answer_vote_models import Answer_AnswerVote
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
		answers = Answer.queryByQuestionId(questionId)
		print answers[0].answer_content
		for answer in answers:
			print 'answer.answer_content', answer.answer_content
			vote = {'user':'hiihi'}
			print vote['user']
			answer.vote = vote
			print answer.vote['user']
			showmax = 5
			answer.showmax = 2

			# 获取投票人name
			votename = Answer_AnswerVote.queryByAnswerId(answer.answer_id)
			answer.votename = votename
			
			
			# 投赞同票人信息
			# agree_count = 
			
			
			
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

class AnswerVoteHandler(BaseHandler):
	'''
	回答投票
	'''
	def post(self):
		answer_id = self.get_argument("answer_id")
		print "answer_id", answer_id
		vote_value = self.get_argument("value")
		
		print "vote_value", vote_value
		answer_info = Answer.queryById(answer_id)
		userId = self.get_current_user_id()
		# 获取投票信息
		vote_info = AnswerVote.queryByAnswerIdAndUserId(answer_id, userId)
				
		# 赞同投票结果分三种情况
		# 情况一 没有投过票，增加一条投票记录
		if not vote_info :
			print 'vote_info', vote_info
			AnswerVote.addAnswerVote(answer_id, answer_info.uid, userId, vote_value)
		# 情况二 已经投过赞同票，则删除赞同记录（已经头赞同票，再点一次是为了取消赞同）
		else :
			print 'vote_info.vote_value', vote_info.vote_value
			if vote_info.vote_value == int(vote_value) :
				print 'already vote'				
				AnswerVote.deleteByVoterId(vote_info.voter_id)
		# 情况三 已经投反对票的，将反对票更新为赞同票
			if vote_info.vote_value != int(vote_value) :
				print 'against'
				AnswerVote.updateByVoterId(vote_info.voter_id, vote_value)
		
		# 统计总票数
		agree_count = AnswerVote.countByAnswerIdAndType(answer_id, 1)
		against_count = AnswerVote.countByAnswerIdAndType(answer_id, -1)
		
		# 更新answer投票数
		Answer.updateVoteByAnswerId(answer_id, vote_value, against_count, agree_count)
		print answer_info.uid
		print answer_info.answer_content
		

		


class AnswerQuestionHandler(BaseHandler):
	def post(self):
		answerContent = self.get_argument("answer_Content")
		questionId = 1
		userId = self.get_current_user_id()
		# userid is false need login 




	
		