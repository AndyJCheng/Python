#!/usr/bin/env python
# encoding: utf-8

"""
@author: Andy Cheng
@license: Apache Licence 
@file: commandline.py
@time: 2019/5/27 21:59
"""
import subprocess

res = subprocess.run(['dir', 'D:'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     shell=True)
print(res.returncode, res.stdout.decode('GB2312'))

