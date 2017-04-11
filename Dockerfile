FROM daocloud.io/django:1.7.1-python2
MAINTAINER chen_kaka <chen-kaka@163.com>

RUN mkdir -p /opt/MutualFundAnalysis
RUN mkdir -p /opt/env
ADD . /opt/MutualFundAnalysis
ADD /xy/application/env /opt/env

RUN mkdir /var/run/sshd -p
EXPOSE 22
EXPOSE 8000

WORKDIR /opt/MutualFundAnalysis

CMD source /opt/env/bin/activate && python manage.py runserver 0.0.0.0:8000 && tail -f /etc/hosts