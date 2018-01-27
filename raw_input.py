#!/usr/bin/env python
# encoding=utf-8
name = raw_input('Please Input Your Nmae:')
age = raw_input('Please Input Your Age:')
job = raw_input('Job:')
sel = input('sae:')
if name == 'jimoon':
    print 'Wlcome in %s:'% name
    print age
    print '''
        Wlcome in %s':
        name :%s
        age :%s
        job:%s
------------------------
    ''' % (name,name,age,job)
#%s 代表字符串，%d 代表数据，%f代表浮点数
#raw_input 输入均代表为字符串输入
#input 输入为整数数字
#如果需要转换为数据则需要int(raw_input('age:'))