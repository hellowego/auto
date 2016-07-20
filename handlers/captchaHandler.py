#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
import re
from baseHandler import BaseHandler
from io import BytesIO
sys.path.append("..")
from utils.captchaUtil import CaptchaUtil




class CaptchaHandler(BaseHandler):
	"""docstring for VerifyCodeHandler"""
	

	def get(self):
		msstream = BytesIO()
		captchaUtil = CaptchaUtil()
		code_img = captchaUtil.createCodeImage()
		code_img.save(msstream,"jpeg")
		self.set_header('Content-Type', 'image/jpg')
		self.write(msstream.getvalue())

		# self.render("account/register.html")