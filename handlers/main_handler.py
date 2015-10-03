#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

from baseHandler import BaseHandler


class IndexHandler(BaseHandler):
	def get(self):
		welcome = "Hello,Torngas!"
		self.render("index.html", welcome=welcome)
