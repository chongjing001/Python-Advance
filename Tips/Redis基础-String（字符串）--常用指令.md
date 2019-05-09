---
title: "Redis基础 String（字符串）- 常用指令"
categories:
- 数据库
tags:
- NoSQL
photo:
- http://pk0mla8df.bkt.clouddn.com/QQ%E6%88%AA%E5%9B%BE20181228193758.png

---

- 1.set - 创建键值对 例：set abc 123
- 2.get - 获取键值对    get abc
- 3.setbit -   bit默认初始化为0
```
redis>setbit num 100 1
(integer)0
redis>setbit num 99  # 除100其他数都返回0
（integer）0
redis>setbit num 100 
(interger)1
```
- 4.setex - 产生键值对，并设置存活时间，如果key值存在则覆盖
```
#当keys不存在时进行setex
redis>setex number 60 1000
OK
redis>get number 
'1000'
redis>ttl number #剩余生存时间
(integer)50

#key存在时，setex覆盖旧值
redis>setex name 旧值
OK
redis>setex name 100 '新值'
OK
redis>get name
'新值'
redis>ttl name
(integer)90
```
- 5.exists - 当key值不存在时，可以创建，存在时创建失败
```
# 对非空字符串进行 SETRANGE

redis> SET greeting "hello world"
OK

redis> SETRANGE greeting 6 "Redis"
(integer) 11

redis> GET greeting
"hello Redis"


# 对空字符串/不存在的 key 进行 SETRANGE

redis> EXISTS empty_string
(integer) 0

redis> SETRANGE empty_string 5 "Redis!"   # 对不存在的 key 使用 SETRANGE
(integer) 11

redis> GET empty_string           # 空白处被"\x00"填充
"\x00\x00\x00\x00\x00Redis!
```
- 6.setlen - 获取字符串的长度
```
redis>set n1 'hello world'
OK
redis>setlen n1
(integer)11

# 不存在的key长度为0
redis>strlen n2
(integer)0
```
- 7.mset/mget 同时设置/获取多个键值对
```
redis> mset a 1 b 2 c 3
OK
redis>mget a b c
1)'1'
2)'2'
3)'3'
注意：mset会覆盖旧值
```
- 8 incr - key的值加一
```
redis>set num 20
OK
redis>incr num
(integer)21
redis>get num # 数字在redis中以字符串的形式保存
'21'
```
- 9 incrby 当key不存在时可以创建，key不是数字时后报错
```
# key 存在且是数字值

redis> SET rank 50
OK

redis> INCRBY rank 20
(integer) 70

redis> GET rank
"70"


# key 不存在时

redis> EXISTS counter
(integer) 0

redis> INCRBY counter 30
(integer) 30

redis> GET counter
"30"


# key 不是数字值时

redis> SET book "long long ago..."
OK

redis> INCRBY book 200
(error) ERR value is not an integer or out of range
```
- 10 decr/ decrby 用法和和上面相同，不同的是 key - 1
- 11 append - 如果 key 已经存在并且是一个字符串， append 命令将 value 追加到 key 原来的值的末尾;如果 key 不存在， append 就简单地将给定 key 设为 value ，就像执行 set key value 一样。









Redis的list类型 - 经典数据存储结构：
栈（stack）- FILO - 先进后出
 lpush + lpop / rpush + rpop
队列（queue） - FILO - 先进先出
lpush + rpop / rpush + lpop
