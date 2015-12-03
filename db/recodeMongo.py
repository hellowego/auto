# 查看数据库
show dbs

# 查看当前使用数据库
db

# 创建数据库
use dbname

# 删除数据库
db.dropDatabase()

# 查看collection
show collections

# 删除collection, 删除成功返回true, 失败为false
db.collectionName.drop()

# collection 插入
db.collectionName.insert({'name':'hi'})

# 更新 collection
db.collectionName.update({'name':'hello'})