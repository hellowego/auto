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


class User_vote(BaseModel):
	"""
	User_vote model
	"""
	__tablename__ = "User_vote"

	
	user_id = Column(Integer, primary_key = True, nullable = False)								# 用户id
	link_id = Column(Integer, primary_key = True, nullable = False)			
	type = Column(Integer, nullable = True, default = 0)							#	
	add_time = Column(Integer, nullable = False)							# 添加时间
	
	
	
	@classmethod
	def queryByUserId(cls, userId):
		session = DBSession()
		userVotes = session.query(cls).filter(cls.user_id == userId).first()
		return userVotes

	@classmethod
	def queryByUserIdAndLinkId(cls, userId, linkid):
		session = DBSession()
		userVote = session.query(cls).filter(cls.user_id == userId, cls.link_id == linkid).first()
		if not userVote:
			return False
		else:
			print userVote
			return userVote
		


	@classmethod
	def add(cls, userid, linkid, type):
		obj = cls(user_id = userid, link_id = linkid, type = type, add_time = long(time.time()))
		session = DBSession()
		session.add(obj)
		session.commit()
		session.close()
		return True

	@classmethod
	def deleteByUserIdAndLinkId(cls, userId, linkid):
		session = DBSession()
		session.query(cls).filter(cls.user_id == userId, cls.link_id == linkid).delete()
		session.commit()
		return True
		
		


	@classmethod
	def updateByUserIdAndLinkId(cls, userId, linkid, type):
		session = DBSession()
		session.query(cls).filter(cls.user_id == userId, cls.link_id == linkid).update({cls.type: type})
		session.commit()
		return True


	



if __name__ == "__main__":
	# bl = User_vote.add(1,1,1)
	userVote = User_vote.queryByUserIdAndLinkId(2,19)
	print userVote.user_id
	






