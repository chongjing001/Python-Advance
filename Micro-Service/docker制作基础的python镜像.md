#### 拉取基础镜像
- 以Ubuntu24示例

`docker pull ubuntu:24.04`

- 启动

`docker run -it -d --name ubuntu24 ubuntu:24.04`

#### 进入docker

docker exec -it ubuntu24 /bin/bash

#### 更新依赖

`apt update`

`apt full-upgrade`

#### 安装pip

- 会自动安装python3.11.7

`apt install pip`

#### 支持中文

```shell
1. apt-get install language-pack-zh-hans
2. locale-gen zh_CN.UTF-8
3. echo "export LC_ALL=zh_CN.UTF-8">> /etc/profile
4. source /etc/profile
```



#### 其他

如果项目中使用`mysqlclinet` 作为`mysql`连接引擎，需要安装c扩展/依赖等

`apt install python3-dev default-libmysqlclient-dev build-essential pkg-config`

使用`pymysql`则不需要



#### 提交镜像

`docker commit -a'作者'  -m '描述' ubuntu24 镜像名:标签`

- -a 和 -m 可省略







