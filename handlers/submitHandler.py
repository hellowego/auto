#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
from baseHandler import BaseHandler
from tornado import gen
sys.path.append("..")

from models.linkModel import Link

class SubmitHandler(BaseHandler):
	def get(self):
		
		
		self.render("submit.html")


class SubmitLinkHandler(BaseHandler):
	def post(self):
		title = self.get_argument("titlex")
		sourceurl = self.get_argument("sourceurl")
		print title
		print sourceurl
		uid = 0
		bl = Link.add(uid, title, sourceurl)
		print bl
		self.redirect("/")

		