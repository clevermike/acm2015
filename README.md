# 山东省第六届ACM大学生程序设计竞赛web服务使用说明
 
## 1、安装apache2
### sudo apt-get install apache2
## 2、安装mysql-server
### sudo apt-get install mysql-server
## 3、安装django
### sudo pip install django
## 4、安装mod-wsgi
### sudo apt-get install libapache2-mod-wsgi
## 5、安装mysql-python
### sudo apt-get install libmysqld-dev
### sudo pip install mysql-python
## 6、配置数据库
### create database acm2015 default character set utf8
### python manage.py syncdb
## 7、配置apache
### vim /etc/apache2/mods-available/wsgi.conf
 `WSGIPythonPath /var/www/acm2015`
### vim /etc/apache2/sites-available/000-default.conf
 `WSGIScriptAlias / "/var/www/acm2015/acm2015/wsgi.py"
	Alias /static/ /var/www/acm2015/static/
	<Directory /var/www/acm2015/static/>
		Order deny,allow
		Allow from all
	</Directory>
	<Directory " /var/www/acm2015/acm2015">
		Order Deny,Allow
		Allow from all
	</Directory>`
## 8、比赛配置
### 将acm2015放在/var/www/下
### 配置settings.py
### 启动pc2board并登录
## 9、启动apache
### sudo service apache2 start
## 10、导入数据文件
### http://localhost/master，用django的管理员账户登录，选择“导入数据”，选择user.txt并将其上传
## 11、配置其他用户
### http://localhost/admin，用django的管理员账户登录，增加气球端账户ballonserver
## 12、启动封榜脚本
### python scripts/FileSender.py

# 本程序采用django框架，包含排行榜、打印服务、大屏幕倒计时、大屏幕滚动榜、气球端、后台数据导入导出等功能
