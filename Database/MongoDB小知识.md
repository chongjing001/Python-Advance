### 创建数据库
- 创建
```
use 数据库名 : 如果数据库不存在，则创建数据库，否则切换到指定的数据库
```
```
>use test
switched to db test
>db
test
```
- 查看所有数据库
```
>show dbs; 或 show databases;
admin   0.000GB
config  0.000GB
local   0.000GB
```
**可以发现刚创建的test不在数据库列表中，要显示它，需要插入数据**
```
>db.test.insert({"name":"张三"})
WriteResult({ "nInserted" : 1 })
>show dbs;
admin   0.000GB
config  0.000GB
local   0.000GB
test    0.000GB
```
**MongoDB 中默认的数据库为 test，如果你没有创建新的数据库，集合将存放在 test 数据库中**
- 删除数据库
删除当前数据库，默认为test，db查看当前的数据库名
```
db.dropDatabase()
```
流程：
```
# 查看所有数据库
>show dbs;
# 切换数据库
>use test;
# 删除
>db.dropDatabase()
{ "dropped" : "runoob", "ok" : 1 }
```
***
#### 集合
- createCollection()
```
db.createCollection(name, options)
```
参数说明：
- name：要创建的集合名称
- options：可选参数，指定有关内存大小及索引的选项
options 可以是如下参数：
capped：布尔  如果为 true，则创建固定集合。固定集合是指有着固定大小的集合，当达到最大值时，它会自动覆盖最早的文档。当该值为 true 时，必须指定 size 参数。
autoindexld：布尔  如为 true，自动在 _id 字段创建索引。默认为 false。
size：数值  为固定集合指定一个最大值（以字节计）。如果 capped 为 true，也需要指定该字段。
max：数字  指定固定集合中包含文档的最大数量。
**在检查文档时，MongoDB 首先检查固定集合的 size 字段，然后检查 max 字段**
```
>use test
switched to db test
>db.createCollections("user")
{ "ok" : 1 }
# 查看已有集合
>show collections  或者 show tables
```
**在 MongoDB 中，你不需要创建集合。当你插入一些文档时，MongoDB 会自动创建集合**
```
>db.user1.insert({"name":"李四"})
```
***
- 删除
```
db.collection.drop()   collection:集合名
```
***
- 插入数据
db.集合名.insert(数据)
```
>db.user.insert({name:"王五",
               age:26,
               gender:'男'
               tags:['a','b','c']
               })
# 或者
>document = ({name:"王五",
               age:26,
               gender:'男'
               tags:['a','b','c']
               })
>db.user.insert(document)
WriteResult({ "nInserted" : 1 })
```
***
- 更新(update())

query : update的查询条件，类似sql update查询内where后面的。
update : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的
upsert : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。
multi : 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。
writeConcern :可选，抛出异常的级别。
```
# 通过update()更新name
>db.user.update({"name":"李四"},{$set:{"name":"你猜"}})
```
**以上语句只会修改第一条发现的文档，如果你要修改多条相同的文档，则需要设置 multi 参数为 true**

- 删除数据
```
db.集合名.remove({可指定数据，不指定则删除全部})
>db.user.remove({"name":"李四"})
# 删除全部
>db.user.remove({})
```
- 查询
db.集合名.find(query, projection)
参数：
- query ：可选，使用查询操作符指定查询条件
- projection ：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）
pretty() 格式化显示所有文档
```
>db.user.find().pretty()
```
**MongoDB 的 find() 方法可以传入多个键(key)，每个键(key)以逗号隔开，即常规 SQL 的 and 条件**
```
>db.col.find({key1:value1, key2:value2}).pretty()
```
#### 条件操作符
(>) 大于 - $gt
(<) 小于 - $lt
(>=) 大于等于 - $gte
(<= ) 小于等于 - $lte
```
db.user.find({age:{$gt:20}})  
类似sql语句：Select * from user where age > 20;
```
#### mongdb  limit与skip方法
- limit
db.集合名.find().limit(数字)
- skip
db.集合名.find().limit(数字).skip()  # skip() 方法默认参数为0
***
```
如sql中：select * from 表名 limit 10 offset 20; # 跳过20条，查询10条
        select * from 表名 limit 10,20;  # 跳过10，查询20条
```
- 顺带说一下MySQL limit优化
例：select * from test limit 10,10;
   select * from test limit 10000,10010;
虽然都是查10条，但查询时间明显差距会较大
```
offset比较小时，偏移offset较小的时候，直接使用limit较优
ffset比较小时，偏移offset较大的时候，使用子查询，能节省大量时间
Select * From test Where id ＞=(
Select id From test Order By id limit 10000,1
) limit 10
```
***
#### mongdb索引
**MongoDB使用 createIndex() 方法来创建索引**
3.0.0之前的版本使用db.collection.ensureIndex()
```
db.集合名.createindex(keys,options)
# Key 值为你要创建的索引字段，1 为指定按升序创建索引，如果你想按降序来创建索引指定为 -1 
```
**也可以使用多个字段创建多个字段的索引**
#### 聚合

#### 分片

#### 备份、恢复