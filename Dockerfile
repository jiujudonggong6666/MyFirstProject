# 基础镜像信息
# 1、第一行必须指定 基础镜像信息
FROM ubuntu:16.04

# 2、维护者信息
MAINTAINER 464983934@qq.com

COPY . /home/lijunxing/MyFirstProject
#RUN sudo apt-get update

#RUN sudo apt-get install nginx

WORKDIR /home/lijunxing/MyFirstProject


EXPOSE 80
