### Docker 制作基础镜像并发布



#### 1.最基础的Linux系统busybox(瑞士军刀)

[参考这篇文章](https://blog.csdn.net/liumiaocn/article/details/80458663)



#### 2. centos的基础镜像

[docker官网获取你所需要的centos版本](https://hub.docker.com/_/centos?tab=tags)



> 下面以centos7示例

> pull镜像

`docker pull centos:7`

> 生成容器并进入镜像

`docker run --name  centos7  docker.io/centos:7 bash`

- `--name`: 对容器命名

> 定制自己需要的服务
>
> 以python3.7 和nginx为例

需要安装的工具`wget`、`make`、`gcc`

```
yum -y install wget make gcc
```

**python3源码安装**

```
1. wget 下载源码
2. configure 配置
3. make && make install  测试并编译
4. ln -s 注册软连接
```

[参考](https://blog.csdn.net/qq_42874994/article/details/103723847)

**nginx源码安装同理**

[参考](https://www.cnblogs.com/connect/p/nginx-install-src.html)



> 删除下载的文件、安装工具

> 提交修改的镜像

`docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]] `
```
OPTIONS说明
-a : 提交的镜像作者
-m : 提交时的说明文字
-p : 在commit时，将容器暂停
CONTAINER  : 容器(一般用容器ID)
REPOSITORY[:TAG] 打标签
```

> 示例：`docker commit -m 'centos7 python3 + nginx' 容器ID centos7:base` 



#### 3.发布到自己docker hub仓库

> docker login 登陆

> 镜像打包

`docker image tag [imageName] [username]/[repository]:[tag]`

示例:`docker image tag centos7:base chongjing001/centos7:base`

> 镜像推送

`docker image push [username]/[repository]:[tag]`

示例:`docker image push chongjing001/centos7:base`
