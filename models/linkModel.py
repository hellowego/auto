#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

# your models module write here
import sys
import time
import datetime
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
	add_time = Column(Integer, nullable = False)							# 添加时间
	
	
	@classmethod
	def queryById(cls, linkId):
		session = DBSession()
		answer = session.query(cls).filter(cls.id == linkId)
		return answer

	@classmethod
	def queryAll(cls):
		session = DBSession()
		linkList = session.query(cls)
		return linkList

	

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
	






