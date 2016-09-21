#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import logging
import logging.config
import os
import datetime
import time


class Util(object):
	'''
	工具函数
	'''
	
	@classmethod
	def response(cls, rsm, errno, err):
		return {'rsm':rsm, 'errno':errno, 'err':err}

	@classmethod
	def getLogger():
		logging.config.fileConfig("config/logger.config")
		logger = logging.getLogger("trace")

		return logger
		
	@classmethod
	def get_avatar_url(cls, uid, size = 'min'):
		# 1234567
		# suid = uid.zfill(7)
		suid = "%07d" % uid
		dir1 = suid[0:3]
		dir2 = suid[3:5]
		dir3 = suid[5:7]
		# 拼接图片的相对路径
		path = 'uploads/avatar/' + dir1 + '/' + dir2 + '/' + dir3 + '_avatar_' + size + '.jpg'
		# 文件的绝对路径
		filePath = os.getcwd() + "/static/" + path
		# 如果文件存在，返回相对路径，否则返回默认路径
		if os.path.exists(filePath):
			return path
		else:
			return 'common/avatar-' + size + '-img.png'
			# return 'uploads/avatar/000/00/02_avatar_min.jpg'


	@classmethod
	def get_time_format(cls, poststamp):
		# 现在的时间戳
		nowStamp = int(time.time())
		# 时间戳差值
		spanStamp = nowStamp - poststamp

		# 60秒之内
		if spanStamp < 60:
			return str(spanStamp) +  u'秒前'
		elif (spanStamp > 60 ) and (spanStamp <= 3600):
			return str(int(spanStamp/60)) + u'分钟前'
		elif (spanStamp > 3600) and (spanStamp < 86400):
			return str(int(spanStamp/3600)) + u'小时' + str(int(spanStamp/3600%60)) + u'分钟前'
		elif (spanStamp >= 86400 ):
			return str(int(spanStamp/86400)) + u'天' +  str(int(spanStamp%86400/3600)) + u'小时前'


		
		
		
if __name__ == "__main__":

	test = 'get_time_format'
	if test == 'response':
		rsm = {"url":"/explore"}
		errno = 0
		err = 'succ'
		print Util.response(rsm, errno, err)
	
	if test == 'get_avatar_url':
		print Util.get_avatar_url('123456', "max")
		print Util.get_avatar_url('123456')

	if test == 'get_time_format':
		nowStamp = int(time.time())
		print Util.get_time_format(nowStamp -10)
		print Util.get_time_format(nowStamp -70)
		print Util.get_time_format(nowStamp -3700)
		print Util.get_time_format(nowStamp -186400)
		print u'天'
		
	# print os.getcwd()
	# print os.path.exists('static/uploads/1.txt')
		
