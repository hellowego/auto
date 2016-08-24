#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import time

from baseHandler import BaseHandler
from tornado import gen
import tornado.web
sys.path.append("..")
from models.account_models import AutoUser
from models.question_models import Question
from models.linkModel import Link
from util import Util

class ExploreHandler(BaseHandler):	

	def get(self):
		# def get_time_format(poststamp):
		# 	return Util.get_time_format(poststamp)
		question = {'context': 123}
		# print question.context
		u = AutoUser.queryAllUsers()
		q = Question.queryAllQuestions()
		questions = {'hi','hello'}
		answer = 'hi'
		# 获取连接
		linkList = Link.queryAll()
		# 获取页数
		pageCount = Link.queryPageCount(10)
		pageNumList = [2,3,4,5,6]

		user = self.get_current_user()

		# get_time_format = Util.get_time_format;
		# nowStamp = int(time.time())
		# print get_time_format(nowStamp -186400)

		self.render("explore/index.html", linkList = linkList, pageNumList = pageNumList, get_time_format = Util.get_time_format, user = user)



	def post(self):
		# offset = self.get_argument("linksize")
		offset = 0
		print 'in explore post'
		# 获取连接
		linkList = Link.queryByPage(offset, 10)
		linkmodel = '''
			<li>
			    <div class="vote midcol unvoted ">
			        %s
			        <div class="score likes">17 </div>
			        <div class="score unvoted">16</div>
			        <div class="score dislikes">15 </div>
			        %s
			    </div>
			    <div class="cont">
			        <h3>[<a href="/news/category/5" class="category">搞笑系列</a>]<a href="%s" target="_blank">%s</a></h3>
			        <div class="info">
			            <span class="author">
							<a href="http://baidu.com">hello</a>&nbsp;发表于&nbsp;28天1小时前
							</span> &nbsp;&nbsp;
			            <span>1&nbsp;阅读</span>
			        </div>
			        
			    </div>
			</li>
			'''
		# 判读用户是否登录
		user = self.get_current_user()
		

		result = ""
		if linkList:
			for link in linkList:
				print '-----begin-------'
				print link.url
				print '-----end-------'
				if user :
					ajaxlogin = "ajaxlogin" 
					arrowup = "<i class=\"arrow up  \" onclick=\"AUTO.agree_vote(this, 'hi', %s);\"></i>" %(link.id)
					arrowdown = "<i class=\"arrow down  \" onclick=\"AUTO.agree_vote(this, 'hi', %s);\"></i>" %(link.id)
				else :
					ajaxlogin = " "
					arrowup = "<i class=\"arrow up  ajaxlogin\" ></i>"
					arrowdown = "<i class=\"arrow down  ajaxlogin\" ></i>"
				linkinfo = linkmodel % (arrowup, arrowdown, link.url, link.title)
				print linkinfo
				result = result + linkinfo
		print result

		self.write(result)
		










