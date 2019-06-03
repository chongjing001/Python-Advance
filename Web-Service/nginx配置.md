##### nginx主配置文件整体结构

![5cf4e29f1dcbc19547](https://i.loli.net/2019/06/03/5cf4e29f1dcbc19547.png)

---

- 1.全局快 - 影响nginx全局，通常包括以下几个部分
  
  - 配置运行nginx服务器用户(组)
  - worker process进程数
  - nginx进程PID存放路径
  - 错误日志的存放路径
  - 配置文件的引入

- events块 - 主要影响nginx服务器与用户网络连接
  
  - 设置网络的序列化
  - 是否允许同时连接多个网络连接
  - 事件驱动模型的选择
  - 最大连接数的配置

- http块
  
  - 定义MIMI-type
  - 自定义服务日志
  - 允许sendfile方式传输
  - 连接超时时间设置
  - 单连接请求数上限

- server块
  
  - 配置网络监听
  - 基于名称的虚拟主机配置
  - 基于IP的虚拟主机配置

- location块
  
  - location配置
  - 请求根目录配置
  - 更改location的URI
  - 网站默认首页配置

```shell
# ----------------------------全局快---------------------------
# 用户
user root;
# 工作进程数(建议跟cpu的核数一直,auto表示自动检查)
worker_process auto;

#全局错误日志及PID文件
error_log /var/log/nginx/error.log;
pid    /var/run/nginx.pid;
# -------------------------------------------------------------

# ----------------------------events块--------------------------
events{
    # epoll是多路复用IO(I/O Multiplexing)中的一种方式,
    #仅用于linux2.6以上内核,可以大大提高nginx的性能
    use epoll;
    # 单个后台worker process进程的最大并发链接数
    worker_connections 1024;
    # 并发总数是 worker_processes 和 worker_connections 的乘积
    # 即 max_clients = worker_processes * worker_connections

}

# --------------------------------------------------------------


# -----------------------http服务配置---------------------------------------
http{
    # ------------------------http全局快------------------------
    # 设定mime类型,类型由mime.type文件定义
    include    /etc/nginx/mime.types;
    default_type application/octet-stream;

    # 设定日志格式
    access_log  /var/log/nginx/access.log;

    # 开启高效文件传输模式
    # sendfile 指令指定 nginx 是否调用 sendfile 函数（zero copy 方式）来输出文件，对于普通应用，
      # 必须设为 on,如果用来进行下载等应用磁盘IO重负载应用，可设置为 off，以平衡磁盘与网络I/O处理速度，降低系统的uptime.
      sendfile on;

      # 用sendfile传输文件时有利于改善性能
      tcp_nopush on;

      # 客服端连接超时时间
      keepalive_timeout 65;

      # 禁用Nagle来解决交互性问题
      tcp_nodelay on;

      #开启gzip压缩
    gzip on;
    gzip_disable "MSIE [1-6]\.(?!.*SV1)";

    #设定请求缓冲
    client_header_buffer_size  1k;
    large_client_header_buffers 4 4k;

     # 包含其他配置文件
    include /etc/nginx/conf.d/*.conf;
    # 包含项目的nginx配置文件
    include /home/conf/*.conf;


    # 设定负载均衡的服务器列表
    upstream 域名 {
    # weigth参数表示权值，权值越高被分配到的几率越大
    server 192.168.8.1:80 weight=5;
    server 192.168.8.2:80 weight=1;
    server 192.168.8.3:80 weight=6;
        }

    # ------------------------http全局快---------------------------

    # ------------------------server-------------------------------
    server {
        # 监听端口
        listen 80;

        # 定义ip或域名访问(可以跟多个,空格隔开,支持正则匹配)
        server_name ip 域名;

        # 定义服务器的默认网站根目录位置
        root /home;

        #设定本虚拟主机的访问日志
        access_log  logs/nginx.access.log  main;


    }

    # ------------------------server-------------------------------



}
# -----------------------http服务配置------------------------------------------
```
