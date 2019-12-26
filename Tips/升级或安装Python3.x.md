### 升级或安装Python3.x

#### 安装依赖库

- `centos`

```
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel libdb4-devel libpcap-devel xz-devel libffi-devel
```


- `ubunut`
  
  - 可以直接使用`apt`安装
  - 源码安装可能需要
  
  ```
  sudo apt-get install libffi-devel
  ```
  
  

#### 下载`Python`源码

```
https://www.python.org/downloads/source/
```

或者

```
https://www.python.org/ftp/python/
```
- 找到你需要的版本
- 使用`wget`下载

例如：**3.7.4**

```
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4rc2.tgz
```

#### 解压

```
tar zxvf Python-3.7.4rc2.tgz
```

#### 编译

进入目录

`cd Python-3.7.4`

里面一般有一个`README.rst`文件，也介绍了安装方式

- 执行配置(`configure shell`脚本)生成`Makefile`（构建文件）

  ```
  ./configure --prefix=/usr/local/python37 --enable-optimizations --with-ssl
  ```
> 如果提示没有`c`的环境，请安装
>
> ```
> sudo apt-get install gcc
> ```

- 构建和安装

  **不是`root`用户加上`sudo`,升级的话建议直接切换`root`**

  `make && make install`

- 配置`PATH`环境变量
  - `vim /etc/profile`不是`root`用户加`sudo`
  - 加入`export PATH=$PATH:/usr/local/python37/bin`
  - 激活`source /etc/profile`
  
- 注册软连接(不是必须的)

```
ln -s /usr/local/python37/bin/python3 /usr/bin/python3
```

#### 测试

```
# 注册了软连接
python3 --version

# 没有注册软连接的话
pyhton3.x.x --version

```





#### 对于`pyhton3 -m venv venv`

> 出现`Error: Command '['/home/tj001/env/ls_env/bin/python3.7', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.`

这是在虚拟机上遇到的情况

不知是不是`pip`版本过高导致的

- 创建时加上`--without-pip`就不装`pip`
  - 示例`python3 -m venv venv --without-pip`
- 激活环境`source venv/bin/activate`
- 安装`pip`
  - `curl https://bootstrap.pypa.io/get-pip.py | python`
- 完成

