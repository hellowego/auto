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
	def queryByAnswerId(cls, answerId):
		session = DBSession()
		answer = session.query(cls).filter(cls.answer_id == answerId)
		return answer

	

	@classmethod
	def addAnswerComment(cls, answer_id, uid, message):
		obj = cls(answer_id = answer_id, uid = uid, message = message, time = long(time.time()))
		session = DBSession()
		session.add(obj)
		session.commit()
		session.close()
		return True



if __name__ == "__main__":
	# bl = AnswerComment.addAnswerComment(1,2,'你好')
	# print bl
	answerComments = AnswerComment.queryByAnswerId(30)
	ss = 'hi %s'
	commentModel = u'''
			<ul>
				<li>
					<a class="aw-user-name" href="http://wenda.wecenter.com/people/seosns" data-id="8884"><img src="http://wenda.wecenter.com/uploads/avatar/000/00/88/84_avatar_min.jpg" alt="" /></a>
				
					<div>
						<p class="clearfix">
						
										<span class="pull-right">
													<a href="javascript:;" onclick="if ($(this).parents('.aw-comment-box').find('form textarea').val() == $(this).parents('.aw-comment-box').find('form textarea').attr('placeholder')){$(this).parents('.aw-comment-box').find('form textarea').val('');};$(this).parents('.aw-comment-box').find('form').show().find('textarea').focus();$(this).parents('.aw-comment-box').find('form textarea').insertAtCaret('@seosns:');$.scrollTo($(this).parents('.aw-comment-box').find('form'), 300, {queue:true});$(this).parents('.aw-comment-box').find('textarea').focus();">回复</a>				</span>
									
						<a href="http://wenda.wecenter.com/people/seosns" class="aw-user-name author" data-id="8884">seosns</a> • <span>2015-04-17 21:45</span>
						</p>
						<p class="clearfix">%s</p>
					</div>
				</li>
			</ul>
			'''
	for answerComment in answerComments :
		print answerComment.message
		s = commentModel %(answerComment.message)

		print s



