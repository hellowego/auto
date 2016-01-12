# -*-coding=utf8-*-
# your models module write here
import sys
import time
import datetime
sys.path.append("..")
from db.dbSession import BaseModel, DBSession 
from answerVote_models import AnswerVote
from account_models import AutoUser


class Answer_AnswerVote():
	"""
	Answer_AnswerVote model
	"""

	@classmethod
	def queryByAnswerId(cls, answerId, voteValue):
		session = DBSession()
		name = session.query(AutoUser.name).filter(AutoUser.id == AnswerVote.vote_uid, AnswerVote.answer_id == answerId, AnswerVote.vote_value == voteValue).distinct().all()
		namelist = []
		for str in name :
			namelist.append(str[0])
		return namelist

	

if __name__ == "__main__":
	name = Answer_AnswerVote.queryByAnswerId(30, '-1')
	print name
	# print name[0][0]
	# l = []
	# for x in name :
	# 	print x[0]
	# 	l.append(x[0])
	# print l


