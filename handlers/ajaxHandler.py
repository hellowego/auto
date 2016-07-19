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
from util import Util

class VoteHandler(BaseHandler):
	"""docstring for VoteHandler"""
	
	def post(self):
		id = self.get_argument("id")
		value = self.get_argument("value")
		print id, value
		Link.vote( id, value)
		rsm = {'type_name':'answer'}
		self.write(Util.response(rsm, 1, None))