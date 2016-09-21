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



class Captcha(BaseModel):
	"""docstring for Captcha"""
	

	__tablename__ = "captcha"


	session_id = Column(String(64), nullable = False)							# 链接
	value = Column(String(32), nullable = False)							# 链接
	add_time = Column(Integer, nullable = False)							# 添加时间
	status = Column(TINYINT, nullable = True, default = 0)			# 状态 0 未使用 1已使用



	@classmethod
	def queryById(cls, sessionId):
		session = DBSession()
		captcha = session.query(cls).filter(cls.session_id == session_id)
		return captcha



	@classmethod
	def add(cls, session_id, value):
		obj = cls(session_id = session_id, value = value, add_time = long(time.time()))
		session = DBSession()
		session.add(obj)
		session.commit()
		session.close()
		return True





