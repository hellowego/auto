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
from util import Util
import traceback


class ProfileHandler(BaseHandler):
	"""docstring for ProfileHandler"""


	def get(self, username):
		self.render("profile/index.html")
