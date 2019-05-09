#### 介绍一下Python3 创建环境的命令（超简单）
在终端中输入python/python3 或其他只要能进入Python环境即可
![](https://img-blog.csdnimg.cn/20190411003103630.png)
**上面就是确认一下进入的是Python3环境，记得要退出**
***
**然后一条命令创建一个纯净的Python环境**
***
helloenv 为环境名称
```shell
python3.6 -m venv helloenv

```
>执行上面命令时，有可能你没有安装venv相关工具，它会提示你安装
>你就按照它给出的命令安装一下
>**最后在执行一下 python3.6 -m venv helloenv 就能创建环境了**
### Tips
- 忘了说了，该命令创建的环境默认就在当前目录里
- **激活环境略～～**
****

**----------------------分割线++++感觉下面写的就是狗屎，就看上面就行了-----------**

#### 安装
- windows: pip3 install virtualenvwrapper-win
 - linux/mac: pip install virtualenvwrapper
#### 虚拟环境相关操作
 - 1）创建虚拟环境：
      virtualenv (虚拟环境名称)
 - 2）退出当前虚拟环境
      deactivate
-  3)直接进入虚拟环境中
      workon my_env 
   通过 pip insatll django==2.1 安装django
 - 4)删除某个虚拟环境
      rmvirtualenv my_env
-  5)列出所有虚拟环境
      lsvirtualenv
-  6)进入到虚拟环境所在目录
      cdvirtualenv my_env
#### 三、修改虚拟环境目录
   我都电脑->右键->属性->高级系统设置->环境变量
   更改WORKON_HOME的值为指定路径

#### 四、创建虚拟环境时候指定python版本
   在使用mkvirtualenv的时候，可以指定 --python的参数来指定具体的python路径
  例：  mkvirtualenv --python==D:\python37\python3.exe my_eny