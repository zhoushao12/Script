#encoding=utf8
import sys
import paramiko

hostname = "192.168.146.128"
command = "df -h"
port = 22
username = "oracle"
password = "oracle"
if __name__ == "__main__":
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, port, username, password)
    stdin, stdout, sterr = s.exec_command(command)
    print "以下为主机：%s磁盘空间使用情况" % hostname
    print stdout.read()
    s.close()