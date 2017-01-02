# 山东省ACM大学生程序设计竞赛web服务使用说明

## 0 项目介绍
> 面向ACM竞赛裁判、选手、赛场工作人员的综合web服务
>
> 提供pc2(Programming Contest Control System)中没有的打印代码、赛场指令等技术支持
>
> 功能清单:
> * [裁判端]配置比赛,导入参赛队伍名单,导出获奖信息;
> * [选手端]排行榜,打印代码服务;
> * [赛场工作人员端]气球状态,大屏幕倒计时及赛场指令,大屏幕滚动排行榜。
>
## 1 环境搭建
#### 1.1 安装django
> sudo pip install django
#### 1.2 安装mysql
> sudo apt-get install mysql-server
>
> sudo apt-get install libmysqld-dev
>
> sudo apt-get install python-dev
>
> sudo pip install mysql-python
#### 1.3 安装pc^2
> http://pc2.ecs.csus.edu/secret.940-1220.html
## 2 环境配置
#### 2.1 配置数据库
> 在sdacm/sdacm/settings.py下的DATABASES设置数据库选项
>
> 使用django的ORM机制建立数据库表:
>
> * python manage.py syncdb
>
> Django 1.7.1及以上的版本需要用以下命令
> * python manage.py makemigrations
> * python manage.py migrate
#### 2.2 配置比赛选项
> 在sdacm/config.py下设置比赛选项, 包括:
> * pc2的路径
> * 比赛时间
> * 比赛奖项安排
> * 比赛气球安排
> * 打印机配置(需要与系统设置的打印机名称一致)
#### 2.3 初始化数据
> 首先需要启动pc2board, 以生成results.xml
>
> 将比赛队伍信息按照user.txt格式准备好, 打开http://localhost/master，用django的管理员账户登录，选择“导入数据”，将准备好的队伍信息表上传
>
> http://localhost/admin，用django的管理员账户登录，增加气球端账户ballonserver, 此账户用于登陆http://localhost/ballon


#### 本程序由dongchen版权所有,如有疑问、报bug、参与开发,可联系QQ:278364079
