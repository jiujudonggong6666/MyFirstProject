# 基础镜像信息
# 1、第一行必须指定 基础镜像信息
FROM ubuntu:16.04
FROM python
#FROM nginx

# 2、维护者信息
MAINTAINER 464983934@qq.com

COPY . /home/lijunxing/my-project

#RUN apt-get update
#RUN apt-get install python3-pip
#RUN pip3 install --upgrade pip
#RUN pip3 install Flask
#RUN apt-get update
#RUN  pip3 install -r /home/lijunxing/my-project/requirements.txt
#RUN  uwsgi --ini uwsgi.ini
#VOLUME /etc/nginx/sites-enabled/myproject .myproject
#CMD 运行以下命令
CMD ["python","/home/lijunxing/MyFirstProject/run.py"]

EXPOSE 8080