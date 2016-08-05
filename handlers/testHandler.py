#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
from baseHandler import BaseHandler
from tornado import gen
import uuid
sys.path.append("..")



class TestHandler(BaseHandler):
	def get(self):
		sessionId = str(uuid.uuid1())
		print sessionId

		self.set_session_id()
		self.render("test/mylogin.html")