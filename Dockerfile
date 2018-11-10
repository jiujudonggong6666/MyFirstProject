# 基础镜像信息
# 1、第一行必须指定 基础镜像信息
FROM ubuntu:16.04

# 2、维护者信息
MAINTAINER 464983934@qq.com

COPY . /home/lijunxing/MyFirstProject
WORKDIR /home/lijunxing/MyFirstProject
RUN apt-get update
RUN apt-get install -y nginx
COPY default /etc/nginx/sites-enabled
RUN pip3 install -r requirements.txt
RUN uswgi --ini uwsgi.ini

#RUN python /home/lijunxing/MyFirstProject/run.py
EXPOSE 80
#CMD nginx -g 'daemon off;'
