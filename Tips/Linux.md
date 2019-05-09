---
title: "Linux常用终端命令"
categories:
- Linux
tags:
- 命令
top: true
---
### 基本指令
**下面四个为ubantu安装更新命令**
sudo  apt  install 软件名         安装软件

sudo  apt  remove  软件名     卸载软件

sudo  apt   update                 更新可用软件列表

sudo  apt   upgrade                更新已安装的包

#### 常用文件指令
命令                               对应英文                           作用
ls                                    list                                    查看当前文件夹的内容
pwd                                print work directory        查看当前所在文件夹
cd     【目录名】             change directory              切换文件夹
touch【文件名】             touch                                如果文件不存在，新建文件
mkdir【目录名】             make directory                 创建目录
rm     【文件名】             remove                             删除指定文件
clear                               clear                                  清屏

vim  文本文件                                                      修改文本内容
                                                                           esc 修改输入方式
                                                                           :wq  保存并退出
                                                                           :q!    强制退出
删除目录  rm -r 目录名
               rm  -i 文件或目录
               rm -f 强制删除

--help   和   man        显示.....命令的帮助信息
例：touch --help        或者  man touch
使用man时的操作
操作键                   功能
空格键                   显示手册页的下一屏
Enter                     一次滚动手册页的一行
b                           回滚一屏
f                             前滚一屏
q                            退出
/word                    搜索word字符串

以.开头的文件为隐藏文件，需要用-a参数才能显示
.代表当前目录
..代表上一级目录
#### 快捷键
ctr + f 		- 前进一个字符
ctr + b		- 后退一个字符
ctr + a		- 回到行首
ctr + e 		- 回到行尾
ctr + w		- 向左删除一个单词
ctr + u		- 向左删除全部
ctr + k		- 向右删除全部
ctr + y		- 粘贴上次删除的内容
ctr + l		- 清屏
#### ls的通配符 
```
*          代表任意个字符
？        代表一个字符  
[]         表示匹配字符组中的任意一个
[abc]    表示匹配a、b、c中的任意一个
[a-f]     表示匹配a到f范围内的任意一个字符
```
cd命令常用参数
（更改当前工作目录）
cd ~ 或cd 切换当前用户的主目录（/home/用户目录）
cd.    保持当前目录不变
cd..   切换到上级目录
cd -  可以在最近两次工作目录之间来回切换

mkdir -p  可以递归创建目录  如a/b/c/d

命令                               对应英文                           作用
tree[目录名]                   tree                                  以树状图列出文件目录结构
cp 源文件 目录文件         copy                                复制文件或目录
mv 源文件 目标文件        move                               移动文件或者目录/文件  或者目录重命名

-I  在执行cp或mv有提示作用

cat 文件名                      concatenate                     查看文件内容、创建文件、合并、追加文件内容等功能
more 文件名                  more                                分屏显示文件内容
grep 搜索文本文件文件名 grep                               搜索文本文件内容

 cat      适合查看文件内容较少的文件
 more  适合查看文件内容较多的文件 
grep -n 显示匹配行及行号    -v显示不包括匹配文本的所有行    -i忽略大小写       

echo 重定向

管道 |
一个命令的输出  可以通过管道 作为 另一个命令的输入 例： ls -lh | more
### 高级命令
shutdown  关机/重新启动

-r 重新启动
shutdown -c  取消关机
shutdown -r now  立刻重启

Ctrl c  可以中断 终端命令

命令                                                  对应英文                                       作用
ifconfig                                        configure a network interface      查看/配置计算机当前网卡信息
ping ip 地址                                  ping                                              检测目标ip地址的连接是否正常

ssh 用户名@ip                               secure shell                                   关机/重新启动
scp 用户名@ip:文件名或路径         
​       用户名@ip:文件名或路径             secure  copy                                远程复制文件
#### 网络管理

常见服务器端口
SSH 服务器      22
Web 服务器     80
HTTPS             443
FTP 服务器       21

ifconfig     查看网卡状态

netstat   -natp					- 查看网络连接状态
netstat   -natp|grep  端口号			- 查看指定端口的网络连接状态	

ping  地址 
ping  -i   时间	地址
ping  -c  次数    地址

telnet  ip地址	端口		 - 查看远程主机网络连接状况

dig 地址			- 查看DNS
wget  地址			- 下载

scp -P port     01.py     user@remote:Desktop/01.py
​            端口    原文件     远程复制的文件

**SSH 高级**

- 免密码登录

   配置公匙
   ssh-keygen 即可生成SSH 钥匙，回车即可
   上传公匙到服务器

    ssh-copy-id -p port user@remote,可以让服务器记住公匙
#### 权限管理
chmod 
可以修改文件或目录的权限
chmod  +/- rwx 文件名或目录名

   目录             拥有者权限             组权限               其他用户权限
文件权限示例          -  r   w   -           r   w   -               r   -      -
目录权限示例         d r   w    x         r   w   x               r   -      x

组管理  终端命令
    命令                                    作用
  groupadd 组名                     添加组
  useradd -G 分组列表          添加组到指定目录
  groupdel  组名                      删除组
  cat/etc/group                       确认组信息
  chgrp 组名  文件/目录名        递归修改文件/目录所属组

用户管理  终端命令
   命令                                            作用                  说明
  useradd -m -g 组 新建用户名     添加新用户        -m 自动建立用户目录
                                                                             -g 指定用户所在的组，否则会建立一个同名的组
  passwd  用户名                          设置用户密码     如果是普通用户，可直接使用passwd修改自己的账户密码
  userdel -r 用户名                       删除用户             -r 选项会自动删除用户家目录
  cat/ect/passwd | grep 用户名    确认用户信息      新建用户后，用户信息会保存在/etc/passwd 文件中


查看用户信息
       命令                         作用
   id [用户名]                 查看用户UID和GID信息
   who                           查看当前所用登录的用户列表
   whoami                     查看当前登录用户的账户名

passwd文件
/etc/passwd 文件存放的是用户信息，由6个分号组成的7个信息
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

命令             作用                                    说明 
su -用户名    切换用户，并且切换目录     - 可以切换到用户家目录，否则保持位置不变
exit               退出当前用户

su 不接用户名，可以切换到root，但不推荐使用，因为不安全

chown         修改拥有者
chgrp           修改组
chmod        修改权限

递归修改文件权限
chmod -R 755 文件名|目录名

      拥有者              组                   其他
     r    w     x        r     w     x        r     w     x
     4   2       1       4    2      1       4     2     1      
 0:表示没有权限

4    2      1               7               rwx
4    2      0               6               rw-
4    0      1               5               r-x
4    0      0               4               r--
0    2      1               3               -wx
0    2      0               2               -w-
0    0      1               1               --x
0    0      0               0               ---

系统信息相关命令
时间和日期
date    查看系统时间
cal      calendar查看日历，-y选项可以查看一年的日历

df -h    disk free显示磁盘的剩余空间
du -h[目录名]     disk  usage显示目录下的文件大小

进程信息
ps aux           process status 查看进程的详细状况
top                 动态显示运行中的进程并且排序
kill [-9]进程代号   终止指定代号的进程，-9表示强行终止

a  显示终端上的所有进程，包括其他用户的进程
u  显示进程的详细状态
x  显示没有控制终端的进程

find [路径] -name “.py” 查找指定路径的扩展名是.py的文件，包括子目录

ln -s 被链接的源文件链接文件   建立文件的软连接，类似window的快捷方式
 ---------链接文件的路径要使用绝对路径

#### 打包和解压

tar  打包/解包
tar -cvf 打包文件.tar 被打包的文件/路径...
tar -xvf 解包文件.tar

c  生成档案文件，创建打包文件
x  解开档案文件
v  列出归档解档的详细过程，显示进度
f  制定档案文件名称，f后面一定是.tar文件，所以必须放选项最后
压缩文件
tar -zcvf  打包文件.tar.gz 被压缩的文件/路径...  
解压缩文件
tar -zxvf 解包文件.tar.gz
解压缩到指定路径
tar -zxvf 解包文件.tar.gz -C目标路径 

bzip2
压缩文件
tar -jcvf  打包文件.tar.bz2 被压缩的文件/路径...
解压文件
tar -jxvf 解包文件.tar.bz2