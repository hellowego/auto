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


class AnswerComment(BaseModel):
	"""
	Answer model
	"""
	__tablename__ = "answer_comments"

	id = Column(Integer, primary_key = True, nullable = False)			# id 
	answer_id = Column(Integer, nullable = False)						# answer_id 
	uid = Column(Integer, nullable = False)								# 发布问题用户id
	message = Column(TEXT, nullable = False)							# 回答内容
	time = Column(Integer, nullable = False)							# 添加时间
	
	
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
	def addAnswerComment(cls, answer_id, uid, message):
		obj = cls(answer_id = answer_id, uid = uid, message = message)
		session = DBSession()
		session.add(obj)
		session.commit()
		session.close()
		return True



if __name__ == "__main__":
	bl = AnswerComment.addAnswerComment(1,2,'你好')
	print bl



