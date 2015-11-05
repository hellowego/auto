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

class Question(BaseModel):
    """
    user model
    """
    __tablename__ = 'question'


    question_id = Column(Integer, primary_key=True, nullable=False)
    question_content = Column(String(255), nullable=False)             #'问题内容'
    question_detail = Column(TEXT, nullable=False)              #'问题说明'
    add_time         = Column(Integer, nullable=False)                 #'添加时间'
    update_time = Column(Integer, nullable=False)      
    published_uid = Column(Integer, nullable=False)                #'发布用户UID'
    answer_count = Column(Integer, nullable=False)                 #'回答计数'
    answer_users = Column(Integer, nullable=False)                 #'回答人数'
    view_count = Column(Integer,  nullable=False)                  #'浏览次数'
    focus_count = Column(Integer,  nullable=False)                 #'关注数'
    comment_count = Column(Integer,  nullable=False)                #'评论数'
    action_history_id = Column(Integer,  nullable=True)            #'动作的记录表的关连id'
    category_id = Column(Integer,  nullable=False)                #'分类 ID'
    agree_count = Column(Integer,  nullable=False)                #'回复赞同数总和'
    against_count = Column(Integer, nullable=False)               #'回复反对数总和'
    best_answer = Column(Integer, nullable=False)                 #'最佳回复 ID'
    has_attach = Column(TINYINT, nullable=False)                  #'是否存在附件'  
    unverified_modify = Column(TEXT, nullable=True)
    unverified_modify_count         = Column(Integer, nullable=False)
    ip = Column(BIGINT, nullable=False)
    last_answer = Column(Integer, nullable=False)                       #'最后回答 ID'
    popular_value = Column(DOUBLE, nullable=False)    
    popular_value_update = Column(Integer, nullable=False)  
    lock = Column(TINYINT, nullable=False)                               #'是否锁定'
    anonymous = Column(TINYINT, nullable=False)    
    thanks_count = Column(Integer, nullable=False)      
    question_content_fulltext = Column(TEXT, nullable=False)
    is_recommend = Column(TINYINT, nullable=False)
    weibo_msg_id = Column(BIGINT, nullable=False)
    received_email_id = Column(Integer, nullable=False)  
    chapter_id         = Column(Integer, nullable=False)
    sort = Column(TINYINT, nullable=False)

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

