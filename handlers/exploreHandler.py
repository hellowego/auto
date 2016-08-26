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
from models.User_vote import User_vote
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
		pageNum = int(self.get_argument("pageNum"))
		print 'pageNum: ', pageNum 
		pagesize = 5;
		offset = pageNum * pagesize
		# print 'in explore post'
		# 获取连接
		linkList = Link.queryByPage(offset, pagesize)
		# 总页数
		pageCount = Link.queryPageCount(pagesize)
		pageEnd = 0
		print '-----pageCount-------', pageCount
		# 判断是否为尾页
		if pageCount == pageNum + 1 :
			pageEnd = 1
			print '-----pageEnd-------'
		linkmodel = '''
			<li>
			    <div class="vote midcol unvoted ">
			        %s
			        <div class="score likes">%s </div>
			        <div class="score unvoted">%s</div>
			        <div class="score dislikes">%s </div>
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
		

		html = ""
		if linkList:
			for link in linkList:
				


				# 判断是否需要登录
				if user :
					# 判断是否投票
					userVote = User_vote.queryByUserIdAndLinkId(user.uid, link.id)
					if userVote:
						if userVote.type == 0 :
							arrowUpStatus = 'up'
							arrowDownStatus = 'downmod'
						else:
							arrowUpStatus = 'upmod'
							arrowDownStatus = 'down'
					ajaxlogin = "ajaxlogin" 
					arrowup = "<i class=\"arrow up  \" onclick=\"AUTO.agree_vote(this, 'hi', %s);\"></i>" %(link.id)
					arrowdown = "<i class=\"arrow down  \" onclick=\"AUTO.disAgree_vote(this, 'hi', %s);\"></i>" %(link.id)
				else :
					ajaxlogin = " "
					arrowup = "<i class=\"arrow up  ajaxlogin\" ></i>"
					arrowdown = "<i class=\"arrow down  ajaxlogin\" ></i>"
				linkinfo = linkmodel % (arrowup,link.likecount + 1, link.likecount , link.likecount - 1 , arrowdown, link.url, link.title)
				# print linkinfo
				html = html + linkinfo
		# print html
		result = {"html" : html, "pageEnd": pageEnd}
		# print result

		self.write(result)
		










