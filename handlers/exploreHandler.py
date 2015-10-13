#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
from baseHandler import BaseHandler
from tornado import gen
sys.path.append("..")
from models.account_models import AutoUser


class ExploreHandler(BaseHandler):
	def get(self):
		self.render("explore/index.html")