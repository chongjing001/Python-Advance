
---
title: ssh免密登陆及登陆失败后的解决办法
categories:
- 服务器
tags:
- ssh

---


#### 这篇文章主要给大家介绍了关于centos配置ssh免密码登录以及登录后仍要输入密码的解决方法,需要的朋友可以参考下

- 首先，我们需要明白为什么要设置SSH免密码登录，其原因是我们在开启服务器的时候需要多次输入yes和root密码，这是我们所不能忍受的，我们迫切需要实现免登录的功能

<font color="#dd0000">第一步：在本机中创建秘钥</font><br /> 
1.执行命令：
>ssh-keygen -t rsa -C "xx@qq.com"
>(随便编个字符串，一般用邮箱）
>**注意事项**
>2、之后一路回车就行啦；会在～（home）目录下中产生.ssh（隐藏）文件夹；
>3、里面有两个文件id_rsa(私钥)、id_rsa.pub(公钥)文件
>注意事项：
>①在liunx环境下，要想复制公钥或是私钥，不要使用vim等编辑器打开文件来复制粘贴；
>因为它会产生不必要的回车。
>②应该使用cat把内容打印到终端上再来复制粘贴；
><font color="#dd0000">第二步：用 ssh-copy-id 把公钥复制到远程主机上</font><br /> 
>ssh-copy-id zhangming@192.168.161.132
>把秘钥拷贝到远程服务器

用这种方式拷贝使用的端口是Linux默认的22，如果你想指定端口，可以使用：

ssh-copy-id -i /用户名/.ssh/id_rsa.pub '-p 端口号 用户名@106.75.52.44'
>ssh-copy-id -i /root/.ssh/id_rsa.pub '-p 22222 root@106.75.52.44'
>这里可能需要等一段时间，反正我是等了挺久的时间，然后显示要你输入密码：

zhangming@106.75.52.44's password:
输入完密码后，显示：
Now try logging into the machine, with "ssh '-p 22222 root@106.75.52.44'", and check in:
 .ssh/authorized_keys
to make sure we haven't added extra keys that you weren't expecting.
表示成功了！
<font color="#dd0000">第三步：远程登入</font><br />
>[zhangming@localhost ~]$ ssh zhangming@192.168.161.134
>Last login: Mon Oct 10 14:18:54 2016 from 192.168.161.135
> ssh zhangming@123.59.44.56 -p 22222

 **注意**
 遇到的大坑：
配置ssh免密码登录后，仍提示输入密码

>解决方法：
>首先我们就要去查看系统的日志文件
> cat /var/log/secure 

发现问题的所在：Authentication refused: bad ownership or modes for file
从字面上可以看出是目录的属主和权限配置不当，查找资料得知：SSH不希望home目录和~/.ssh目录对组有写权限，通过下面几条命令改下
> g-w /home/zhangming
> chmod 700 /home/zhangming/.ssh
> chmod 600 /home/zhangming/.ssh/authorized_keys
> 然后我们再去登录，就能不用密码进入了。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~