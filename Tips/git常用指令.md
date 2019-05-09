---
title: "git常用指令"
categories:
- git
tags:

top: true
---


# git常用指令  
## 1.基本指令
`git init ` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ——  新建git仓库      
`git add 文件/文件夹` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ——  将文件添加到缓存区中  
`git add -A` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --- 添加所有内容到缓存区中
`git stutas` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;———    查看git状态  
`git commit -m  ‘提交信息’`  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;——  将缓存区中的内容全部提交到git本地仓库中  


`git log`   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;——-    查看提交日志  

`git reset  - - hard   HEAD`  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;——   让工作目录中的内容和仓库中的内容保持一致  
`git reset  --hard HEAD^`   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;——  回到上一个版本  
`git  reset  - - hard 版本号`  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;——  回到指定的版本  
`git checkout  - -  文件名`  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ——  从暂存区中恢复工作目录中的内容(让工作区中的指定文件，回到上次提交的时候的状态)  

`git clone <url> ` - 将服务器上的项目(仓库)克隆 (使用https地址需要输入密码，使用ssh地址需要添加公钥)  

`git remote add origin 地址`  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;----- 关联远程仓库(只需要关联一次)

``git push [-u] origin master``  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;----- 提交(-u在第一次提交分之的时候才用)  

## 2.分之管理  
创建仓库会默认给我们创建一个master分之,这个分之一般作为提交和发布分之;开发一般会自己创建一个develop分之，用来开发和测试;多人协作的时候还可能根据不同的人或者(不同的功能)创建不同的分之，用来独立开发  

常见分之： master(主要是合并develop), develop(主要合并下面的其他分支), 功能/人员分之(开发)  

`git branch [-a]`   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		- 查看分之   
`git branch 分之名`		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 创建分之   
`git checkout   分支名`		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-   切换分之      
`git checkout -b 分之名`		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	- 切换并创建新的分之   
`git diff	分之1  分之2`		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 查看两个分之之间的差异  
`git merge 分之名	`			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 让当前分之和指定分之进行合并     

注意: 切换分之、push、pull，这些操作前要保证工作区是clean  

怎么避免冲突：  不要发生多个分之对同一个文件在同一个版本下进行修改(和同伴确认和商量)



