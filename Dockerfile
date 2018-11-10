# 基础镜像信息
# 1、第一行必须指定 基础镜像信息
FROM ubuntu:16.04
FROM python
#FROM nginx

# 2、维护者信息
MAINTAINER 464983934@qq.com

COPY . /home/lijunxing/MyFirstProject
RUN  pip3 install -r /home/lijunxing/MyFirstProject/requirements.txt
RUN  uwsgi --ini /home/lijunxing/MyFirstProject/uwsgi.ini
#VOLUME /etc/nginx/sites-enabled/myproject /etc/nginx/sites-enabled/myproject
#CMD ["nginx"]
#CMD ["nginx", "-g", "daemon off;"]
CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]
EXPOSE 8080