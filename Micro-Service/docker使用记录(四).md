##### docker 修改已有镜像

- 先使用镜像启动容器
  
    `docker run -d -p 8100:80 hello:v-1.0`

- 进入容器
  
    `docker exec -it <name> bash`

- 编辑需要修改的文件，第一次需要安装编辑软件
  
    `apt-get update`更新软件源
  
    `apt-get install vim` 安装vim

- 修改`app.py`文件
  
  `vim app.py`

```python
from flask import Flask

# 获取方式对象，(就随意)命名为app
app = Flask(__name__)
# 使用app绑定路由
@app.route('/')
def hello():
    # 页面内容
    # 添加新内容
    html = '<h1>Hello Docker</h1><p>修改内容</p>'

    return html

# 启动
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=80)
```

- `exit`退出容器；`docker restart <name>`重启容器

- 访问`ip:port`可以发现页面已经更新

##### 镜像上传和下载

可以考虑把 image 文件分享到网上，让其他人使用

首先，去  [hub.docker.com](https://hub.docker.com/)  或  [cloud.docker.com](https://cloud.docker.com/)  注册一个账户

建一个仓库用于存储镜像

用下面的命令登录

`docker login` 输入后会提示输入用户名和密码

登录成功后会提示`Login Succeeded`

**镜像推送**

镜像打包

`docker image tag [imageName] [username]/[repository]:[tag]`

示例:`docker image tag hello:v-1.0 chongjing/hello:v-1.0`

镜像推送

`docker image push [username]/[repository]:[tag]`

示例:`docker image push chongjing001/hello:v-1.0`

![docker记录](https://i.loli.net/2019/05/31/5cf0cf99f0b8e95330.png)
