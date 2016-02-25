#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import datetime
import time
import tornado.web
from baseHandler import BaseHandler
from tornado import gen
sys.path.append("..")
from models.account_models import AutoUser
from models.question_models import Question
from models.answer_models import Answer
from models.answerVote_models import AnswerVote
from models.answer_vote_models import Answer_AnswerVote
from models.answerComment_models import AnswerComment
from models.users_models import Users
from models.userFollow_models import User_follow
from util import Util
import traceback


class ProfileHandler(BaseHandler):
	"""docstring for ProfileHandler"""


	def get(self, username):
		# 当前的用户id
		uid = int(self.get_current_user_id())
		# 要访问的用户主页
		user = Users.queryByUsername(username)
		
		# 判读是否已经关注
		isfollowed = User_follow.queryIsFollowed(uid, user.uid)
		if not user :
			self.render("global/show_message.html", user = user)
		else :
			print user.user_name
			print uid, user.uid
			# uid = None
			self.render("profile/index.html", user = user, uid = uid, isfollowed = isfollowed)


class FollowPeopleHandler(BaseHandler):
	"""
	关注按钮
	"""
	def post(self):
		rsm = {'type':'add'}
		print 'follow'
		# self.write(Util.response(None, -1, u'回复不存在'))
		self.write(Util.response(rsm, 1, None))


