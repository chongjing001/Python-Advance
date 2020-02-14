---
title: "Linux常用终端命令"
categories:
- Linux
tags:
- 命令
top: true
---
#### `ubantu`安装更新命令

| 命令                      | 说明                       |
| ------------------------- | -------------------------- |
| sudo  apt  install 软件名 | 安装软件                   |
| sudo  apt  remove  软件名 | 卸载软件                   |
| sudo  apt   update        | 更新可用软件列表           |
| sudo  apt   upgrade       | 更新已安装的包             |
| sudo  apt autoclean       | 清理旧版本的软件缓存       |
| sudo apt  clean           | 清理所有软件缓存           |
| sudo apt autoremove       | 删除系统不再使用的孤立软件 |

#### 快捷键

| 命令     | 说明               |
| -------- | ------------------ |
| ctrl + f | 前进一个字符       |
| ctrl + b | 后退一个字符       |
| ctrl + a | 回到行首           |
| ctrl + e | 回到行尾           |
| ctrl + w | 向左删除一个单词   |
| ctrl + u | 向左删除全部       |
| ctrl + k | 向右删除全部       |
| ctrl + y | 粘贴上次删除的内容 |
| ctrl + l | 清屏               |
| ctrl + r | 检索历史命令       |


#### 常用基本命令

| 命令           | 对应英文             | 说明                         |
| -------------- | -------------------- | ---------------------------- |
| ls             | list                 | 查看当前文件夹的内容         |
| pwd            | print work directory | 查看当前所在路径             |
| cd  [目录名]   | change directory     | 切换文件夹                   |
| touch [文件名] |                      | 创建文件                     |
| rm [文件名]    | remove               | 删除文文件                   |
| clear          | clear                | 清屏 (快捷键：`ctrl + l`)    |
| cp             | copy                 | 拷贝文件                     |
| mv             | move                 | 移动文件                     |
| mkdir          | make directory       | 创建目录                     |
| tree [目录]    |                      | 以树状图列出文件目录结构     |
| cat            |                      | 查看文件内容（终端输出方式） |
| echo           |                      | 重定向                       |
| shutdown       |                      | 关机                         |
| find           |                      | 查找文件                     |

> 补充

  - 删除
    -   `rm -r` 目录名
    -  `rm  -i `文件或目录
    -   ` rm -f `强制删除

  - `--help   和   man`        显示.....命令的帮助信息
    例：touch --help        或者  man touch
    使用man时的操作
    操作键                   功能
    空格键                   显示手册页的下一屏
    Enter                     一次滚动手册页的一行
    b                           回滚一屏
    f                             前滚一屏
    q                            退出
    /word                    搜索word字符串

- 以`.`开头的文件为隐藏文件，需要用`-a`参数才能显示
  `.`代表当前目录
  `..`代表上一级目录
- ls的通配符 
```
*          代表任意个字符
？         代表一个字符  
[]         表示匹配字符组中的任意一个
[abc]     表示匹配a、b、c中的任意一个
[a-f]     表示匹配a到f范围内的任意一个字符
```
- cd命令常用参数

```
（更改当前工作目录）
cd ~ 或 cd    切换当前用户的主目录（/home/用户目录）
cd .         保持当前目录不变
cd ..        切换到上级目录
cd -         可以在最近两次工作目录之间来回切换
```

- 递归创建目录

  - `mkdir -p`
  - 示例：`mkdir -p a/b/c/d`
  
- 管道 `|`
  
  - 一个命令的输出  可以通过管道 作为 另一个命令的输入
  
- 关机/重新启动 `shutdown`
  - `-r `重新启动
  - `shutdown -c`  取消关机
  - `shutdown -r now`  立刻重启
  
- `find`

  - 示例：`find [路径] -name “.py” 查找指定路径的扩展名是.py的文件，包括子目录`

- 软链接

  - `ln -s` 被链接的源文件链接文件   建立文件的软连接，类似windows的快捷方式

  - 链接文件的路径要使用绝对路径

    #### 

####  进阶命令

| 命令                                       | 说明                         |
| ------------------------------------------ | ---------------------------- |
| ifconfig                                   | 查看/配置计算机当前网卡信息  |
| ping ip 地址                               | 检测目标ip地址的连接是否正常 |
| ssh 用户名@ip                              | 远程连接                     |
| scp 文件或目录 用户名@ip:文件名或路径      | 远程上传文件                 |
| scp  用户名@ip:文件名或路径   本地文件路径 | 从远程下载文件               |
| netstat / top / ps                         | 查看网络状态和端口占用情况   |
| dig                                        | 查看DNS                      |
| wget                                       | 下载                         |
| ssh-keygen                                 | ssh秘钥                      |
| chmod                                      | 权限管理                     |
| who                                        | 查看电脑用户                 |
| free                                       | 查看内存使用情况             |
| df                                         | 磁盘占用情况                 |



> 补充

- 常见服务器端口
  - SSH 服务器      22
  - Web 服务器     80
  - HTTPS             443
  - FTP 服务器       21

- `netstat`
  - `netstat   -natp`					- 查看网络连接状态
  - `netstat   -natp|grep`  端口号			- 查看指定端口的网络连接状态	

- 免密码登录

   - 配置公匙
     - ``ssh-keygen` 即可生成`SSH` 钥匙，回车即可
   - 上传公匙到服务器
  -  `ssh-copy-id -p port user@remote`,可以让服务器记住公匙


#### 权限管理
- `chmod` : 修改文件或目录的权限
  `chmod  +/- rwx` 文件名或目录名

```
   目录             拥有者权限             组权限               其他用户权限
文件权限示例         -  r   w   -         r   w   -               r   -    -
目录权限示例         d  r   w   x         r   w   x               r   -    x
```





##### 组管理  终端命令

| 命令                    | 说明                    |
| ----------------------- | ----------------------- |
| groupadd 组名           | 添加组                  |
| useradd -G 分组列表     | 添加组到指定目录        |
| groupdel  组名          | 删除组                  |
| cat /etc/group          | 确认组信息              |
| chgrp 组名  文件/目录名 | 递归修改文件/目录所属组 |

```
chown         修改拥有者
chgrp         修改组
chmod         修改权限
```

递归修改文件权限
`chmod -R 755` 文件名|目录名

        拥有者                  组                  其他
     r    w     x        r     w     x        r     w     x
     4    2     1        4     2     1        4     2     1      


> 0 : 表示没有权限
>
> `r` : 可读   `w` : 可写  `x` : 执行

```
4    2      1               7               rwx
4    2      0               6               rw-
4    0      1               5               r-x
4    0      0               4               r--
0    2      1               3               -wx
0    2      0               2               -w-
0    0      1               1               --x
0    0      0               0               ---
```





#####  用户管理  终端命令

| 命令                        | 说明                                                         |
| --------------------------- | ------------------------------------------------------------ |
| useradd -m -g 组 新建用户名 | 添加新用户        -m 自动建立用户目录  -g 指定用户所在的组，否则会建立一个同名的组 |
| passwd  用户名              | 设置用户密码     如果是普通用户，可直接使用passwd修改自己的账户密码 |
| userdel -r 用户名           | 删除用户             -r 选项会自动删除用户家目录             |
| cat /ect/passwd grep 用户名 | 确认用户信息      新建用户后，用户信息会保存在/etc/passwd 文件中 |
| su -用户名                  | 切换用户      su 不接用户名，可以切换到root，但不推荐使用，因为不安全 |
|                             |                                                              |



##### 查看用户信息

```
   命令                         作用
   id [用户名]                 查看用户UID和GID信息
   who                        查看当前所用登录的用户列表
   whoami                     查看当前登录用户的账户名
```



###### `passwd` 文件

```
/etc/passwd  文件存放的是用户信息，由6个分号组成的7个信息
1.用户名
2.密码（x：表示加密的密码）
3.UID （用户标识）
4.GID （组标识）
5.用户全名或本地账号
6.家目录
7.登录使用的 Shell，就是登录之后使用的终端命令，ubantu默认是dash

usermod 修改用户登录 shell
usermod -s /bin/bash 用户名

/etc/passwd 是用于保护用户信息的文件
/usr/bin/passwd 是用于修改用户的密码

which 命令可以查看执行命令所在的位置
which ls   输出-->  /bin/ls
which useradd  输出-->  /usr/sbin/useradd
```



#### 系统信息相关命令
##### 时间和日期

```
date              查看系统时间
cal               查看日历，-y选项可以查看一年的日历
df -h            显示磁盘的剩余空间
du -h[目录名]     显示目录下的文件大小
```

##### 进程信息

```
ps aux      process status    查看进程的详细状况
top                           动态显示运行中的进程并且排序
kill [-9]进程代号              终止指定代号的进程，-9表示强行终止

a                             显示终端上的所有进程，包括其他用户的进程
u  							  显示进程的详细状态
x  							  显示没有控制终端的进程
```

##### 定时器`crontab`

`/etc/crontab`文件

```
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
```

`minute`： 表示分钟，可以是从0到59之间的任何整数。
 `hour`：表示小时，可以是从0到23之间的任何整数。
 `day`：表示日期，可以是从1到31之间的任何整数。
 `month`：表示月份，可以是从1到12之间的任何整数。
 `week`：表示星期几，可以是从0到7之间的任何整数，这里的0或7代表星期日。
 `command`：要执行的命令，可以是系统命令，也可以是自己编写的脚本文件

```
星号（*）：代表所有可能的值，例如month字段如果是星号，则表示在满足其它字段的制约条件后每月都执行该命令操作。

逗号（,）：可以用逗号隔开的值指定一个列表范围，例如，“1,2,5,7,8,9”

中杠（-）：可以用整数之间的中杠表示一个整数范围，例如“2-6”表示“2,3,4,5,6”

正斜线（/）：可以用正斜线指定时间的间隔频率，例如“0-23/2”表示每两小时执行一次。同时正斜线可以和星号一起使用，例如*/10，如果用在minute字段，表示每十分钟执行一次。
```

> 几个命令

```
crontab

Options:
 -u <user>  define user            指定某个用户的crontab文件
 -e         edit user's crontab    编辑crontab文件
 -l         list user's crontab    列出crontab文件
 -r         delete user's crontab  删除
 -i         prompt before deleting   显示某个用户的crontab文件内容，默认当前
 -n <host>  set host in cluster to run users' crontabs
 -c         get host in cluster to run users' crontabs
 -s         selinux context
 -x <mask>  enable debugging

```



#### 打包和解压

- `.tar`格式

```
tar  打包/解包
tar -cvf 打包文件.tar 被打包的文件/路径...
tar -xvf 解包文件.tar

c  生成档案文件，创建打包文件
x  解开档案文件
v  列出归档解档的详细过程，显示进度
f  制定档案文件名称，f后面一定是.tar文件，所以必须放选项最后
```

- `.tar.gz`格式

```
压缩文件
tar -zcvf  打包文件.tar.gz 被压缩的文件/路径...

解压缩文件
tar -zxvf 解包文件.tar.gz

解压缩到指定路径
tar -zxvf 解包文件.tar.gz -C目标路径 
```

- `.tar.bz2`格式

```
压缩文件
tar -jcvf  打包文件.tar.bz2 被压缩的文件/路径...

解压文件
tar -jxvf 解包文件.tar.bz2
```

- `zip`格式

```
压缩
zip FileName.zip DirName

解压
unzip FileName.zip
```



#### 特殊符号之`;`  `|`   `&`

##### `;`分号符

```
command1 ; command2
用;号隔开每个命令, 每个命令按照从左到右的顺序,顺序执行，
彼此之间不关心是否失败， 所有命令都会执行
```

##### `|`管道符

```
command1 | command2
左边命令的输出就会作为管道符右边命令的输入
示例：列出/home目录下带有hello的文件
ls /home | grep hello
```

##### `&` 设置进程为后台

```
command &
默认情况下进程为前台进程，这样就把当前shell占了，如果在命令后面加上&就可以将进程挂在后台
```

`&&` 

```
command1 && command2
当command1执行成功后，才会执行command2
```

`||`

```
command1 || command2
当command1执行失败才会执行command2
```



