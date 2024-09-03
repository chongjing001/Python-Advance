### docker制作达梦数据库驱动的Python镜像记录

> **使用`Sqlalchemy` ORM 操作达梦**

**[镜像中安装`Python`参考上一篇](./docker制作基础的python镜像.md)**



#### 下载DM8安装包

##### 版本选择

[官网](https://eco.dameng.com/download/)
![](../res/Dm8downloadpage.jpg)

`Linux`安装包只有 `rhel6/7`这里选择7下载 

> 2024 8 月记

**亲测：红帽7可以在Ubuntu镜像中安装**

##### 解压并获取安装文件
**建议在`windows`下解压并提取安装文件后copy至容器中**
![](../res/dm8zipiso.jpg)

**`windows`下可直接双击挂载iso**
![](../res/Dm8install.jpg)

- copy至docker容器中
`docker cp DMInstall.bin 容器名:目录`

#### 准备工作
##### 创建`dmdba` 用户
> 没有dmdba用户安装程序不能运行。。。
```shell
# 创建用户所在的组
groupadd dinstall -g 2001

# 创建用户
useradd  -G dinstall -m -d /home/dmdba -s /bin/bash -u 2001 dmdba

```

#### 执行安装命令

`./DMInstall.bin -i`

**输出:**

```
root@1abcc8c919ce:/# ./DMInstall.bin -i                        
安装语言:                                                          
[1]: 简体中文                                                      
[2]: English                                                   
请选择安装语言 [1]:1                                                  
解压安装程序.........                                                
硬件架构校验通过！                                                      
欢迎使用达梦数据库安装程序                                                  
                                                               
是否输入Key文件路径? (Y/y:是 N/n:否) [Y/y]:n                             
                                                               
是否设置时区? (Y/y:是 N/n:否) [Y/y]:n                                  
                                                               
安装类型:                                                          
1 典型安装                                                         
2 服务器                                                          
3 客户端                                                          
4 自定义                                                          
请选择安装类型的数字序号 [1 典型安装]:4                                        
1 服务器组件                                                        
2 客户端组件                                                        
  2.1 DM管理工具                                                   
  2.2 DM性能监视工具                                                 
  2.3 DM数据迁移工具                                                 
  2.4 DM控制台工具                                                  
  2.5 DM审计分析工具                                                 
  2.6 SQL交互式查询工具                                               
3 驱动                                                           
4 用户手册                                                         
5 数据库服务                                                        
  5.1 实时审计服务                                                   
  5.2 作业服务                                                     
  5.3 实例监控服务                                                   
  5.4 辅助插件服务                                                   
请选择安装组件的序号 (使用空格间隔) [1 2 3 4 5]:3                              
所需空间: 776M                                                     
                                                               
请选择安装目录 [/opt/dmdbms]:                                         
可用空间: 935G                                                     
是否确认安装路径(/opt/dmdbms)? (Y/y:是 N/n:否)  [Y/y]:y                  
                                                               
安装前小结                                                          
安装位置: /opt/dmdbms                                              
所需空间: 776M                                                     
可用空间: 935G                                                     
版本信息:                                                          
有效日期:                                                          
安装类型: 自定义                                                      
是否确认安装? (Y/y:是 N/n:否):y                                        
2024-09-03 13:55:58                                            
[INFO] 安装达梦数据库...                                              
2024-09-03 13:55:58                                            
[INFO] 安装 基础 模块...                                             
2024-09-03 13:56:01                                            
[INFO] 安装 驱动 模块...                                             
2024-09-03 13:56:03                                            
[INFO] 移动日志文件。                                                 
2024-09-03 13:56:03                                            
[INFO] 安装达梦数据库完成。                                              
                                                               
安装结束                                                           
```

#### 设置系统变量

- `/etc/environment` 增加以下内容
```shell
DM_HOME="/opt/dmdbms"
LD_LIBRARY_PATH="/opt/dmdbms/bin"
```
- `/root/.bashrc` 增加以下内容
```shell
# Load system-wide environment variables 
. /etc/environment
```

- 数据库安装**bin**目录下拷贝`libcrypto.so`到`/usr/lib /usr/lib64`
  - 我这里是`/opt/dmdbms/bin`

```shell
cp /opt/dmdbms/bin/libcrypto.so /usr/lib
cp /opt/dmdbms/bin/libcrypto.so /usr/lib64
```

#### 安装`sqlalchemy-dm`

##### 初始化虚拟镜像

`python3 -m venv venv`

如果没有安装`python3-venv` 根据提示安装

- 激活虚拟环境
  - `source venv/bin/activate`

- 安装 `setuptools`
  - `pip install setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple`

##### 安装dmPython

`pip install dmPython -i https://pypi.tuna.tsinghua.edu.cn/simple`

##### sqlalchemy-dm

- 先安装`sqlalchemy`
  - `pip install sqlalchemy -i https://pypi.tuna.tsinghua.edu.cn/simple`

- 进入`Python`驱动目录(sqlalchemy2.0.0)
  - `cd /opt/dmdbms/drivers/python/sqlalchemy2.0.0/`
  
  - 目前`sqlalchemy model`层中自增主键在插入时会出现错误: `[CODE:-2106]无效的表或视图名`
  
    处理办法，修改 sqlalchemy_dm 目录下`base.py`源码
  
    ```python
    # 将base.py源码中 _set_autoinc_col_from_lastrowid方法中 table.name改为table.fullname就可以了
    
    # statement = "select {} from {} where rowid = {}".format(autoinc_col.name, table.name, lastrowid)
    # 改成
    statement = "select {} from {} where rowid = {}".format(autoinc_col.name, table.fullname, lastrowid)
    
    ```
  
    
  
  - 返回上一级 ` python setup.py install`

#### 测试

```python
from sqlalchemy import create_engine, Index, ForeignKey, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String

# 创建基类
Base = declarative_base()
db_schema = 'hello'


class BaseModel(Base):
    __abstract__ = True
    __table_args__ = {"schema": db_schema}


class Task(BaseModel):
    __tablename__ = 'tb_task'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    medias = relationship('TaskMedias', backref=f'task')


class TaskMedias(BaseModel):
    __tablename__ = 'tb_task_medias'
    id = Column(Integer, primary_key=True)
    guid = Column(String(50))

    task_id = Column(Integer, ForeignKey(f'{db_schema}.tb_task.id'))

    # 添加索引，达梦不支持在create table时添加索引，所以这里放在这里单独添加
    __table_args__ = (
        Index('idx_guid', 'guid', unique=True),
        {"schema": db_schema},
    )


# 创建数据库引擎
engine = create_engine(f"dm+dmPython://SYSDBA:SYSDBA@172.16.147.212:5237", echo=True)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

session.execute(text(f"CREATE SCHEMA {db_schema}"))

print(session.execute(text('SELECT SF_GET_CASE_SENSITIVE_FLAG()')).scalar())

# 创建所有表
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

t = Task(name='task1')
session.add(t)
session.commit()

query_data = session.query(Task).all()
print(query_data)

```



#### 删除安装文件`DMInstall.bin`

