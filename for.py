#!/usr/bin/env python
# encoding=utf-8
name = raw_input('Please Input Your Nmae:')
#age = raw_input('Please Input Your Age:') 代表字符型在判断数字时会无法判断，需要进行数字输入
real_age = 29
job = raw_input('Job:')
sel = input('sae:')
for i in range(10):
    age = input('gae:')
    if age > 40:
        msg = '年龄大于40'
    elif age == 29:
        msg = '\033[32;1m年龄等于29,goog\033[0m,gooe'
#输出颜色高亮
        break
        #跳出循环
    else:
        msg = '年龄小于40'
    print '剩余输入次数小于 %s' % (9 - i)
print '''
Personal information of %s:
    name: %s
    age: %s
    job: %s
    sel: %s
################
    msg: %s
    name %s age %s
''' % (name,name,age,job,sel,msg,name,msg)
print '''
    name %s age %s
''' %(name,msg)