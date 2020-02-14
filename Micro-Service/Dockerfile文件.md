### Dockerfile



| 常用命令   | 说明                                                        |
| ---------- | ----------------------------------------------------------- |
| FROM       | 指定基础镜像                                                |
| MAINTAINER | 指定维护者信息                                              |
| RUN        | 执行命令                                                    |
| ADD        | 拷贝文件，如果是URL或压缩包，会自动下载和解压               |
| COPY       | 拷贝文件或目录到镜像中，用法同ADD，只是不支持自动下载和解压 |
| WORKDIR    | 设置当前工作目录                                            |
| VOLUME     | 设置挂载目录                                                |
| EXPOSE     | 打开的端口                                                  |
| ENV        | 设置环境变量                                                |
| CMD        | 容器启动后要执行的事                                        |



##### FROM

- 指明基础镜像

```
FROM yourimgagename
```

##### MAINTAINER

- 指明镜像维护着及其联系方式（一般是邮箱地址）

```
MAINTAINER username <email>
```

##### RUN

- 构建镜像时运行的`Shell`命令

```
RUN ["apt", "install", "vim"]
或
RUN apt install vim
```

##### CMD

- 启动容器时执行的Shell命令

```
CMD ["./start.sh"]
或
CMD /start.sh
```

##### ENTRYPOINT

- 启动容器时执行的`Shell`命令，同`CMD`类似，只是由`ENTRYPOINT`启动的程序**不会被docker run命令行指定的参数所覆盖**，而且，**这些命令行参数会被当作参数传递给ENTRYPOINT指定指定的程序**

```
ENTRYPOINT ["/bin/bash", "-C", "/start.sh"]
或
ENTRYPOINT /bin/bash -C '/start.sh'
```

##### ADD/COPY

- 拷贝文件或目录到镜像中

```
ADD MyProject.tar.gz /home/MyProject
```

##### 

##### EXPOSE

- 声明容器运行的服务端口

```
EXPOSE 80 443
```

##### ENV

- 设置环境内环境变量

```
ENV MYSQL_ROOT_PASSWORD 123456
```

##### ARG

- 在构建镜像时，指定一些参数

