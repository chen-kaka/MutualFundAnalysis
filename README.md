# MutualFundAnalysis
MutualFund data Analysis service


create python django project:

sudo easy_install pip

sudo pip install Django==1.10.5

django-admin.py startproject DjangoProj


run project:

python manage.py runserver

python manage.py runserver 0.0.0.0:8000

项目结构:

DjangoProj: 项目的容器。

manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。

DjangoProj/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。

DjangoProj/settings.py: 该 Django 项目的设置/配置。

DjangoProj/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。

DjangoProj/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。



添加model:

python manage.py startapp TestModel



安装MySQL-python:

vi ~/.bash_profile

然后添加:

export PATH=${PATH}:/usr/local/mysql/bin

使更改生效:

source ~/.bash_profile

install MySQL-python

sudo pip install MySQL-python

创建数据库:

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
  Apply all migrations: TestModel, admin, auth, contenttypes, sessions
Running migrations:
  Applying TestModel.0001_initial... OK

重新运行服务:

数据添加成功！


引入:
from django.core.context_processors import csrf

报错:

ImportError: No module named context_processors

解决方案:

from django.views.decorators import csrf


管理后台:

1、创建超级用户:

python manage.py createsuperuser

输入用户名密码
本系统创建为: admin / admin123

2、访问:
http://127.0.0.1:8000/admin/

uwsgi:

1、uwsgi --http :8001 --wsgi-file test.py

2、配置nginx

3、uwsgi --ini /etc/uwsgi9090.ini &
  /usr/local/nginx/sbin/nginx