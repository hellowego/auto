#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
from baseHandler import BaseHandler
from tornado import gen
sys.path.append("..")

from models.linkModel import Link
from models.catalogModel import Catalog

class SubmitHandler(BaseHandler):
	def get(self):
		catalogList = Catalog.queryAll()
		
		self.render("submit.html", catalogList = catalogList)


class SubmitLinkHandler(BaseHandler):
	def post(self):
		title = self.get_argument("titlex")
		sourceurl = self.get_argument("sourceurl")
		optionvalue = self.get_argument("catalogid")
		#  添加http:// 或者https:// 前缀
		if (sourceurl[0:7] == 'http://' or sourceurl[0:8] == 'https://'):
			pass
		else :
			sourceurl = 'http://' + sourceurl

		print title
		print optionvalue
		uid = 0
		bl = Link.add(uid, title, sourceurl)
		print bl
		self.redirect("/")

		