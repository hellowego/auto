#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

# your models module write here
from __future__ import division
import sys
import time
import datetime
import math

sys.path.append("..")
from db.dbSession import BaseModel, DBSession
from sqlalchemy import Column, String, Integer

from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


class Link(BaseModel):
	"""
	Link model
	"""
	__tablename__ = "Link"

	id = Column(Integer, primary_key = True, nullable = False)			# id 
	uid = Column(Integer, nullable = True, default = 0)								# 用户id
	title = Column(String(256), nullable = False)							# 标题
	url = Column(String(256), nullable = False)							# 链接
	likecount = Column(Integer, nullable = True, default = 0)								# 
	dislikecount = Column(Integer, nullable = True, default = 0)								# 
	add_time = Column(Integer, nullable = False)							# 添加时间
	readcount = Column(Integer, nullable = True, default = 0)
	
	
	@classmethod
	def queryById(cls, linkId):
		session = DBSession()
		answer = session.query(cls).filter(cls.id == linkId)
		return answer

	@classmethod
	def queryAll(cls):
		session = DBSession()
		linkList = session.query(cls).order_by(cls.add_time.desc())[:3]
		return linkList

	@classmethod
	def queryByPage(cls, offset, limit):
		session = DBSession()
		linkList = session.query(cls).order_by(cls.add_time.desc()).offset(offset).limit(limit)
		return linkList


	@classmethod
	def queryPageCount(cls, pageSize):
		session = DBSession()
		count = session.query(cls).count()
		# 向上取整，如：3.2  取整后为 4
		pageCount = int(math.ceil(count/int(pageSize)))
		return pageCount

	@classmethod
	def queryCount(cls):
		session = DBSession().count()
		count = session.query(cls)
		return count



	@classmethod
	def vote(cls, id, value):
		session = DBSession()
		if 'unvoted2like' == value:
			session.query(cls).filter(cls.id == id).update({cls.likecount:cls.likecount + 1})
		elif 'unvoted2dislike' == value:
			session.query(cls).filter(cls.id == id).update({cls.dislikecount:cls.dislikecount + 1})
		elif 'like2dislike' == value:
			session.query(cls).filter(cls.id == id).update({cls.likecount:cls.likecount - 1})
			session.query(cls).filter(cls.id == id).update({cls.dislikecount:cls.dislikecount + 1})
		elif 'dislike2like' == value:
			session.query(cls).filter(cls.id == id).update({cls.dislikecount:cls.dislikecount - 1})
			session.query(cls).filter(cls.id == id).update({cls.likecount:cls.likecount + 1})
		elif 'like2unvoted' == value:
			session.query(cls).filter(cls.id == id).update({cls.likecount:cls.likecount - 1})
		elif 'dislike2unvoted' == value:
			session.query(cls).filter(cls.id == id).update({cls.dislikecount:cls.dislikecount - 1})


		session.commit()
		session.close()
		return True


	

	@classmethod
	def add(cls, uid, title, url):
		obj = cls(uid = uid, title = title, url = url, add_time = long(time.time()))
		session = DBSession()
		session.add(obj)
		session.commit()
		session.close()
		return True



if __name__ == "__main__":
	bl = Link.add(1,'tilte','你好')
	print bl
	






