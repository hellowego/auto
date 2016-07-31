#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
import time
from baseHandler import BaseHandler
from tornado import gen
import tornado.web
sys.path.append("..")
from models.account_models import AutoUser
from models.question_models import Question
from models.linkModel import Link
from util import Util

class ExploreHandler(BaseHandler):	

	def get(self):
		# def get_time_format(poststamp):
		# 	return Util.get_time_format(poststamp)
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

		user = self.get_current_user()

		# get_time_format = Util.get_time_format;
		# nowStamp = int(time.time())
		# print get_time_format(nowStamp -186400)

		self.render("explore/index.html", linkList = linkList, pageNumList = pageNumList, get_time_format = Util.get_time_format, user = user)