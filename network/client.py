#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: client.py
@time: 2018/8/4 22:40
"""
import socket

sk = socket.socket()
ip_port = ('localhost', 9998)

sk.connect(ip_port)

with open(r'D:\python_project\python\Pipfile', 'rb') as f:
    for i in f:
        sk.send(i)
sk.send('quit'.encode())

