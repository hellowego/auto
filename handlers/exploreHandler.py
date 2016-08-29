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
from models.user_vote_model import User_vote
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
		
		# 判断是否为尾页
		if pageCount == pageNum + 1 :
			pageEnd = 1
			print '-----pageEnd-------'
		linkmodel = '''
			<li>
			    <div class="vote midcol %s ">
			        %s
			        <div class="score likes">%s </div>
			        <div class="score unvoted">%s</div>
			        <div class="score dislikes">%s </div>
			        %s
			    </div>
			    <div class="cont thing">
			        <p class="title">
			        	<a class="title" href="%s" target="_blank">%s</a>
			        	<span class="domain">
			        		(
			        			<a>%s</a>
			        		)
			        	</span>

			        </p>
			        <div class="info">
			            <span class="author">
							<a href="http://baidu.com">hello</a>&nbsp;发表于&nbsp;28天1小时前
							</span> &nbsp;&nbsp;
			            <span>1&nbsp;阅读</span>
			            <span>
			            	<a href="/comment/%s">回复</a>
			            </span>
			        </div>
			        
			    </div>
			</li>
			'''
		# 判读用户是否登录
		user = self.get_current_user()
		

		html = ""	
		
		if linkList:
			for link in linkList:
				# 初始化变量
				votestate = "unvoted"
				arrowUpStatus = 'up'
				arrowDownStatus = 'down'
				score = link.likecount - link.dislikecount
				# 判断是否需要登录
				if user :
					# 判断是否投票
					userVote = User_vote.queryByUserIdAndLinkId(user.uid, link.id)
					if userVote :	
						# print '------userVote------  ', 	userVote		
						if userVote.type == 0 :
							# print '------type------ 0 '
							arrowDownStatus = 'downmod'
							votestate = 'dislikes'
							score += 1
						else:
							arrowUpStatus = 'upmod'							
							votestate = 'likes'
							score -= 1
					ajaxlogin = "ajaxlogin" 
					arrowup = "<i class=\"arrow %s  \" onclick=\"AUTO.agree_vote(this, 'hi', %s);\"></i>" %(arrowUpStatus, link.id)
					arrowdown = "<i class=\"arrow %s  \" onclick=\"AUTO.disAgree_vote(this, 'hi', %s);\"></i>" %(arrowDownStatus, link.id)
				else :
					ajaxlogin = " "
					arrowup = "<i class=\"arrow up  ajaxlogin\" ></i>"
					arrowdown = "<i class=\"arrow down  ajaxlogin\" ></i>"
				linkinfo = linkmodel % (votestate, arrowup, score + 1, score , score - 1 , arrowdown, link.url, link.title, link.url, link.id)
				# print linkinfo
				html = html + linkinfo
		# print html
		result = {"html" : html, "pageEnd": pageEnd}
		# print result

		self.write(result)


class CommentHandler(BaseHandler):
	"""docstring for CommentHandler"""
	def get(self, linkId):
		print 'linkid', linkId

		link = Link.queryById(linkId)

		self.render("explore/comment.html", link = link, get_time_format = Util.get_time_format)
		# self.render("test/dropload.html")
		# self.render("account/register.html")
		
		










