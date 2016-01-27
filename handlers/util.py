#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

class Util(object):
	'''
	工具函数
	'''
	
	@classmethod
	def response(cls, rsm, errno, err):
		return {'rsm':rsm, 'errno':errno, 'err':err}

		
		
		
if __name__ == "__main__":

	rsm = {"url":"/explore"}
	errno = 0
	err = 'succ'
	print Util.response(rsm, errno, err)

