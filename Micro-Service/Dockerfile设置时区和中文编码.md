### Dockerfile设置时区和中文编码



##### 设置时区

```
...

#定义时区参数
ENV TZ=Asia/Shanghai

#设置时区
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo '$TZ' > /etc/timezone

...
```

##### 设置中文编码

```
...

# 中文支持
RUN yum -y install kde-l10n-Chinese
RUN yum -y install glibc-common
RUN localedef -c -f UTF-8 -i zh_CN zh_CN.utf8
# 设置编码
ENV LC_ALL zh_CN.UTF-8

...
```



