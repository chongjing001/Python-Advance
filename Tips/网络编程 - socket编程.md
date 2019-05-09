---
title: "网络编程-socket"
categories:
- python
tags:
- 网络编程
- socket
---
#### 一、服务器套接字
- socket又叫套接字，指的就是实现通信过程的两个端。等待请求的一端叫服务端套接字，发送请求的一端叫客户端套接字

- python中提供了socket模块来支持socket编程
```python
import socket

# ==========服务器套接字=============
# 1.创建套接字对象
"""
socket(family, type)
family - 设置ip类型   AF_INET(默认值) - ipv4   AF_INET6 - ipv6
type - 设置传输类型  SOCK_STREAM(默认值) - tcp   SOCK_DGRAM - udp
"""
# 创建一个基于ipv4和TCP的套接字对象
server = socket.socket()

# 2.绑定ip地址和端口
"""
bind((ip地址, 端口号))
ip地址 - 服务器对应的计算机的ip地址，字符串
端口号 - 用来区分计算机上不同服务; 是一个数字，范围是0~65535;
        但是其中1024以下的是著名端口，用来表示一个特殊的服务,一般不要用;
        同一时间一个端口只能对应一个服务
"""
server.bind(('10.7.187.149', 8081))

# 3.开始监听
"""
listen(最大监听数) 
最大监听数 - 用来设置当前服务器一次可以处理多少个请求
"""
server.listen(100)
print('开始监听')

# 4. 让服务一直处于启动状态
while True:
    # 5.接收客户端发送的请求，返回建立的会话和客户端地址；
    # 注意，这段代码会阻塞线程(程序运行到这儿会停下来，直到有客户端给当前服务器发送请求为止)
    conversation, addr = server.accept()
    print('接收到请求:', addr)

    # 6.接收消息(客户端发送给服务器的消息)
    """
    recv(缓存大小)  - 获取客户端给服务器发送的数据，返回值是二进制
    缓存大小 - 决定一次可以接收的数据的最大字节数
    
    这儿也会阻塞线程，直到客户端发送了消息才会接着往后执行
    """
    re_data = conversation.recv(1024)
    print('======')
    print(re_data.decode('utf-8'))

    # 7.发送数据(服务器给客户端发送数据)
    """
    send(数据) - 将指定的数据发送给客户端
    数据 - 要求是二进制
    
    字符串(str)转二进制(bytes):
    a.bytes(字符串, 'utf-8')
    b.字符串.encode('utf-8')
    
    二进制转字符串
    a.str(二进制数据, 'utf-8')
    b.二进制.decode('utf-8')
    """
    # message = 'HTTP/1.1 200 OK\r\n\r\n <html><<head><meta charset="utf-8" /><title>表格</title></head><body>你好!</body></html>'
    message = '你好！！！'
    # conversation.send(bytes(message, encoding='utf-8'))
    conversation.send(message.encode(encoding='utf-8'))

    # 8.关闭连接
    conversation.close()
```
二、客户端套接字
```python
import socket

# 1.创建套接字对象
client = socket.socket()

# 2.连接服务器
"""
connect((ip, 端口))
"""
client.connect(('172.21.203.2', 8088))

# 3.发送消息
message = input('>>')
client.send(message.encode('utf-8'))

# 4.接收消息
re_data = client.recv(1024)
print(re_data.decode('utf-8'))
```
#### 三、网络请求
```python
import requests

"""
python中去做http请求，需要使用一个第三方库: requests
"""
"""
get(url, 参数字典) - 返回响应
"""
# 1.向服务器发送get请求
# a.手动拼接url
# url = 'https://www.apiopen.top/satinApi?type=1&page=1'
# response = requests.get(url)
# print(response)

# b.自动拼接url
url = 'https://www.apiopen.top/satinApi'
response = requests.get(url, {'type': 1, 'page': 1})
print(response)

# 2.获取响应头
header = response.headers
print(header)

# 3.获取响应体
"""
a.获取二进制格式的响应体
"""
content = response.content
print(type(content))

"""
b.获取json格式响应体 - 自动将json数据转换成python
"""
json = response.json()
print(type(json))

"""
c.获取字符串格式的响应体
"""
text = response.text
print(type(text))


# 应用：下载网络图片
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1543395098&di=2a5bbaa5600097b050ba69a688672de9&src=http://p0.qhimgs4.com/t0112e7ebfdef7f923d.jpg'
response = requests.get(url)
image_data = response.content
with open('王也.jpg', 'wb') as f:
    f.write(image_data)
```