####  搭建nginx静态资源服务器(以图片为例)

##### 准备
- 云服务器一台
- nginx(安装略)

##### 配置
**1.首先进入nginx主配置文件，`vim /etc/nginx/nginx.conf`**
```shell
# 在http{}里面添加一个路径
http{
# ... 省略代码

# 告诉nginx主文件去下面路径寻找配置
include /home/conf/*.conf

# ... 省略代码


}
```
**2.配置椎间的 xxx.conf 文件**
示例：

- 在家目录创建一个images目录  即`/home/images`
`mkdir /home/images`
- 再创建一个conf目录
`mkdir /home/conf`
- 创建并打开一个nginx的配置文件
`vim /home/conf/img_server_nginx.conf`
- 编辑配置
```shell
server {
	listen 8000;
	# sever_name 可以同时配置多个
	server_name ip地址 域名;

	location /images/ {
	# root是将images映射到/home/images/目录下，也就是去该目录下查找资源
    root  /home/;
    # autoindex on 打开浏览功能
    autoindex on;
	}  

}
```
- 修改用户访问权限
  `chmod 777 -R /home/images/`

- 重启nginx服务
  `systemctl restart nginx`或`nginx -s reload`

- 测试(通过scp远程上传图片测试)
  `scp ./avtor.jpg  用户名@ip地址:/home/images`

## 特别提示: 记得要打开网络安全组端口哦(我上面用的8000)

- 打开网址
	- [IP访问]ip地址:8000/images/mooskd.jpg
	- [域名访问，顺便将买的域名用起来]http://img.mededream.com:8000/images/mooskd.jpg
	
- 效果如下

![nginx图片服务器](../res/nginx图片服务器实力.png)
