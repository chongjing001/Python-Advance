### MySQL配置



#### mysql密码策略相关参数

##### 查看 mysql 初始的密码策略

```sql
SHOW VARIABLES LIKE 'validate_password%';
```

##### 密码的验证强度等级,默认为 MEDIUM

```sql
set global validate_password_policy=
```

> 关于 validate_password_policy 的取值：
> 0/LOW：只验证长度；
> 1/MEDIUM：验证长度、数字、大小写、特殊字符；
> 2/STRONG：验证长度、数字、大小写、特殊字符、字典文件；

##### 当前密码长度`validate_password_length`

```sql
set global validate_password_length=
```



##### 设置或修改密码, 示例：

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
```



##### 其他

>`validate_password_dictionary_file` 指定密码验证的文件路径
>
>`validate_password_mixed_case_count`  整个密码中至少要包含大/小写字母的总个数
>
>`validate_password_number_count ` 整个密码中至少要包含阿拉伯数字的个数
>
>`validate_password_special_char_count` 整个密码中至少要包含特殊字符的个数





#### mysql 开放权限

```sql
grant all privileges on *.* to 'root'@'172.17.0.2' identified by 'passwd2' with grant option;
```

- 开放所有权限给root,当root以passwd2(不一定是root登录密码,仅作为情景下登录的密码)密码从 172.17.0.2 登入的时候,允许其操作所有数据库下的所有表
- `*.*`可以改成特定数据库下的特定表

```sql
flush privileges;   刷新
```

*重启数据库*

```
systemctl restart mysqld
```

