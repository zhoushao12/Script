#!/usr/bin/env python
# encoding=utf-8
name = raw_input('Please Input Your Nmae:')
#age = raw_input('Please Input Your Age:') 代表字符型在判断数字时会无法判断，需要进行数字输入
age = input('gae:')
job = raw_input('Job:')
sel = input('sae:')
#%s 代表字符串，%d 代表数据，%f代表浮点数
#raw_input 输入均代表为字符串输入
#input 输入为整数数字
#如果需要转换为数据则需要int(raw_input('age:'))
if age > 5:
    msg ='年龄大于5岁'
elif age >50:
    msg='年龄大于50'
else:
    msg='年龄小于5岁'
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