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
		obj = cls(answer_id = 1, answer_uid = 2, vote_uid = 3, add_time = long(time.time()), vote_value = 4, reputation_factor = 1)
		session = DBSession()
		session.add(obj)
		session.commit()
		session.close()
		return True



if __name__ == "__main__":
	bl = AnswerVote.addAnswerVote(1,2,3,4)
	print bl


