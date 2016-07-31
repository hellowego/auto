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
	

	def get(self, randnum):
		msstream = BytesIO()
		captchaUtil = CaptchaUtil()
		code_img, randstr = captchaUtil.createCodeImage()
		self.set_secure_cookie("randstr", randstr)
		# print randstr
		# 验证码记录数据库
		self.set_secure_cookie("randstr", randstr)
		code_img.save(msstream,"jpeg")
		self.set_header('Content-Type', 'image/jpg')
		self.write(msstream.getvalue())

		# self.render("account/register.html")