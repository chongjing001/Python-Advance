### 安装
- 安装postgresql服务器
sudo apt-get insatll postgresql
- 安装postgresql 客户端
sudo apt-get install postgresql-client

- 一般情况下，安装完成后，postgresql服务器会自动在5432端口开启
- 如果想安装图形化管理界面
sudo apt-get install pgadmin3

### 添加新用户和数据库
初次安装后，默认生成一个名为postgres的数据库和一个名为postgres的数据库用户。这里需要注意的是，同时还生成了一个名为postgres的Linux系统用户。
我们可以使用postgres用户，来生成其他用户和新数据库
#### 使用shell命令行
1.创建数据库用户testuser，并指定其为超级用户。
sudo -u postgres createuser --superuser testuser
然后，登录数据库控制台，设置testuser用户的密码，完成后退出控制台。
```
sudo -u postgres psql
\password testuser
\q
```
接着，在shell命令行下，创建数据库test，并指定所有者为testuser。
sudo -u postgres createdb -O testuser test
### 登录数据库
添加新用户和新数据库以后，就要以新用户的名义登录数据库，这时使用的是psql命令。
psql -U testuser -d test -h 127.0.0.1 -p 5432
上面命令的参数含义如下：-U指定用户，-d指定数据库，-h指定服务器，-p指定端口。
输入上面命令以后，系统会提示输入testuser用户的密码。输入正确，就可以登录控制台了。
psql命令存在简写形式。如果当前Linux系统用户，同时也是PostgreSQL用户，则可以省略用户名（-U参数的部分）。举例来说，我的 Linux系统用户名为ruanyf，且PostgreSQL数据库存在同名用户，则我以ruanyf身份登录Linux系统后，可以直接使用下面的命令 登录数据库，且不需要密码。
psql test
此时，如果PostgreSQL内部还存在与当前系统用户同名的数据库，则连数据库名都可以省略。比如，假定存在一个叫做ruanyf的数据库，则直接键入psql就可以登录该数据库。
psql
另外，如果要恢复外部数据，可以使用下面的命令。
psql test < test.sql

### 控制台命令
```
\q:退出
\p:设置密码
\h：查看SQL命令的解释，比如\h select。
\?：查看psql命令列表。\l：列出所有数据库。
\c [database_name]：连接其他数据库。
\d：列出当前数据库的所有表格。
\d [table_name]：列出某一张表格的结构。
\du：列出所有用户。
\e：打开文本编辑器。
\conninfo：列出当前数据库和连接的信息。
```
### 数据库操作
```
# 创建新表
CREATE TABLE user(name VARCHAR(20), date DATE);
usertbl
# 插入数据
INSERT INTO user(name, date) VALUES('张三', '2013-12-22');

# 选择记录
SELECT * FROM user;

# 更新数据
UPDATE user set name = '李四' WHERE name = '张三';

# 删除记录
DELETE FROM user WHERE name = '李四' ;

# 添加栏位
ALTER TABLE user ADD email VARCHAR(40);

# 更新结构
ALTER TABLE user ALTER COLUMN date SET NOT NULL;

# 更名栏位
ALTER TABLE user RENAME COLUMN date TO signup;

# 删除栏位
ALTER TABLE user DROP COLUMN email;

# 表格更名 
ALTER TABLE user RENAME TO backuptbl;

# 删除表格
DROP TABLE IF EXISTS backup_tbl;
```