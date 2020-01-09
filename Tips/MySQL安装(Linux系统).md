---
title: "MySQL安装(Linux系统)"
categories:
- 数据库
tags:
- SQL
---


#### 数据库简介
数据库 - 实现项目中的数据持久化
数据库类别：
- 关系型数据产品
  - `Oracle` - 甲骨文
  - `MySQL` - 甲骨文 - `MariaDB`
  - `DB2`、`SQLServer`、`PostgreSQL`、`SQLite`

- 非关系型数据库
- `NoSQL`数据库 - `Redis`
   
   - `MongoDB` - 文档数据库 - 适应量大但是价值低的数据
   - `Rdeis` - KV数据库 - 性能好适合做高速缓存服务
   - `ElasticSearch` - 搜索引擎
- MySQL
   特点：
   - 理论基础 ：集合论和关系代数
   - 用二维表来组织数据（行（记录）和列（字段））
   - 能够唯一标识一条记录的列称为主键（`primary key`）
   - SQL - 结构化查询语言
   >DDL - 数据定义语言 - create / drop / alter
   >DML - 数据操作语言 - insert / delete / update / select
   >DCL - 数据控制语言 - grant / revoke / commit / rollback
#### MySQL服务端安装
- Linux安装软件
> 1. 包管理工具 - yum / rpm
```
Docker - 提供虚拟化服务，创建虚拟化容器并安装软件
yum -y install docker-io
yum -y remove docker-io
yum info ...
yum search ...
yum list installed | grep docker
```

> Docker服务
```
systemctl start docker
systemctl stop docker
systemctl restart docker
systemctl status docker
systemctl enable docker
systemctl disable docker
```

> Docker的命令
```
1. 查看已经下载的镜像文件（安装包）：
   docker images

2. 下载MySQL的镜像文件：
   docker pull mysql:5.7

MySQL数据库超级管理员账号 - root

3. 创建并运行容器：
   docker run -d -p 3306:3306 --name mysql57 -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7

4. 查看运行中的容器：
   docker ps

5. 查看所有的容器：
   docker container ls -a

6. 停止容器
   docker stop mysql57

7. 启动容器
   docker start mysql57

8. 删除容器
   docker rm -f mysql57
```
#### 安装MySQL客户端工具：
Navicat for MySQL - 猫
SQLyog - 海豚
Toad for MySQL - 蛤蟆