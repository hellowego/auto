1. 查询所有数据，id 排序
session.query(User).order_by(User.id)

2. 查询所有数据，id 逆序排序
session.query(User).order_by(User.id.desc())

3. label 相当于Oracle里的别名
session.query(User.name.label('name_label')).all()

4. 表的别名 user_alias 等同于 User 方便同一个表使用join查询
user_alias = aliased(User, name='user_alias')
session.query(user_alias, user_alias.name).all()

5. 排序后取第二条和第三条记录， [:3] 前三条记录
session.query(User).order_by(User.id)[1:3]


6. 下面两个语句是一样的，filter_by 要一个= 不需要类名， filter 要两个等号，需要类名
session.query(User.name).filter_by(fullname='Ed Jones')
session.query(User.name).filter(User.fullname=='Ed Jones')

7. 相当于两个and条件查询
session.query(User).filter(User.name=='ed').filter(User.fullname=='Ed Jones')

8. 过滤器
query.filter(User.name == 'ed')   			-- equals
query.filter(User.name != 'ed')				-- not equals
query.filter(User.name.like('%ed%'))		-- like
query.filter(User.name.in_(['ed', 'wendy', 'jack']))   -- in

-- 子查询
query.filter(User.name.in_(
        session.query(User.name).filter(User.name.like('%ed%'))
))

-- not in
query.filter(~User.name.in_(['ed', 'wendy', 'jack']))

-- is null
query.filter(User.name == None)
query.filter(User.name.is_(None))


-- is not null
query.filter(User.name != None)
query.filter(User.name.isnot(None))

-- and 的三种写法
# use and_()
from sqlalchemy import and_
query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))

# or send multiple expressions to .filter()
query.filter(User.name == 'ed', User.fullname == 'Ed Jones')

# or chain multiple filter()/filter_by() calls
query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')

-- or 的用法
from sqlalchemy import or_
query.filter(or_(User.name == 'ed', User.name == 'wendy'))

-- match 不知道和Like什么区别
query.filter(User.name.match('wendy'))


9. 返回一个list
query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
query.all()

10.  返回第一个
query.first()


11. 查询到一条语句，如果返回多行则报错，没有找到数据也报错
user = query.one()
user = query.filter(User.id == 99).one()

-- one_or_none() he one() 区别： 如果没找到记录返回None, 如果找到多条记录也不会报错

-- scalar() 调用one() 返回这一行的第一列（还是行号待确认)



-- 返回行数
session.query(User).filter(User.name.like('%ed')).count()


12. 文本语句text函数
session.query(User).filter(text("id<224")).order_by(text("id")).all()


13. 绑定变量
session.query(User).filter(text("id<:value and name=:name")).params(value=224, name='fred').order_by(User.id).one()

14. sql语句
session.query(User).from_statement(text("SELECT * FROM users where name=:name")).params(name='ed').all()

15. 分组查询
from sqlalchemy import func
session.query(func.count(User.name), User.name).group_by(User.name).all()

16. 计数，下面语句执行效果一样
SELECT count(*) FROM table
session.query(func.count('*')).select_from(User).scalar()
session.query(func.count(User.id)).scalar()

17. 关联查询
session.query(User, Address).filter(User.id==Address.user_id).filter(Address.email_address=='jack@google.com').all()









