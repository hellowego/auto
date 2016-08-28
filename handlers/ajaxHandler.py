#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
from baseHandler import BaseHandler
from tornado import gen
import tornado.web
sys.path.append("..")
from models.account_models import AutoUser
from models.question_models import Question
from models.linkModel import Link
from util import Util

class VoteHandler(BaseHandler):
	"""docstring for VoteHandler"""
	@tornado.web.authenticated
	def post(self):
		id = self.get_argument("id")
		value = self.get_argument("value")
		print id, value
		user = self.get_current_user()
		Link.vote( id, user.uid, value)
		rsm = {'type_name':'answer'}
		self.write(Util.response(rsm, 1, None))