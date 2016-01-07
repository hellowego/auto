# -*-coding=utf8-*-
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


class AnswerVote(BaseModel):
	"""
	Answer model
	"""
	__tablename__ = "answer_vote"

	voter_id = Column(Integer, primary_key = True, nullable = False)	# 自动ID
	answer_id = Column(Integer, nullable = False)						# 回复id 
	answer_uid = Column(Integer, nullable = True, default = '')			# 回复作者id
	vote_uid = Column(Integer, nullable = True, default = '')			# 投票者ID
	add_time = Column(Integer, nullable = False)						# 添加时间
	vote_value = Column(TINYINT, nullable = True, default = 1)			# -1反对 1 支持
	reputation_factor = Column(Integer, nullable = True, default = 1)	# 
	
	@classmethod
	def queryById(cls, answerId):
		session = DBSession()
		answer = session.query(cls).filter(cls.answer_id == answerId).first()
		return answer

	@classmethod
	def queryByQuestionId(cls, questionId):
		session = DBSession()
		answers = session.query(cls).filter(cls.question_id == questionId)
		return answers

	@classmethod
	def addAnswerVote(cls, answer_id, answer_uid, vote_uid, vote_value):
		obj = cls(answer_id = answer_id, answer_uid = answer_uid, vote_uid = vote_uid, add_time = long(time.time()), vote_value = vote_value, reputation_factor = 1)
		session = DBSession()
		session.add(obj)
		session.commit()
		session.close()
		return True

	@classmethod
	def queryByAnswerIdAndUserId(cls, answer_id, vote_uid):
		session = DBSession()
		vote_info = session.query(cls).filter(cls.answer_id == answer_id , cls.vote_uid == vote_uid).first()
		return vote_info

	@classmethod
	def deleteByVoterId(cls, voter_id):
		session = DBSession()
		session.query(cls).filter(cls.voter_id == voter_id).delete()
		session.commit()
		session.close()
		
	@classmethod
	def updateByVoterId(cls, voter_id, vote_value):
		session = DBSession()
		session.query(cls).filter(cls.voter_id == voter_id).update({cls.vote_value:vote_value})
		session.commit()
		session.close()
		
	@classmethod
	def countByAnswerIdAndType(cls, answer_id, vote_value):
		session = DBSession()
		count = session.query(cls).filter(cls.answer_id == answer_id, cls.vote_value == vote_value).count()		
		session.close()
		return count

if __name__ == "__main__":
	# bl = AnswerVote.addAnswerVote(1,2,3,4)	
	# print bl
	
	count = AnswerVote.countByAnswerIdAndType(30, 1)
	print count


