
#### 什么是docker?
Docker是一个开源项目，诞生于2013年初，最初是dotCloud公司内部的一个业余项目。它基于Google公司推出的Go	语言实现。项目后来加入了Linux基金会，遵从了Apache2.0	协议，项目代码在GitHub上进行维护

**Docker 属于 Linux 容器的一种封装，提供简单易用的容器使用接口。它是目前最流行的 Linux 容器解决方案。**
Docker 将应用程序与该程序的依赖，打包在一个文件里面。运行这个文件，就会生成一个虚拟容器。程序在这个虚拟容器里运行，就好像在真实的物理机上运行一样。有了 Docker，就不用担心环境问题。

总体来说，Docker 的接口相当简单，用户可以方便地创建和使用容器，把自己的应用放入容器。容器还可以进行版本管理、复制、分享、修改，就像管理普通的代码一样
#### 为什么要使用docker
作为一种新兴的虚拟化方式Docker跟传统的虚拟化方式相比具有众多的优势。
首先，Docker容器的启动可以在秒级实现，这相比传统的虚拟机方式要快得多。	其次，Docker	对系统资源的利用率很高，一台主机上可以同时运行数千个Docker容器。
容器除了运行其中应用外，基本不消耗额外的系统资源，使得应用的性能很高，同时系统的开销尽量小。 传统虚拟机方式运行10个不同的应用就要起10个虚拟机，而Docker只需要启动10个隔离的应用即可。
具体说来，Docker在如下几个方面具有较大的优势

- 更快的交付和部署
	-对开发和运维（devop）人员来说，最希望的就是一次创建或配置，可以在任意地方正常运
	开发者可以使用一个标准的镜像来构建一套开发容器，开发完成之后，运维人员可以直接使用这个容器来 部署代码。Docker可以快速创建容器，快速迭代应用程序，并让整个过程全程可见，使团队中的其他成员 更容易理解应用程序是如何创建和工作的。	Docker容器很轻很快！容器的启动时间是秒级的，大量地节约 开发、测试、部署的时间
- 更高的虚拟化
	- Docker容器的运行不需要额外的hypervisor支持，它是内核级的虚拟化，因此可以实现更高的性能和效率
- 更轻松的迁移和扩展
	- Docker容器几乎可以在任意的平台上运行，包括物理机、虚拟机、公有云、私有云、个人电脑、服务器 等。	这种兼容性可以让用户把一个应用程序从一个平台直接迁移到另外一个。
- 更简单的管理
	- 使用	Docker，只需要小小的修改，就可以替代以往大量的更新工作。所有的修改都以增量的方式被分发和 更新，从而实现自动化并且高效的管理
- 更简单的管理
	- 使用Docker，只需要小小的修改，就可以替代以往大量的更新工作。所有的修改都以增量的方式被分发和 更新，从而实现自动化并且高效的管理
- 与虚拟机对比
特性 |  容器   |   虚拟机 
 ------- |   ------ | --------
启动  | 秒级 | 分钟级
硬盘使用|一般为MB|一般为GB
性能	 | 接近原生 | 弱于
系统支持量 | 单机支持上千个容器 | 一般几十个

**以上为docker从入门到实践摘取**

#### docker的三个概念
- 1.镜像(image)：类似于虚拟机中的镜像，是一个包含有文件系统的面向Docker引擎的只读模板。任何应用程序运行都需要环境，而镜像就是用来提供这种运行环境的。例如一个Ubuntu镜像就是一个包含Ubuntu操作系统环境的模板，同理在该镜像上装上Apache软件，就可以称为Apache镜像
- 2.容器(Container):类似于一个轻量级的沙盒，可以将其看作一个极简的Linux系统环境（包括root权限、进程空间、用户空间和网络空间等），以及运行在其中的应用程序。Docker引擎利用容器来运行、隔离各个应用。容器是镜像创建的应用实例，可以创建、启动、停止、删除容器，各个容器之间是是相互隔离的，互不影响。注意：镜像本身是只读的，容器从镜像启动时，Docker在镜像的上层创建一个可写层，镜像本身不变
- 3.仓库(Repository):类似于代码仓库，这里是镜像仓库，是Docker用来集中存放镜像文件的地方。注意与注册服务器（Registry）的区别：注册服务器是存放仓库的地方，一般会有多个仓库；而仓库是存放镜像的地方，一般每个仓库存放一类镜像，每个镜像利用tag进行区分，比如Ubuntu仓库存放有多个版本（12.04、14.04等）的Ubuntu镜像

#### docker三大用途
- 提供一次性的环境。比如，本地测试他人的软件、持续集成的时候提供单元测试和构建的环境
- 提供弹性的云服务。因为 Docker 容器可以随开随关，很适合动态扩容和缩容
- 组建微服务架构。通过多个容器，一台机器可以跑多个服务，因此在本机就可以模拟出微服务架构

#### docker安装
Docker 是一个开源的商业产品，有两个版本：社区版（Community Edition，缩写为 CE）和企业版（Enterprise Edition，缩写为 EE）。企业版包含了一些收费服务，个人开发者一般用不到。下面的介绍都针对社区版

- Centos 系列
	- Centos6,可以使用EPEL库安装Docker，命令如下
```shell
sudo yum install http://mirrors.yun-idc.com/epel/6/i386/epel-release-6-8.noarch.rpm
sudo yum install docker-io
```
	- Centos7，CentOS-Extras库中已带Docker，可以直接安装
	`sudo yum install docker`
	- 安装之后启动Docker服务，并让它随系统启动自动加载
	`sudo service docker start`或`systemctl start docker`
	`sudo chconfig docker on`
- Ubuntu 系列
	- Ubuntu 14.04之前的版本
```shell
sudo apt-get update
sudo apt-get install linux-image-generic-lts-raring	linux-headers-generic-lts-raring
sudo reboot  # 重启
```
	- Ubuntu14.04以上版本
```shell
sudo apt-get update
sudo apt-get install docker-ce
service docker start 或者 systemctl start docker
```
**tip：下载很慢的情况下一个更换Ubuntu软件源，提升下载速度**
- 安装Docker后，由于直接访问dockerhub下载镜像会非常缓慢，建议更换国内镜像，可以通过修改/etc/docker/daemon.js文件来做到
```shell
{
	"registry-mirrors": [
        "http://hub-mirror.c.163.com",
        "https://registry.docker-cn.com"
    ]
}
```
如果使用云服务器（如：阿里云），通常云服务器提供商会提供默认的镜像服务器，并不需要手动进行指定
