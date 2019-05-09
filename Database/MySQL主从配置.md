#### 一、找到MySQL的配置文件
- linux：在  /etc/mysql中的mysql.cnf 
   或者/etc/mysql/mysql.conf.d中的mysqld.cnf
- windows: 一般在C:\Program Files (x86)\MySQL\MySQL Server 下有一个my.ini的  文件

***
#### 二、主机配置
在配置文件中找到  [mysqld]
```shell
[mysqld]
# 下面时新加的内容
server-id=200  # 设置主服务器器的ID  数字随意
innodb_flush_log_at_trx_commit=2
# 操作系统崩溃或者系统断电的情况下,上一秒钟所有事务数据才可能丢失
sync_binlog=1  # 开启binlog日日志同步功能
log-bin=mysql-bin-200  # binlog日日志文文件名
# binlog-do-db=goto # 这个表示只同步某个库 (如果没有此项,表示同步所有的库)
```
**注意：这里还有一个地方没有修改，后面会出现**
![一直连接不上](https://img-blog.csdnimg.cn/20190414171144320.png)
```shell
bind-address            = 127.0.0.1
# 表示只监听本地，所有其他ip（从机）会被拒绝，连不上
```
**最好把上面bind-address注释掉**
```shell
# bind-address           = 127.0.0.1
```
***
###### 配置完成后重启一下
**linux：**
```
systemctl restart mysql
或者 service mysqld restart
```
**window：**
```
停止服务：net stop mysql
开启：net start mysql
```
###### 登录mysql
```
mysql -uroot  -p
# 分配权限给从库
# 例：授权给从数据库服务器192.168.1.14,用户名mark,密码123456
mysql>grant replication slave on *.* to 'mark'@'192.168.1.14' identified by '123456';
#查看主库的状态
 mysql>show master status ; 
```
![](https://img-blog.csdnimg.cn/20190414173033897.png)
**这里的File和Position的值配置从库的时候有用**
***
#### 三、从机配置
###### 配置从库
**还是mysql的配置文件**
```shell
server-id=300
innodb_flush_log_at_trx_commit=2
sync_binlog=1
log-bin=mysql-bin-300
```
**重启从机的mysql服务**
命令和上面的一样

###### 测试一下是否能连上刚才分配mark
```shell
mysql -umark -h192.168.1.12 -p123456
```
可以进入的话一般就ok
进入mysql客户端
```
mysql>change master to master_host='192.168.1.12',master_user='mark' ,master_password='123456', master_log_file='mysql-bin-202.000003' ,master_log_pos=564;
```
```
mysql> start slave; ##开启从库 (stop slave:关闭从库
```
```
mysql> show slave status; # Slave_IO_Running,Slave_SQL_Running 都为Yes的时候表示配置成功
```
![](https://img-blog.csdnimg.cn/20190414201654765.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyODc0OTk0,size_16,color_FFFFFF,t_70)
***
#### 验证主从复制功能（略...）
> mysql>create database hello default charset='utf8';
> mysql>use hello;
> ```
> mysql>create table user (
>       id int primary key auto_increment,
>       name varchar(128) not null,
>       age int not null
> );
> ```
**查看从库是否有------------------------------------------------------------------->**
