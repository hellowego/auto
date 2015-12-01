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


class Answer(BaseModel):
	"""
	Answer model
	"""
	__tablename__ = "Answer"

	answer_id = Column(Integer, primary_key = True, nullable = False)	# id 
	question_id = Column(Integer, nullable = False)						# 问题id
	answer_content = Column(TEXT, nullable = False)						# 回答内容
	add_time = Column(Integer, nullable = False)						# 添加时间
	against_count = Column(Integer, nullable = True, default = 0)		# 反对票数
	agree_count = Column(Integer, nullable = False, default = 0)		# 赞同票数
	uid = Column(Integer, nullable = False)								# 发布问题用户id
	comment_count = Column(Integer, nullable = True, default = 0)		# 评论总数
	uninterested_count = Column(Integer, nullable = True, default = 0)	# 感兴趣票数
	thanks_count = Column(Integer, nullable = True, default = 0)		# 感谢票数
	category_id = Column(Integer, nullable = True, default = 0)			# 分类id
	has_attach = Column(TINYINT, nullable = True, default = 0)			# 是否有附件
	ip = Column(BIGINT, nullable = True)								# ip
	force_fold = Column(TINYINT, nullable = True, default = 0)			# 是否折叠
	anonymous = Column(TINYINT, nullable = True, default = 0)			# 是否匿名
	publish_source = Column(String(16), nullable = True)				# 来源

	@classmethod
	def queryById(cls, answerId):
		session = DBSession()
		answer = session.query(cls).filter(cls.answer_id == answerId).first()
		return answer

	@classmethod
	def addAnswer(cls, questionId, answerContent, userId):
		obj = cls(question_id = questionId, answer_content = answerContent, uid = userId, add_time = long(time.time()))
		session = DBSession()
		session.add(obj)
		session.commit()
		session.close()
		return True



if __name__ == "__main__":
	questionId = 1
	answerContent = "hello"
	uid = 1
	Answer.addAnswer(questionId, answerContent, uid)

	answer = Answer.queryById(18)
	print answer.answer_content

	print time.ctime()

	now = long(time.time())
	print now
	str = datetime.datetime.utcfromtimestamp(now)
	print str
	strnow = str.strftime("%Y-%m-%d %H:%M:%S")
	print strnow


