
#!  /usr/bin/env  python
#coding=utf-8

import  os
import  time

def git_down_project():
    print("gitproject")
    print("���ڸ��¶�Ӧ����Ŀ")
    os.popen("git pull origin master")
    print("�ȴ���Ŀ�������")
    time.sleep(15)
    print("��Ŀ�������")


def find_uwsgi():
    print("����uwsgi���̷���")
    uwsgiList =os.popen("ps -ef |grep uwsgi | awk '{print $2}'").readlines()
    print("uwsgi���̼���Ϊ%s"%uwsgiList)
    return uwsgiList

def kill_uwsgi(pidlist):
    uwsgiList=pidlist
    if len(uwsgiList)<6:
        pass
        print("uwsgi������δ����"%uwsgiList)
    else:
        for pidid in uwsgiList:
            os.popen("kill -9 %s" %pidid)
            print("��ǰ����Ľ���idΪ%s"%pidid)
        print("�������")

def start_uwsgi():
    filelist=os.popen("ls").readlines()
    print(filelist)
    if "uwsgi.sock\n" in filelist:
        print(filelist)
        os.popen("rm -rf uwsgi.sock")
        print("����uwsgi.sock�ļ�")
        time.sleep(3)
        print("����uwsgi�ļ�")
        os.popen("uwsgi --ini zhuzher-TMG.ini")
        print("uwsgi�����ɹ�����Ŀ������")
    else:
        print("end")

def restart_uwsgi():
    git_down_project()
    uwsgiList=find_uwsgi()
    kill_uwsgi(uwsgiList)
    start_uwsgi()


if __name__ == '__main__':
    restart_uwsgi()
