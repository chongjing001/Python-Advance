---
title: "Redis基础（一）"
categories:
- 数据库
tags:
- NoSQL
---
#### 安装Redis
```
wget http://download.redis.io/releases/redis-5.0.3.tar.gz

解包
gunzip redis-5.0.3.tar.gz
tar -xvf redis-5.0.3.tar

cd redis-5.0.3
编译
gcc --version
安装
make && make install
```
**提供高速缓存服务 - 缓存热点数据（访问量大数据不大）**
**缓解了数据的压力（高频访问数据不用直接访问数据库）**
```
启动：
redis-server --requirepass 123456 --appendonly yes > redis.log 2> redis-error.log &

连接自己的redis
redis -cli -h ip -p 端口
密码：auth 123456
auth - 验证身份
ping - 心跳时间

set  - 设置键值对
git  - 取值

expire - 设置超时时间
ttl 内容 - 查看剩余存活时间  -1 永久  -2 超时  - 正整数 剩余时间
keys * 查看所有键

flushdb  - 清空数据库中所有键值对
flushall - 清除所有数据库中的所有键值对

existis 判断是否存在
select 序号（默认有16库） 切换数据库


save / bgsave - 保存数据 / 后台保存数据
shutdown - 关闭服务器


Redis提供两种持久化数据的方案：
1. RDB - 默认开启
2. AOF - 默认关闭 -- appendonly yes
```