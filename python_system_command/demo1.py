#!/usr/bin/env python
# encoding: utf-8

"""
@author: Andy Cheng
@license: Apache Licence 
@file: demo1.py
@time: 2019/6/2 12:29
"""
import os
import subprocess

# 不能获得命令的返回信息
command = os.system('cat /etc/profile')

output = os.popen('cat /etc/profile')
print(output.read())

# windowns
res = subprocess.run(['dir', 'D:'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     shell=True)
print(res.returncode, res.stdout.decode('GB2312'))

# linux
grep = subprocess.Popen(args=["grep --help"], shell=True, stdout=subprocess.PIPE)
ret = subprocess.call(["ls", "-l"], shell=False)
