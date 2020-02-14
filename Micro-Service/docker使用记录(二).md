#### docker 基本命令
- 查看Docker的信息和版本
显示一些相关的系统系统信息
`docker version` 或`docker info`
显示一个容器的底层具体信息
`docker inspect`

- Docker需要用户具有sudo权限,为了避免每次命令都输入`sudo`,可以把用户加入Docker用户组
`sudo usermod -aG docker $USER`

- 运行Hello-World项目来测试Docker。第一次运行时由于本地没有hello-world的镜像因此需要联网进行下载
`docker run hello-world`

- 下载镜像
`docker pull <name>`

- 运行镜像文件
`docker run <image-id>`
`docker run -p <port1>:<port2> <name>`

- 查看镜像文件
`docker image ls` 或 `docker images`

- 删除镜像文件和容器(可删除多个)
	- 删除镜像文件`docker rmi <name>`
	- 删除容器`docker rm <name>`

- 查看正在运行容器
`docker ps`

- 查看已停止运行的容器

  `docker ps -a`

- 停止运行的容器
  `docker stop <container-id>`或`docker stop <name>`

- 对于那些不会自动终止的容器，就可以用下面的方式来停止
  `docker container kill <container-id>`

- 检查一个容器文件系统的修改
  `docker diff <name>`

- 从一个Docker的仓库服务器下拉下一个镜像或仓库
  `docker pull <name>`

- 将一个镜像或者仓库推送到一个Docker的注册服务器
  `docker push <name>`

- 在Docker index中搜索一个镜像
  `docker search <name>`

- 启动/重启/停止/容器
  `docker start/restart/stop <name>`

- 镜像文件打包成文件

  `docker save -o 文件名   镜像`

  示例：

  `docker save -o myimage.tar  myimage`

- 将文件导入成镜像

  `docker load --input 文件`

  或

  `docekr load < 文件`

- 保存修改后的镜像

  `docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]] `

  >  OPTIONS说明
  >
  >  -a : 提交的镜像作者
  >
  >  -m : 提交时的说明文字
  >
  >  -p : 在commit时，将容器暂停
  >
  >  CONTAINER  : 容器
  >
  >  REPOSITORY[:TAG] 打标签







