
#!  /usr/bin/env  python
#coding=utf-8

import  os
import  time

def git_down_project():
    print("gitproject")
    print("正在更新对应的项目")
    os.popen("git pull origin master")
    print("等待项目更新完毕")
    time.sleep(15)
    print("项目更新完成")


def find_uwsgi():
    print("查找uwsgi进程服务")
    uwsgiList =os.popen("ps -ef |grep uwsgi | awk '{print $2}'").readlines()
    print("uwsgi进程集合为%s"%uwsgiList)
    return uwsgiList

def kill_uwsgi(pidlist):
    uwsgiList=pidlist
    if len(uwsgiList)<6:
        pass
        print("uwsgi进程尚未启动"%uwsgiList)
    else:
        for pidid in uwsgiList:
            os.popen("kill -9 %s" %pidid)
            print("当前清理的进程id为%s"%pidid)
        print("清理完成")

def start_uwsgi():
    filelist=os.popen("ls").readlines()
    print(filelist)
    if "uwsgi.sock\n" in filelist:
        print(filelist)
        os.popen("rm -rf uwsgi.sock")
        print("清理uwsgi.sock文件")
        time.sleep(3)
        print("启动uwsgi文件")
        os.popen("uwsgi --ini zhuzher-TMG.ini")
        print("uwsgi启动成功，项目已重启")
    else:
        print("end")

def restart_uwsgi():
    git_down_project()
    uwsgiList=find_uwsgi()
    kill_uwsgi(uwsgiList)
    start_uwsgi()


if __name__ == '__main__':
    restart_uwsgi()
