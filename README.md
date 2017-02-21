# MutualFundAnalysis
MutualFund data Analysis service

### 初始安装库:

    sudo easy_install pip

    sudo pip install Django==1.10.5

    django-admin.py startproject MutualFundAnalysis

    sudo pip install MySQL-python

    sudo pip install requests

    sudo pip install django-crontab

scrapy:

    brew install python
    xcode-select --install
    sudo pip install scrapy

beautifulsoup:

    sudo pip install beautifulsoup4

安装virtualenv:

sudo pip install virtualenv

virtualenv --no-site-packages venv

source venv/bin/activate

使用deactivate命令退出当前的venv环境。

http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000

### 项目运行:

python manage.py runserver

python manage.py runserver 0.0.0.0:8000

### 项目结构:

MutualFundAnalysis: 项目的容器。

manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。

MutualFundAnalysis/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。

MutualFundAnalysis/settings.py: 该 Django 项目的设置/配置。

MutualFundAnalysis/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。

MutualFundAnalysis/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。



添加model:

python manage.py startapp Model



安装MySQL-python:

vi ~/.bash_profile

然后添加:

export PATH=${PATH}:/usr/local/mysql/bin

使更改生效:

source ~/.bash_profile

### 创建数据库:

CREATE DATABASE IF NOT EXISTS mutualfund default charset utf8 COLLATE utf8_general_ci;

python manage.py migrate

注意:syncdb is deprecated because of the migration system.
在Django 1.9及未来的版本种使用migrate代替syscdb.

新的表没有创建:

(1146, "Table 'test.testmodel_test' doesn't exist")

重新运行:python manage.py migrate 报错:
Your models have changes that are not yet reflected in a migration, and so won't be applied.

Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.

重新执行两行命令:

python manage.py makemigrations

python manage.py migrate

数据创建成功:
Operations to perform:
  Apply all migrations: Model, admin, auth, contenttypes, sessions
Running migrations:
  Applying Model.0001_initial... OK

重新运行服务:

数据添加成功！


引入:
from django.core.context_processors import csrf

报错:

ImportError: No module named context_processors

解决方案:

from django.views.decorators import csrf


### 管理后台:

1、创建超级用户:

python manage.py createsuperuser

输入用户名密码
本系统创建为: admin / admin123

2、访问:
http://127.0.0.1:8000/admin/

admin/admin123

uwsgi:

1、uwsgi --http :8001 --wsgi-file test.py

2、配置nginx

3、uwsgi --ini /etc/uwsgi9090.ini &
  /usr/local/nginx/sbin/nginx


### 定时任务

每次添加或修改定时任务后更新:

python manage.py crontab add

移除所有任务:

python manage.py crontab remove

查看已经激活的任务使用:

python manage.py crontab show