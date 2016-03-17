# 启动数据库
E:\mongodb-win32-x86_64-3.0.7\bin>mongod -dbpath  ../db

#连接数据库
E:\mongodb-win32-x86_64-3.0.7\bin>mongo.exe

# 查看数据库
show dbs

# 查看当前使用数据库
db

# 查询集合
db.th_trade_right.find()

# 创建数据库
use dbname

# 删除数据库
db.dropDatabase()

# 查看collection
show collections

# 删除collection, 删除成功返回true, 失败为false
db.name.drop()

# collection 插入
db.name.insert({'name':'hi','age':20})
db.name.insert({'name':'hi','age':21})
db.name.insert({'name':'hi','age':22})
db.name.insert({'name':'tom','age':18})
db.name.insert({'name':'jack','age':22})

db.name.insert({'name':'hi','age':20},{'name':'hi','age':21},{'name':'hi','age':22})

# 更新 collection
db.name.update({"name":"hi"},{"$set":{"age":25}})

# 按条件删除
db.name.remove({"name":"hi"})
# 按条件只删除第一条
db.name.remove({"name":"hi"}, ture)
# 多个条件删除
db.name.remove({"name":"hi", "age":20})

# like 查询
db.name.find({"name":/^ja/})
db.name.find({"name":/^h/, "age":21})


# 按时间排序desc
db.moverecord.find().sort({movedate:-1})

# MongoDB提供了一组比较操作符：$lt $lte $gt $gte $ne，依次等价于< <= > >= !=。

#下面的示例返回符合条件age >= 18 && age <= 40的文档。
db.name.find({"age":{"$gte":18, "$lte":40}}).toArray()

#下面的示例返回条件符合name != "tom"
db.name.find({"name":{"$ne":"tom"}})

#$in等同于SQL中的in，下面的示例等同于SQL中的in ("tom","jack")
db.name.find({"name":{"$in":["tom","jack"]}})

#$nin等同于SQL中的not in，同时也是$in的取反。如：
db.name.find({"name":{"$nin":["tom","jack"]}})


#$or等同于SQL中的or，$or所针对的条件被放到一个数组中，每个数组元素表示or的一个条件。
#下面的示例等同于name = "tom" or age = 35
db.name.find({"$or": [{"name":"tom"}, {"age":22}]})

#下面的示例演示了如何混合使用$or和$in。
db.name.find({"$or": [{"name":{"$in":["tom","jack"]}}, {"age":22}]})

# $not表示取反，等同于SQL中的not。
db.name.find({"name": {"$not": {"$in":["tom","jack"]}}})

#
db.th_trade_right