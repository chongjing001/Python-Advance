#### Docker镜像缩容-多阶段构建Dockerfile

##### 第一阶段：构建应用

```dockerfile
# 第一阶段：构建应用
FROM python:3.12-slim as builder

WORKDIR /app

# 如果项目中使用mysqlclinet 作为mysql连接引擎 
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```
- `gcc`: C 编译器，用于编译 `mysqlclient`
- `python3-dev`: Python 开发头文件，用于编译 Python 扩展模块
- `default-libmysqlclient-dev`: 适用于基于 Debian 的镜像）：MySQL 客户端库的默认版本
- `pkg-config`: 用于管理编译时依赖的工具，`mysqlclient` 需要它来查找 MySQL 客户端库的位置
- **`--user`**：将包安装到用户主目录下的特定目录中，通常是 `~/.local/lib/pythonX.X/site-packages`（`X.X` 是 Python 版本号）。

#####  第二阶段：生成最终镜像

```dockerfile
FROM python:3.12-slim
ENV TZ Asia/Shanghai
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . /app

EXPOSE 80
EXPOSE 7000

ENV PATH=/root/.local/bin:$PATH

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers", "1"]
```

##### Dockerfile 整合如下

```dockerfile
# 第一阶段：构建应用
FROM python:3.12-slim as builder

WORKDIR /app

# 如果项目中使用mysqlclinet 作为mysql连接引擎 
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

FROM python:3.12-slim
ENV TZ Asia/Shanghai
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . /app

EXPOSE 80
EXPOSE 7000

ENV PATH=/root/.local/bin:$PATH

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000", "--workers", "1"]
```





