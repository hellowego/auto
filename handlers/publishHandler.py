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

class PublishQuestionHandler(BaseHandler):
	"""docstring for PublishQuestionHandler"""
	def post(self):
		print 'PublishQuestionHandler'
		url = '/'
		rsm = {'url':'/question/2'}
		self.write(Util.response(rsm, 1, None))
