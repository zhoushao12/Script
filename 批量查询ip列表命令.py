#/usr/bin/env python
#encoding=utf8
import os
import paramiko
port = 22
file=open("ip.list")
for line in file:
    hostname = str(line.split(",")[0])
    ipaddress = str(line.split(",")[1])
    username = str(line.split(",")[2])
    password = str(line.split(",")[3]).strip()
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn=s.connect(ipaddress,port,username,password)
    stdin,stdout1,sterr=s.exec_command("df -h")
    stdin,stdout2,sterr=s.exec_command("df -i")
    print "#########", hostname, "###########"
    print stdout1.read()
    print stdout2.read()
    print "#########检查完成###########"
    s.close()
file.close()