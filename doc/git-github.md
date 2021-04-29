## **git/github----协作开发**
----By Luo, 2021.4.5  

#### **----------------开源项目获取--------------**   
1. 安装git软件，建立远端github账户。首次运行git需配置用户信息（用户名和邮箱，可任意设置）。示例如下：
$ git config --global user.name "xin luo"
$ git config --global user.email xinluo@example.com
2. fork开源项目到个人账户。
3. 在本地新建git 仓库。
$ git init
4. 添加远端库，即与个人远端库建立链接。其中name为远端名，一般用origin, <url>为远端库代码链接。
$ git remote add <name> <url>
具体示例如下，
$ git remote add origin https://github.com/xxxx/aaa.git
可以检查是否与个人远端库建立连接。
$ git remote -v
5. 拉取远端库到本地并与本地代码合并（前一个main为远端分支名，后一个main为本地分支名）：
$ git pull origin main:main

#### **----------------独立项目开发--------------**
1. 修改代码后添加修改到暂存区，‘.’表示所有修改。
$ git add .
2. 提交修改到本地仓库。
$ git commit -m &lt;message&gt;
具体示例：
$ git commit -m ‘修复了a代码bug’
3. 提交最新版本到个人远端库,其中origin是个人远端库名（前一个main为个人远端库主分支，后一个main为个人本地分支名），push到个人github账户需要输入github账号密码（https 
访问），或者配置ssh公钥（ssh访问）。
$ git push origin main:main

#### **----------------开源项目代码提交--------------**  
独立项目开发期间，开源项目也在实时更新。对项目修改进行提交前首先要将个人开发版本与开源项目最新版本进行合并。
1. 建立与fork上游库的连接。&lt;url&gt; 为上游库代码链接，即开源项目源地址。
$ git remote add upstream &lt;url&gt;
检查是否与远端建立连接，此时你将看到个人本地库既与个人远端又与上游远端库相连。
$ git remote -v
2. 拉取上游库最新版本到本地并与个人开发版本进行合并。
$ git pull upstream
3. 将合并版本推到个人远端库。
$ git push origin main
3. 在个人github上fork的项目中新建pull requests，提交代码并申请开源项目合并。
4. 等待更改代码审核。

----------------练习---------------  
fork开源项目：<https://github.com/xinluo2018/landsat578-water>
对项目下hello_git.py文件进行更改并提交。
