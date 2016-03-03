# -*-coding=utf8-*-
# your models module write here
import sys
sys.path.append("..")
from db.dbSession import BaseModel, DBSession
from sqlalchemy import Column, String, Integer

from sqlalchemy.dialects.mysql import \
		BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
		DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
		LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
		NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
		TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


class User_action_history_fresh(BaseModel):
	"""
	User_action_history_fresh model
	"""
	__tablename__ = 'User_action_history_fresh'

	history_id = Column(Integer, primary_key=True, nullable=False)
	uid = Column(Integer, nullable=True) 
	associate_type = Column(TINYINT, nullable=True, default = 0) 
	associate_action = Column(SMALLINT, nullable=True, default = 0) 
	associate_id = Column(TINYINT, nullable=True, default = 0) 
	add_time = Column(DATETIME, nullable=True, default = datetime.now) 
	associate_attached = Column(Integer, nullable=True, default = 0) 
	anonymous = Column(TINYINT, nullable=True, default = 0) 
	fold_status  = Column(TINYINT, nullable=True, default = 0) 
	

	@classmethod
	def queryByFansUid(cls, fansUid):
		# 创建session对象:
		session = DBSession()
		follows = session.query(cls).filter(cls.fans_uid==fansUid).all()
		return follows

		
	



if __name__ == "__main__":
	print 'hi'
	

	print 'hello'


_fresh