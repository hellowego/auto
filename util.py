#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
#

import logging
import logging.config
import os


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
		suid = uid.zfill(7)
		dir1 = suid[0:3]
		dir2 = suid[3:5]
		dir3 = suid[5:7]
		# 拼接路径
		path = 'static/uploads/avatar/' + dir1 + '/' + dir2 + '/' + dir3 + '_avatar_' + size + '.jpg'
		if os.path.exists(path):
			return path
		else:
			return 'common/avatar-' + size + '-img.png'
		
		
		
if __name__ == "__main__":

	test = 'get_avatar_url'
	if test == 'response':
		rsm = {"url":"/explore"}
		errno = 0
		err = 'succ'
		print Util.response(rsm, errno, err)
	
	if test == 'get_avatar_url':
		print Util.get_avatar_url('123456', "max")
		print Util.get_avatar_url('123456')
		
	# print os.getcwd()
	# print os.path.exists('static/uploads/1.txt')
		
