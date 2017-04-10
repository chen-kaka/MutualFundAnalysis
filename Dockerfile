FROM daocloud.io/django:onbuild
MAINTAINER chen_kaka <chen-kaka@163.com>

RUN mkdir -p /opt/MutualFundAnalysis
ADD . /opt/MutualFundAnalysis

RUN mkdir /var/run/sshd -p
EXPOSE 22
EXPOSE 8000

WORKDIR /opt/MutualFundAnalysis
CMD python manage.py runserver 0.0.0.0:8000 && tail -f /etc/hosts