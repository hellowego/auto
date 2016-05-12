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

class Question(BaseModel):
    """
    user model
    """
    __tablename__ = 'question'


    question_id = Column(Integer, primary_key=True, nullable=False)
    question_content = Column(String(255), nullable=False)             #'问题内容'
    question_detail = Column(TEXT, nullable=False)              #'问题说明'
    add_time         = Column(Integer, nullable=True)                 #'添加时间'
    update_time = Column(Integer, nullable=True)      
    published_uid = Column(Integer, nullable=True)                #'发布用户UID'
    answer_count = Column(Integer, nullable=True, default = 0)                 #'回答计数'
    answer_users = Column(Integer, nullable=True, default = 0)                 #'回答人数'
    view_count = Column(Integer,  nullable=True, default = 0)                  #'浏览次数'
    focus_count = Column(Integer,  nullable=True, default = 0)                 #'关注数'
    comment_count = Column(Integer,  nullable=True, default = 0)                #'评论数'
    action_history_id = Column(Integer,  nullable=True, default = 0)            #'动作的记录表的关连id'
    category_id = Column(Integer,  nullable=True, default = 0)                #'分类 ID'
    agree_count = Column(Integer,  nullable=True, default = 0)                #'回复赞同数总和'
    against_count = Column(Integer, nullable=True, default = 0)               #'回复反对数总和'
    best_answer = Column(Integer, nullable=True, default = 0)                 #'最佳回复 ID'
    has_attach = Column(TINYINT, nullable=True, default = 0)                  #'是否存在附件'  
    unverified_modify = Column(TEXT, nullable=True)
    unverified_modify_count         = Column(Integer, nullable=True, default = 0)
    ip = Column(BIGINT, nullable=True, default = 0)
    last_answer = Column(Integer, nullable=True, default = 0)                       #'最后回答 ID'
    popular_value = Column(DOUBLE, nullable=True, default = 0)    
    popular_value_update = Column(Integer, nullable=True, default = 0)  
    lock = Column(TINYINT, nullable=True, default = 0)                               #'是否锁定'
    anonymous = Column(TINYINT, nullable=True, default = 0)    
    thanks_count = Column(Integer, nullable=True, default = 0)      
    question_content_fulltext = Column(TEXT, nullable=True)
    is_recommend = Column(TINYINT, nullable=True, default = 0)
    weibo_msg_id = Column(BIGINT, nullable=True)
    received_email_id = Column(Integer, nullable=True)  
    chapter_id         = Column(Integer, nullable=True)
    sort = Column(TINYINT, nullable=True, default = 0)

    @classmethod
    def queryAllQuestions(cls):
        session = DBSession()
        questions = session.query(cls)
        return questions


    @classmethod
    def queryById(cls, questionId):
        session = DBSession()
        question = session.query(cls).filter(cls.question_id == questionId).first()
        return question


    @classmethod
    def addQuestion(cls, question_content, question_detail, published_uid):
        obj = cls(question_content = question_content, question_detail = question_detail, 
            published_uid = published_uid, add_time = long(time.time()), update_time = long(time.time()))
        session = DBSession()
        session.add(obj)
        session.commit()
        session.close()
        return True




if __name__ == "__main__":
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    #new_user = AutoUser(id='6', name='Bob', hashed_password='ok', email = 'hi@hi.com')
    # 添加到session:
    #session.add(new_user)

    query = session.query(Question)
    for question in query:
        print question.question_content
        print question.question_detail
        print question.comment_count
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

