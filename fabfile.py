#!/usr/bin/env python
#encoding=utf-8
from fabric.api import *
env.hosts=['127.0.0.1','127.0.0.1']
env.passwords = {
    'monit@127.0.0.1:22':'Passw0rd',
    'monit@127.0.0.1:22':'Passw0rd',
}
@runs_once
def input_raw():
    return prompt("Please input directory name:",default="/home")
