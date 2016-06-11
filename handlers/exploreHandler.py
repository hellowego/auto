#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
from baseHandler import BaseHandler
from tornado import gen
sys.path.append("..")
from models.account_models import AutoUser
from models.question_models import Question
from models.linkModel import Link


class ExploreHandler(BaseHandler):
	def get(self):
		question = {'context': 123}
		# print question.context
		u = AutoUser.queryAllUsers()
		q = Question.queryAllQuestions()
		questions = {'hi','hello'}
		answer = 'hi'
		# 获取连接
		linkList = Link.queryAll()
		# 获取页数
		pageCount = Link.queryPageCount(10)
		pageNumList = [2,3,4,5,6]

		self.render("explore/index.html", linkList = linkList, pageNumList = pageNumList)