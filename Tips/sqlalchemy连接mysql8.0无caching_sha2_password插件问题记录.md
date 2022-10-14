#### sqlalchemy连接mysql8.0无caching_sha2_password插件问题记录



*stack error*：

```
sqlalchemy.exc.OperationalError: (_mysql_exceptions.OperationalError) (2059, "Authentication plugin 'caching_sha2_password'

```



- 方式一：

创建新的新用户，使用mysql_native_password插件

   *mysql shell*

```shell

--创建新的用户 
create user root@'%' identified WITH mysql_native_password BY 'root';
grant all privileges on *.* to root@'%' with grant option;
flush privileges;
	
```





- 方式二：

安装mysql 8.0 客户端

*linux*-centos7

```shell
yum -y install http://dev.mysql.com/get/mysql80-community-release-el7-7.noarch.rpm
```



```shell
yum -y install mysql
```

